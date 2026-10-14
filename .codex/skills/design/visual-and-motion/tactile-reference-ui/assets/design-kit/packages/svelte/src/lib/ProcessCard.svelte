<script lang="ts">
  import { cx } from '@tactile-ui/tokens';
  interface Props { title: string; description: string; step?: string; mark: 'scatter' | 'align' | 'transfer'; className?: string }
  let { title, description, step, mark, className }: Props = $props();
  const paths = {
    scatter: 'M22 30 62 62M75 20 70 57M150 25 109 59M170 90 110 84M35 112 72 90M88 125 95 91',
    align: 'M36 25H94M68 43H143M22 61H110M88 79H174M48 97H124M70 115H154',
    transfer: 'm40 24 20 30-20 30 20 30m36-90 20 30-20 30 20 30m36-90 20 30-20 30 20 30'
  };
</script>

<article class={cx('tui-process-card', className)}>
  <svg class="tui-process-mark" viewBox="0 0 200 140" aria-hidden="true"><path d={paths[mark]} fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" /></svg>
  {#if step}<span class="tui-process-step">{step}</span>{/if}
  <h3>{title}</h3><p>{description}</p>
</article>
