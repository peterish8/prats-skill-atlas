<script lang="ts">
  import type { Snippet } from 'svelte';
  import { cx } from '@tactile-ui/tokens';
  interface Props { title: string; description: string; art?: Snippet; children?: Snippet; className?: string }
  let { title, description, art, children, className }: Props = $props();
</script>

<div class={cx('tui-empty-state', className)}>
  {#if art}<div class="tui-empty-art">{@render art()}</div>{/if}
  <h3>{title}</h3><p>{description}</p>
  {#if children}<div class="tui-empty-actions">{@render children()}</div>{/if}
</div>
