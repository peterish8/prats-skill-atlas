import assert from 'node:assert/strict';
import { createMotionStage } from '../packages/tokens/dist/index.js';

// SSR must not touch browser globals.
const server = createMotionStage({});
server.update({paused:true}); server.destroy();

class Media extends EventTarget { constructor(matches) { super(); this.matches=matches; } change(matches) { this.matches=matches; this.dispatchEvent(new Event('change')); } }
class Stage extends EventTarget {
  dataset={}; properties=new Map();
  style={setProperty:(name,value)=>this.properties.set(name,value)};
  getBoundingClientRect(){return {left:0,top:0,width:400,height:200};}
}
const reduced=new Media(false), pointer=new Media(true), frames=new Map();
let frameId=0, observer;
globalThis.window={
  matchMedia:q=>q.includes('reduced-motion')?reduced:pointer,
  requestAnimationFrame:callback=>{frames.set(++frameId,callback);return frameId;},
  cancelAnimationFrame:id=>frames.delete(id)
};
globalThis.document=new EventTarget(); document.visibilityState='visible';
globalThis.IntersectionObserver=class { constructor(callback){this.callback=callback;observer=this;} observe(){} disconnect(){this.disconnected=true;} };
const stage=new Stage(), controller=createMotionStage(stage,{intensity:1});
assert.equal(stage.dataset.motionRunning,'true');
function move(x=400,y=200,type='mouse') {
  const event=new Event('pointermove');Object.assign(event,{clientX:x,clientY:y,pointerType:type});stage.dispatchEvent(event);
}
function flush(){const callbacks=[...frames.values()];frames.clear();callbacks.forEach(callback=>callback());}
move();move();assert.equal(frames.size,1,'pointer events coalesce into one frame');flush();
assert.equal(stage.properties.get('--tui-pointer-x'),'6.00px');
assert.equal(stage.properties.get('--tui-pointer-y'),'4.00px');
controller.update({paused:true,intensity:1});
assert.equal(stage.dataset.motionRunning,'false');move();assert.equal(frames.size,0);
assert.equal(stage.properties.get('--tui-pointer-x'),'0px');
controller.update({paused:false,intensity:100});move(9999,9999);flush();
assert.equal(stage.properties.get('--tui-pointer-x'),'6.00px','large coordinates/intensity remain bounded');
reduced.change(true);assert.equal(stage.dataset.motionRunning,'false');move();assert.equal(frames.size,0);
reduced.change(false);document.visibilityState='hidden';document.dispatchEvent(new Event('visibilitychange'));
assert.equal(stage.dataset.motionRunning,'false');
document.visibilityState='visible';document.dispatchEvent(new Event('visibilitychange'));
observer.callback([{isIntersecting:false}]);assert.equal(stage.dataset.motionRunning,'false');
observer.callback([{isIntersecting:true}]);assert.equal(stage.dataset.motionRunning,'true');
move(200,100,'touch');assert.equal(frames.size,0,'touch scrolling does not move decoration');
move();assert.equal(frames.size,1);stage.dispatchEvent(new Event('pointercancel'));assert.equal(frames.size,0);
controller.destroy();assert.ok(observer.disconnected);move();assert.equal(frames.size,0);
reduced.change(true);reduced.change(false);assert.equal(stage.dataset.motionRunning,'false','removed listeners cannot restart motion');
delete globalThis.window;delete globalThis.document;delete globalThis.IntersectionObserver;
console.log('Motion controller passed: SSR, coalescing, bounds, pause, reduced motion, hidden/offscreen, touch, cancel and teardown. Synthetic DOM unit check; browser evidence is separate.');
