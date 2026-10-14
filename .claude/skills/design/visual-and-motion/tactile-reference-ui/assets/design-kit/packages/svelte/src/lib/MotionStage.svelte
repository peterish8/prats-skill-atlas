<script lang="ts">
  import { onMount, type Snippet } from 'svelte';
  import { cx, createMotionStage } from '@tactile-ui/tokens';
  interface Props { children: Snippet; paused?: boolean; intensity?: number; className?: string }
  let { children, paused = false, intensity = 0.6, className }: Props = $props();
  let element: HTMLDivElement | undefined;
  let controller = $state<ReturnType<typeof createMotionStage>>();

  onMount(() => {
    if (!element) return;
    const mounted = createMotionStage(element, { paused, intensity });
    controller = mounted;
    return () => { mounted.destroy(); };
  });
  $effect(() => { controller?.update({ paused, intensity }); });
</script>

<div bind:this={element} class={cx('tui-motion-stage', className)} data-paused={paused}>
  {@render children()}
</div>
