<script lang="ts">
  import type { Snippet } from 'svelte';
  import { cx, type ShowcaseTone } from '@tactile-ui/tokens';
  interface Props { title: string; description: string; art: Snippet; tone?: ShowcaseTone; className?: string }
  let { title, description, art, tone = 'blue', className }: Props = $props();
</script>

<article class={cx('tui-showcase-card', className)} data-tone={tone}>
  <div class="tui-showcase-art">{@render art()}</div>
  <div class="tui-showcase-copy"><h3>{title}</h3><p>{description}</p></div>
</article>
