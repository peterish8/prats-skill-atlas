<script lang="ts">
  import { onMount, type Snippet } from 'svelte';
  import { cx, motion } from '@tactile-ui/tokens';

  interface Props { children: Snippet; className?: string; delay?: number }
  let { children, className, delay = 0 }: Props = $props();
  let element: HTMLDivElement | undefined;
  let revealed = $state(true);
  const safeDelay = $derived(Number.isFinite(delay) ? Math.min(motion.maxStagger, Math.max(0, delay)) : 0);

  onMount(() => {
    const node = element;
    if (!node || typeof IntersectionObserver === 'undefined') return;
    const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
    let observer: IntersectionObserver | undefined;
    function show() { revealed = true; observer?.disconnect(); }
    function observe() {
      observer?.disconnect();
      if (preference.matches || !node || node.getBoundingClientRect().top < window.innerHeight) { show(); return; }
      revealed = false;
      observer = new IntersectionObserver(entries => { if (entries.some(entry => entry.isIntersecting)) show(); }, { threshold: 0.08 });
      observer.observe(node);
    }
    observe();
    preference.addEventListener('change', observe);
    node.addEventListener('focusin', show);
    return () => { observer?.disconnect(); preference.removeEventListener('change', observe); node.removeEventListener('focusin', show); };
  });
</script>

<div bind:this={element} class={cx('tui-reveal', className)} data-revealed={revealed} style:--tui-reveal-delay={`${safeDelay}ms`}>
  {@render children()}
</div>
