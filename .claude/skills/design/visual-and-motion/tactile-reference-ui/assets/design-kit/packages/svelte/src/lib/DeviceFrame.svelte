<script lang="ts">
  import type { Snippet } from 'svelte';
  import { cx } from '@tactile-ui/tokens';
  interface Props { label: string; variant?: 'desktop' | 'phone'; children: Snippet; className?: string }
  let { label, variant = 'desktop', children, className }: Props = $props();
</script>

<figure class={cx('tui-device-frame', className)} data-variant={variant}>
  <div class="tui-device-chrome" aria-hidden="true"><span></span><span></span><span></span></div>
  <div class="tui-device-content">{@render children()}</div>
  <figcaption class="tui-device-caption">{label}</figcaption>
</figure>
