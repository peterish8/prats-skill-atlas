<script lang="ts">
  import type { Snippet } from 'svelte';
  import { cx } from '@tactile-ui/tokens';
  interface Props { items: { id: string; title: string; content: Snippet }[]; label?: string; className?: string }
  let { items, label = 'More details', className }: Props = $props();
</script>

<section class={cx('tui-accordion', className)} aria-label={label}>
  {#each items as item (item.id)}<details class="tui-accordion-item"><summary class="tui-accordion-summary">{item.title}</summary><div class="tui-accordion-content">{@render item.content()}</div></details>{/each}
</section>
