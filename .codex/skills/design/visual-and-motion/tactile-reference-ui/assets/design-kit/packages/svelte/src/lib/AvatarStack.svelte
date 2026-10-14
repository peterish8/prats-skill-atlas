<script lang="ts">
  import { cx } from '@tactile-ui/tokens';
  interface Props { items: { id: string; name: string; initials: string }[]; max?: number; className?: string }
  let { items, max = 4, className }: Props = $props();
  const limit = $derived(Number.isFinite(max) ? Math.max(1, Math.floor(max)) : 4);
  const visible = $derived(items.slice(0, limit));
  const remaining = $derived(items.slice(limit));
</script>

<ul class={cx('tui-avatar-stack', className)} aria-label="Contributors">
  {#each visible as item (item.id)}<li><span class="tui-avatar" aria-hidden="true">{item.initials}</span><span class="tui-sr-only">{item.name}</span></li>{/each}
  {#if remaining.length}<li><span class="tui-avatar-overflow" aria-hidden="true">+{remaining.length}</span><span class="tui-sr-only">{remaining.map(item => item.name).join(', ')}</span></li>{/if}
</ul>
