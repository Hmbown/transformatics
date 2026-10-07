// Render the film with headless Chromium and ffmpeg.
//
//   node render.mjs --out /external/output
//   node render.mjs --out /external/output --stills 20,61.5
//   node render.mjs --out /external/output --from 54 --to 96
//
// Run `python narrate.py ...` first: it writes out/timeline.json and
// out/narration.wav, which fix every scene's timing.
import { spawn } from 'node:child_process';
import { chromium } from 'playwright';
import fs from 'node:fs';
import crypto from 'node:crypto';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));

const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };
// --out DIR (timeline.json, narration.wav, captions.vtt live here), --page film.html|short.html,
// --size 1920x1080|1080x1920, --lang eng|chi (subtitle track language)
if (!arg('--out')) throw new Error('An external --out directory is required.');
const out = path.resolve(here, arg('--out'));
const repo = path.resolve(here, '../..');
if (out === repo || out.startsWith(repo + path.sep)) throw new Error('Keep renders outside the repository.');
const PAGE = arg('--page', 'film.html');
const [VW, VH] = arg('--size', '1920x1080').split('x').map(Number);
const SUBLANG = arg('--lang', 'eng');
const FPS = Number(arg('--fps', 30));
const timeline = JSON.parse(fs.readFileSync(path.join(out, 'timeline.json'), 'utf8'));
const hash = p => crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const sourceFiles = ['film.js', 'labels.zh.js', PAGE, ...(PAGE === 'short.html' ? ['short.js'] : [])];
const sourceHashes = Object.fromEntries(sourceFiles.map(p => [p, hash(path.join(here, p))]));

const browser = await chromium.launch({
  args: ['--font-render-hinting=none', '--disable-lcd-text'],
});
const page = await browser.newPage({ viewport: { width: VW, height: VH }, deviceScaleFactor: 1 });
let pageError;
page.on('pageerror', e => { pageError = e; });
await page.goto(pathToFileURL(path.join(here, PAGE)).href);
await page.evaluate(async () => { await document.fonts.ready; });
await page.evaluate(tl => window.setTimeline(tl), timeline);
await page.evaluate(async () => { await document.fonts.ready; });

const stills = arg('--stills');
if (stills) {
  fs.mkdirSync(path.join(out, 'stills'), { recursive: true });
  for (const s of stills.split(',')) {
    const t = Number(s);
    const id = await page.evaluate(t => window.renderFrame(t), t);
    const file = path.join(out, 'stills', `${t.toFixed(1).padStart(6, '0')}-${id}.png`);
    await page.screenshot({ path: file });
    console.log(file);
  }
  await browser.close();
  process.exit();
}

const from = Number(arg('--from', 0));
const to = Math.min(Number(arg('--to', timeline.duration)), timeline.duration);
if (!(Number.isFinite(FPS) && FPS > 0 && from >= 0 && to > from)) throw new Error('Invalid frame rate or time range.');
const name = arg('--name', from === 0 && to === timeline.duration ? 'transformatics-film' : `preview-${from}-${to}`);
const video = path.join(out, `${name}.mp4`);
const ff = spawn('ffmpeg', [
  '-y', '-loglevel', 'error',
  '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
  '-ss', String(from), '-t', String(to - from), '-i', path.join(out, 'narration.wav'),
  ...(from === 0 && to === timeline.duration ? ['-i', path.join(out, 'captions.vtt')] : []),
  '-map', '0:v', '-map', '1:a', '-metadata:s:a:0', `language=${SUBLANG}`, ...(from === 0 && to === timeline.duration ? ['-map', '2:s', '-c:s', 'mov_text', '-metadata:s:s:0', `language=${SUBLANG}`] : []),
  '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p', '-tune', 'animation',
  '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart',
  '-metadata', `title=${timeline.title}`, '-t', String(to - from), video,
], { stdio: ['pipe', 'inherit', 'inherit'] });
const finished = new Promise(resolve => {
  ff.on('error', error => resolve({ error }));
  ff.on('close', code => resolve({ code }));
});
ff.stdin.on('error', () => {}); // write callbacks below report the failure

const n = Math.round((to - from) * FPS);
const t0 = Date.now();
try {
  for (let k = 0; k < n; k++) {
    if (pageError) throw pageError;
    await page.evaluate(t => window.renderFrame(t), from + k / FPS);
    const buf = await page.screenshot({ type: 'jpeg', quality: 95 });
    await new Promise((resolve, reject) => ff.stdin.write(buf, error => error ? reject(error) : resolve()));
    if (k % 300 === 0) console.log(`frame ${k}/${n}  ${((Date.now() - t0) / 1000).toFixed(0)} s`);
  }
  ff.stdin.end();
  const result = await finished;
  if (result.error || result.code !== 0) throw result.error || new Error(`ffmpeg failed: ${result.code}`);
  if (pageError) throw pageError;
  for (const [p, digest] of Object.entries(sourceHashes)) {
    if (hash(path.join(here, p)) !== digest) throw new Error(`Source changed during render: ${p}`);
  }
  fs.writeFileSync(path.join(out, `${name}-render.json`), JSON.stringify({
    video, width: VW, height: VH, fps: FPS, frames: n, from, to,
    sources: sourceHashes, timeline_sha256: hash(path.join(out, 'timeline.json')),
    narration_sha256: hash(path.join(out, 'narration.wav')), encoder_exit: result.code,
  }, null, 2));
  console.log(video);
} finally {
  if (!ff.stdin.writableEnded) { ff.stdin.destroy(); ff.kill('SIGTERM'); }
  await browser.close();
}
