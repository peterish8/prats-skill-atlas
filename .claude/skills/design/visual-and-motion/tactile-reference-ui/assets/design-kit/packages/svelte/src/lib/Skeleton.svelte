<script lang="ts">
  import { cx } from '@tactile-ui/tokens';
  interface Props { className?: string; lines?: number }
  let { className, lines = 3 }: Props = $props();
  const count = $derived(Number.isFinite(lines) ? Math.min(12, Math.max(1, Math.floor(lines))) : 3);
</script>

<div class={cx('tui-skeleton', className)} aria-hidden="true">{#each Array.from({ length: count }) as _, index (index)}<span class="tui-skeleton-line"></span>{/each}</div>
