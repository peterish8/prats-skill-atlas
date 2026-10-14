<script lang="ts">
  import type { Snippet } from 'svelte';
  import { cx, type Tone } from '@tactile-ui/tokens';
  interface Props { title: string; tone?: Tone; children: Snippet; className?: string }
  const id = $props.id();
  let { title, tone = 'neutral', children, className }: Props = $props();
</script>

<aside class={cx('tui-notice', className)} data-tone={tone} aria-labelledby={id}>
  <h3 {id} class="tui-notice-title">{title}</h3>{@render children()}
</aside>
