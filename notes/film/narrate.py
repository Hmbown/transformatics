"""Make English or Mandarin speech, timing, and captions with standard Edge voices.

Only narration text is sent. Outputs and request caches must be outside the
repository. Provider word events check the returned text; they do not prove
that every word is audible. Listening and duration review remain necessary.
"""
import argparse
import asyncio
import hashlib
import html
import json
import re
import subprocess
import unicodedata
import wave
from pathlib import Path

import edge_tts
import numpy as np
GAP = 0.55


def vtt_time(s):
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{sec:06.3f}"

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]


def norm(s):
    return ''.join(c for c in unicodedata.normalize('NFKC', s).lower() if c.isalnum())


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=1) + '\n')


async def synthesize(text, voice, rate, stem):
    request = dict(text=text, voice=voice, rate=rate, boundary='WordBoundary')
    key = hashlib.sha256(json.dumps(request, sort_keys=True).encode()).hexdigest()
    mp3, receipt = stem.with_suffix('.mp3'), stem.with_suffix('.json')
    if mp3.exists() and receipt.exists():
        cached = json.loads(receipt.read_text())
        if cached.get('request_sha256') == key and cached.get('audio_sha256') == hashlib.sha256(mp3.read_bytes()).hexdigest():
            return cached['words']
    tmp = stem.with_suffix('.mp3.part')
    for attempt in range(3):
        words = []
        try:
            with tmp.open('wb') as f:
                async for chunk in edge_tts.Communicate(**request, connect_timeout=30, receive_timeout=60).stream():
                    if chunk['type'] == 'audio':
                        f.write(chunk['data'])
                    elif chunk['type'] == 'WordBoundary':
                        words.append({'w': html.unescape(chunk['text']), 's': chunk['offset'] / 1e7,
                                      'e': (chunk['offset'] + chunk['duration']) / 1e7})
            if not words or tmp.stat().st_size < 1000:
                raise ValueError('Missing speech or word events')
            if norm(''.join(w['w'] for w in words)) != norm(text):
                raise ValueError(f'Returned speech text differs: {words!r}')
            tmp.replace(mp3)
            save(receipt, {'request_sha256': key, 'request': request, 'words': words,
                           'audio_sha256': hashlib.sha256(mp3.read_bytes()).hexdigest()})
            return words
        except Exception:
            if attempt == 2:
                raise
            await asyncio.sleep(2 * (attempt + 1))


def pcm(path):
    with wave.open(str(path)) as w:
        assert w.getnchannels() == 1 and w.getframerate() == 48000
        return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768


def caption_cues(beat, lang):
    # Preserve the caption spelling (math symbols can differ from the spoken
    # words). These are phrase timings, not claimed forced word alignment.
    cap = beat['cap']
    tokens = re.findall(r'[A-Za-z0-9]+(?:[’\-][A-Za-z0-9]+)*|[^\sA-Za-z0-9]', cap) if lang == 'zh' else cap.split()
    limit = 24 if lang == 'zh' else 78
    chunks, current = [], ''
    for token in tokens:
        sep = '' if lang == 'zh' else ' '
        candidate = current + (sep if current else '') + token
        if len(candidate) > limit and current:
            chunks.append(current)
            current = token
        else:
            current = candidate
        if re.search(r'[。！？!?;；]$', current) or (len(current) > limit * .45 and re.search(r'[,.，：:]$', current)):
            chunks.append(current)
            current = ''
    if current:
        chunks.append(current)
    weights = [max(1, len(norm(c))) for c in chunks]
    total, used = sum(weights), 0
    start, end = beat['start'], beat['end']
    cues = []
    for c, w in zip(chunks, weights):
        a = start + (end - start) * used / total
        used += w
        b = start + (end - start) * used / total
        cues.append({'start': round(a, 3), 'end': round(b, 3), 'cap': c})
    return cues


async def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script', type=Path, default=HERE / 'script.json')
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--voice', required=True)
    ap.add_argument('--rate', default='-5%')
    ap.add_argument('--only-scene', help='Generate a sample containing just this scene')
    args = ap.parse_args()
    out = args.out.resolve()
    if out.is_relative_to(REPO):
        raise SystemExit('Keep generated audio outside the repository; choose an external --out.')
    out.mkdir(parents=True, exist_ok=True)
    (out / 'beats').mkdir(exist_ok=True)
    script = json.loads(args.script.read_text())
    lang = script.get('language', 'en')
    source = script['scenes']
    if args.only_scene:
        source = [sc for sc in source if sc['id'] == args.only_scene]
        if not source:
            raise SystemExit('Scene not found')
    clock, scenes, pieces, report = 0., [], [], []
    for si, sc in enumerate(source):
        start = clock
        clock += sc['lead']
        beats = []
        for bi, beat in enumerate(sc['beats']):
            stem = out / 'beats' / f'{sc["id"]}-{bi:02}'
            words = await synthesize(beat['say'], args.voice, args.rate, stem)
            wav = stem.with_suffix('.wav')
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(stem.with_suffix('.mp3')),
                            '-ac', '1', '-ar', '48000', '-c:a', 'pcm_s16le', str(wav)], check=True)
            data = pcm(wav)
            dur = len(data) / 48000
            if not np.isfinite(data).all() or np.max(np.abs(data)) < .01:
                raise ValueError(f'Silent or invalid beat: {stem.name}')
            if words[-1]['e'] > dur + .25:
                raise ValueError(f'Word events extend beyond audio: {stem.name}')
            units = len(re.findall(r'[\u3400-\u9fff]|[A-Za-z]+', beat['say'])) if lang == 'zh' else len(beat['say'].split())
            pace = units / dur * 60
            low, high = (130, 380) if lang == 'zh' else (90, 230)
            flag = not (low <= pace <= high)
            report.append({'beat': stem.name, 'seconds': round(dur, 3),
                           'units_per_minute': round(pace, 1), 'duration_review_flag': flag,
                           'provider_text_match': True, 'peak_dbfs': round(float(20*np.log10(np.max(np.abs(data)))), 2)})
            pieces.append((clock, data))
            entry = {'start': round(clock, 3), 'end': round(clock + dur, 3), 'cap': beat['cap'],
                     'words': [{**w, 's': round(clock + w['s'], 3), 'e': round(clock + w['e'], 3)} for w in words]}
            entry['cues'] = caption_cues(entry, lang)
            beats.append(entry)
            clock += dur + GAP
            print(f'{stem.name}: {dur:.1f}s, {pace:.0f} units/min' + (' [review duration]' if flag else ''), flush=True)
        if beats:
            clock -= GAP
        clock += sc['tail']
        scenes.append({'id': sc['id'], 'start': round(start, 3), 'end': round(clock, 3), 'beats': beats})
    track = np.zeros(round(clock * 48000), dtype=np.float32)
    for at, data in pieces:
        i = round(at * 48000)
        track[i:i + len(data)] += data
    raw = out / 'narration-raw.wav'
    with wave.open(str(raw), 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(48000)
        w.writeframes((np.clip(track, -1, 1) * 32767).astype(np.int16).tobytes())
    # Two-pass loudness normalization; no music or speech time-stretching.
    result = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', str(raw),
                             '-af', 'loudnorm=I=-18:TP=-2:LRA=9:print_format=json', '-f', 'null', '-'],
                            capture_output=True, text=True, check=True)
    loud, _ = json.JSONDecoder().raw_decode(result.stderr[result.stderr.rfind('{'):])
    filt = ('loudnorm=I=-18:TP=-2:LRA=9:linear=true:'
            f'measured_I={loud["input_i"]}:measured_TP={loud["input_tp"]}:'
            f'measured_LRA={loud["input_lra"]}:measured_thresh={loud["input_thresh"]}:'
            f'offset={loud["target_offset"]}')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(raw), '-af', filt,
                    '-ar', '48000', '-c:a', 'pcm_s16le', str(out / 'narration.wav')], check=True)
    timeline = {'title': script['title'], 'language': lang, 'voice': args.voice, 'rate': args.rate,
                'caption_timing': 'Phrases apportioned within beat duration; provider word events also retained.',
                'script_sha256': hashlib.sha256(args.script.read_bytes()).hexdigest(),
                'duration': round(clock, 3), 'scenes': scenes}
    save(out / 'timeline.json', timeline)
    save(out / 'audio-report.json', {'voice': args.voice, 'rate': args.rate, 'beats': report,
                                    'loudness_first_pass': loud, 'human_listening': 'pending'})
    lines = ['WEBVTT', '']
    cues = [cue for sc in scenes for beat in sc['beats'] for cue in beat['cues']]
    for i, cue in enumerate(cues, 1):
        lines += [str(i), f'{vtt_time(cue["start"])} --> {vtt_time(cue["end"])}', cue['cap'], '']
    (out / 'captions.vtt').write_text('\n'.join(lines))
    print(f'{len(report)} beats; {clock:.1f}s; {sum(r["duration_review_flag"] for r in report)} duration flags', flush=True)


if __name__ == '__main__':
    asyncio.run(main())
