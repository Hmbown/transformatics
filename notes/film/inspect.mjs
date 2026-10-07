// Inspect every narrated beat (plus credits), save stills, and report text
// outside the frame. This checks presentation, not the papers' PDE proofs.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {chromium} from 'playwright';
const here=path.dirname(fileURLToPath(import.meta.url));
const arg=(k,d)=>{const i=process.argv.indexOf(k);return i<0?d:process.argv[i+1];};
const out=path.resolve(arg('--out')),short=process.argv.includes('--short');
const tl=JSON.parse(fs.readFileSync(path.join(out,'timeline.json'),'utf8'));
const size=short?{width:1080,height:1920}:{width:1920,height:1080};
const browser=await chromium.launch({args:['--font-render-hinting=none','--disable-lcd-text']});
const page=await browser.newPage({viewport:size,deviceScaleFactor:1});
const errors=[];
page.on('pageerror',e=>errors.push(e.message));
await page.goto(pathToFileURL(path.join(here,short?'short.html':'film.html')).href);
await page.evaluate(tl=>window.setTimeline(tl),tl);
await page.evaluate(async()=>{await document.fonts.ready;});
await page.evaluate(()=>{
 window.drawnText=[];
 const original=CanvasRenderingContext2D.prototype.fillText;
 CanvasRenderingContext2D.prototype.fillText=function(s,x,y,...rest){
  if(this.canvas.id==='c'&&this.globalAlpha>.2){
   const m=this.measureText(s),a=this.textAlign,b=this.textBaseline;
   const left=x-(a==='center'?m.width/2:(a==='right'||a==='end')?m.width:0);
   const height=m.actualBoundingBoxAscent+m.actualBoundingBoxDescent;
   const top=y-(b==='middle'?height/2:(b==='top'||b==='hanging')?0:m.actualBoundingBoxAscent);
   const t=this.getTransform(),p=t.transformPoint({x:left,y:top}),q=t.transformPoint({x:left+m.width,y:top+height});
   window.drawnText.push({text:String(s),x:p.x,y:p.y,right:q.x,bottom:q.y});
  }
  return original.call(this,s,x,y,...rest);
 };
});
const dir=path.join(out,'review-stills');fs.mkdirSync(dir,{recursive:true});
const samples=[],overflow=[],texts=new Set();
let n=0;
for(const sc of tl.scenes){
 const beats=sc.beats.length?sc.beats:[{start:sc.start+1,end:sc.end-1}];
 for(let bi=0;bi<beats.length;bi++){
  const beat=beats[bi],T=(beat.start+beat.end)/2;
  const result=await page.evaluate(T=>{
   window.drawnText=[];window.renderFrame(T);
   const math=[...document.querySelectorAll('.eq')].filter(d=>+d.style.opacity>.2).map(d=>{
    const r=d.getBoundingClientRect();return{text:d.textContent,x:r.x,y:r.y,right:r.right,bottom:r.bottom};
   });
   return{text:window.drawnText,math};
  },T);
  for(const r of [...result.text,...result.math]){
   texts.add(r.text);
   if(r.x < -2||r.y < -2||r.right > size.width+2||r.bottom > size.height+2)
    overflow.push({scene:sc.id,beat:bi,time:T,...r});
  }
  const name=`${String(n++).padStart(3,'0')}-${sc.id}-${bi}.png`;
  await page.screenshot({path:path.join(dir,name)});
  samples.push({scene:sc.id,beat:bi,time:T,file:name});
 }
}
const report={language:tl.language,scenes:tl.scenes.length,frames:samples.length,errors,overflow,texts:[...texts],samples};
fs.writeFileSync(path.join(out,'visual-report.json'),JSON.stringify(report,null,2));
console.log(JSON.stringify({language:tl.language,scenes:tl.scenes.length,frames:samples.length,errors,overflow}));
await browser.close();
if(errors.length||overflow.length)process.exitCode=1;
