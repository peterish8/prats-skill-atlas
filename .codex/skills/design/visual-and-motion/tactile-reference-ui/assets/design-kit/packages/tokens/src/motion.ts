export interface MotionStageOptions { paused?: boolean; intensity?: number }
export interface MotionStageController { update(options: MotionStageOptions): void; destroy(): void }

/** Shared DOM adapter: no framework updates per frame and no permanent frame loop. */
export function createMotionStage(element: HTMLElement, initial: MotionStageOptions = {}): MotionStageController {
  if (typeof window === 'undefined') return { update() {}, destroy() {} };
  let options = initial;
  let destroyed = false, visible = true, frame = 0;
  let targetX = 0, targetY = 0;
  let bounds = element.getBoundingClientRect();
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  const pointer = window.matchMedia('(hover: hover) and (pointer: fine)');
  const strength = () => Number.isFinite(options.intensity) ? Math.max(0, Math.min(1, options.intensity!)) : .6;
  const running = () => !destroyed && !options.paused && !reduced.matches && visible && document.visibilityState !== 'hidden';
  function reset() {
    if (frame) window.cancelAnimationFrame(frame);
    frame = 0; targetX = targetY = 0;
    element.style.setProperty('--tui-pointer-x', '0px');
    element.style.setProperty('--tui-pointer-y', '0px');
    element.style.setProperty('--tui-pointer-rx', '0deg');
    element.style.setProperty('--tui-pointer-ry', '0deg');
  }
  function sync() {
    element.dataset.motionRunning = String(running());
    if (!running() || !pointer.matches) reset();
  }
  function flush() {
    frame = 0;
    if (!running() || !pointer.matches) return;
    const multiplier = strength();
    element.style.setProperty('--tui-pointer-x', (targetX * 6 * multiplier).toFixed(2) + 'px');
    element.style.setProperty('--tui-pointer-y', (targetY * 4 * multiplier).toFixed(2) + 'px');
    element.style.setProperty('--tui-pointer-rx', (-targetY * 2 * multiplier).toFixed(2) + 'deg');
    element.style.setProperty('--tui-pointer-ry', (targetX * 3 * multiplier).toFixed(2) + 'deg');
  }
  function enter() { bounds = element.getBoundingClientRect(); }
  function move(event: PointerEvent) {
    if (!running() || !pointer.matches || event.pointerType === 'touch') return;
    targetX = Math.max(-1, Math.min(1, (event.clientX - bounds.left) / Math.max(1, bounds.width) * 2 - 1));
    targetY = Math.max(-1, Math.min(1, (event.clientY - bounds.top) / Math.max(1, bounds.height) * 2 - 1));
    if (!frame) frame = window.requestAnimationFrame(flush);
  }
  const observer = typeof IntersectionObserver !== 'undefined' ? new IntersectionObserver(entries => {
    visible = entries.some(entry => entry.isIntersecting);
    sync();
  }, { threshold: 0 }) : undefined;
  observer?.observe(element);
  element.addEventListener('pointerenter', enter);
  element.addEventListener('pointermove', move);
  element.addEventListener('pointerleave', reset);
  element.addEventListener('pointercancel', reset);
  reduced.addEventListener('change', sync);
  pointer.addEventListener('change', sync);
  document.addEventListener('visibilitychange', sync);
  sync();
  return {
    update(next) { options = next; sync(); },
    destroy() {
      destroyed = true; reset(); observer?.disconnect();
      element.dataset.motionRunning = 'false';
      element.removeEventListener('pointerenter', enter);
      element.removeEventListener('pointermove', move);
      element.removeEventListener('pointerleave', reset);
      element.removeEventListener('pointercancel', reset);
      reduced.removeEventListener('change', sync);
      pointer.removeEventListener('change', sync);
      document.removeEventListener('visibilitychange', sync);
    }
  };
}
