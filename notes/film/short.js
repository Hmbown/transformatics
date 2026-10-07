// A restrained vertical cut. One moving diagram per narrated beat.
// Geometry reused from film.js is checked by checks.mjs. Caption cues are
// phrase estimates within each beat, not claimed audio word alignment.
'use strict';
const SW_ = 1080, SH_ = 1920;
let STL = null, LANG = 'en';
const STEXT = {
 en: {
  intro: 'Two results with a force', introSub: 'OpenAI · September–October 2026',
  blowup: 'Finite-time breakdown', blowupSub: 'A smooth force; an unbounded peak speed',
  energy: 'Energy stays bounded', energySub: 'The fast region shrinks toward a point',
  force: 'The force supplies energy', forceSub: 'This construction starts from rest',
  compute: 'A smooth flow can compute', computeSub: 'The force depends on the machine and input',
  halt: 'A particle detects halting', haltSub: 'Entering the box means the program has stopped',
  open: 'The unforced question remains open', openSub: 'General smooth initial data in three dimensions',
  peak: 'Peak speed', coreEnergy: 'Core energy', volume: 'Volume ratio',
  fixed: 'Fixed scale · schematic core', scale: 'Published scalings, with h = 0.005',
  initial: 'Initially at rest', rest: 'No force: the fluid stays at rest',
  target: 'Target box', trajectory: 'A schematic halting trajectory',
  condition: 'Enters the box ⇔ the machine halts',
  example: 'Taylor–Green cells · an exact unforced example',
  source: 'OpenAI: Finite time blowup for Navier–Stokes; openai/math, family 376.',
 },
 zh: {
  intro: '两个使用外力的结果', introSub: 'OpenAI · 2026 年 9–10 月',
  blowup: '有限时间内失去光滑性', blowupSub: '外力光滑，峰值速度趋于无穷',
  energy: '能量保持有界', energySub: '高速区域向一点收缩',
  force: '外力提供能量', forceSub: '这个构造从静止出发',
  compute: '光滑流动能够执行计算', computeSub: '外力由机器和输入决定',
  halt: '用粒子检测停机', haltSub: '进入盒子，表示程序已停止',
  open: '无外力的问题仍未解决', openSub: '三维空间中的一般光滑初始条件',
  peak: '峰值速度', coreEnergy: '核心能量', volume: '体积比',
  fixed: '固定比例 · 核心示意图', scale: '论文中的尺度，取 h = 0.005',
  initial: '初始静止', rest: '没有外力：流体保持静止',
  target: '目标盒子', trajectory: '停机轨迹的示意图',
  condition: '进入盒子 ⇔ 机器停机',
  example: 'Taylor–Green 涡胞 · 无外力的精确解',
  source: '来源：OpenAI《Finite time blowup for Navier–Stokes》；openai/math 第 376 族。',
 },
};
const sl = k => STEXT[LANG][k];
function st(s, x, y, size = 38, opts = {}) { text(s, x, y, { font: SANS, size, ...opts }); }
function heading(id, τ) {
 const a = ramp(τ, 0, .35);
 st(sl(id), 84, 170, LANG === 'zh' ? 54 : (id === 'open' ? 47 : 52), { weight: '600', alpha: a });
 st(sl(id + 'Sub'), 84, 237, LANG === 'zh' ? 31 : 30, { color: C.muted, alpha: a });
}
function caption(T) {
 const beat = STL.scenes.flatMap(s => s.beats).find(b => T >= b.start && T < b.end);
 if (!beat) return;
 const cue = beat.cues?.find(c => T >= c.start && T < c.end);
 if (!cue) return;
 const size = LANG === 'zh' ? 46 : 45;
 g.save(); g.font = `${size}px ${SANS}`;
 const tokens = LANG === 'zh' ? Array.from(cue.cap) : cue.cap.split(' ');
 let lines = [], line = '';
 for (const word of tokens) {
  const next = line + (line && LANG !== 'zh' ? ' ' : '') + word;
  if (g.measureText(next).width > 890 && line) { lines.push(line); line = word; } else line = next;
 }
 if (line) lines.push(line);
 g.restore();
 lines.forEach((l, i) => st(l, 84, 1515 + i * 65, size));
}
const SS = {};
const SB = {x:160,y:420,s:760};
function cell(τ, scale = 1) {
 drawStreamlines(.32, SB);
 drawTGDots(3 + τ * scale, .9, {b: SB, radius: 4});
 g.save(); g.strokeStyle=C.faint; g.lineWidth=2; g.strokeRect(SB.x,SB.y,SB.s,SB.s); g.restore();
}
SS.intro = τ => {
 cell(τ,.7);
 st(sl('example'),540,1250,26,{align:'center',color:C.muted});
};
function core(τ,D,start,end,energy) {
 const q = smooth(clamp((τ-.4)/Math.max(1,D-1)));
 const tau = 10**lerp(start,end,q), r=260*Math.sqrt(tau), z=260*tau**.495;
 g.save(); g.strokeStyle=C.faint; g.lineWidth=2;
 g.beginPath();g.moveTo(540,380);g.lineTo(540,1110);g.stroke();
 g.fillStyle=rgba(C.red,.18);g.strokeStyle=C.red;g.lineWidth=4;
 g.beginPath();g.ellipse(540,745,Math.max(r,2),Math.max(z,2),0,0,TAU);g.fill();g.stroke();g.restore();
 const speed=tau**-.505, e=tau**.485;
 st(sl('fixed'),540,1160,28,{align:'center',color:C.muted});
 st(`${sl('peak')}  ×${speed.toFixed(1)}`,540,1232,45,{align:'center',color:C.red});
 if(energy)st(`${sl('coreEnergy')}  ×${e.toFixed(3)}`,540,1297,42,{align:'center',color:C.blue});
 st(sl('scale'),540,1380,25,{align:'center',color:C.muted});
}
SS.blowup=(τ,D)=>core(τ,D,0,-2,false);
SS.energy=(τ,D)=>core(τ,D,-2,-4,true);
SS.force=τ=>{
 // The particles are at rest throughout this example. Cutting force from a
 // moving Taylor–Green solution would not make it stop instantaneously.
 g.save();g.fillStyle=C.blue;
 for(let i=0;i<13;i++)for(let j=0;j<13;j++){
  g.beginPath();g.arc(190+i*58,410+j*58,4,0,TAU);g.fill();
 }g.restore();
 st('u(0) = 0,   f = 0',540,1225,58,{align:'center'});
 st('u(t) = 0',540,1320,58,{align:'center',color:C.blue,alpha:ramp(τ,2,.6)});
};
SS.compute=(τ,D)=>{
 const progress=2*smooth(clamp((τ-3)/Math.max(3,D-4)));
 drawProgramExample({x:84,y:420,w:912,h:830},progress,LANG);
};
SS.halt=(τ,D)=>{
 const p=clamp((τ-.6)/(D*.65));
 const xy=s=>[150+690*s,1000-440*s+55*Math.sin(6*s)];
 g.save();g.fillStyle=rgba(C.teal,.10);g.strokeStyle=C.teal;g.lineWidth=3;
 g.fillRect(725,440,230,230);g.strokeRect(725,440,230,230);
 g.strokeStyle=C.blue;g.lineWidth=5;g.beginPath();
 for(let i=0;i<=Math.round(p*150);i++){const [x,y]=xy(i/150);i?g.lineTo(x,y):g.moveTo(x,y);}g.stroke();
 const [x,y]=xy(p);g.fillStyle=C.blue;g.beginPath();g.arc(x,y,12,0,TAU);g.fill();g.restore();
 st(sl('target'),840,402,30,{align:'center',color:C.teal});
 st(sl('trajectory'),540,1165,28,{align:'center',color:C.muted});
 st(sl('condition'),540,1260,LANG==='zh'?40:35,{align:'center'});
};
SS.open=τ=>{
 cell(τ,.65);
 st(sl('example'),540,1260,26,{align:'center',color:C.muted});
};
window.setTimeline=tl=>{
 STL=tl;LANG=tl.language||'en';
 document.documentElement.lang=LANG==='zh'?'zh-CN':'en';
 // Short has its own bilingual text; shared math helpers remain language-neutral.
 FILM_LANG='en';buildTG(tgS(40));
};
window.renderFrame=T=>{
 const sc=STL.scenes.find(sc=>T<sc.end)||STL.scenes.at(-1),τ=T-sc.start,D=sc.end-sc.start;
 g.setTransform(1,0,0,1,0,0);g.globalAlpha=1;g.fillStyle=C.bg;g.fillRect(0,0,SW_,SH_);
 heading(sc.id,τ);SS[sc.id](τ,D);caption(T);
 g.fillStyle=C.faint;g.fillRect(84,1432,912,2);
 st(LANG==='zh'?'Transformatics · Hunter Bown 的学习笔记':'Transformatics · Hunter Bown’s learning notes',84,1770,24,{color:C.muted});
 wrapText(sl('source'),84,1820,900,{size:20,font:SANS,color:C.muted,lh:29});
 return sc.id;
};
