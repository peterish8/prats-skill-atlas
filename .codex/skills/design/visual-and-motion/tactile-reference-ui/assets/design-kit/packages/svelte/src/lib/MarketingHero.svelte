<script lang="ts">
  import type { Snippet } from 'svelte';
  import { cx } from '@tactile-ui/tokens';
  interface Props { eyebrow?: string; title: string; description: string; align?: 'center' | 'split'; art?: Snippet; children?: Snippet; className?: string }
  const titleId = $props.id();
  let { eyebrow, title, description, align = 'center', art, children, className }: Props = $props();
</script>

<section class={cx('tui-marketing-hero', className)} data-align={align} aria-labelledby={titleId}>
  <div class="tui-hero-copy">
    {#if eyebrow}<p class="tui-hero-eyebrow">{eyebrow}</p>{/if}
    <h1 id={titleId} class="tui-hero-title">{title}</h1>
    <p class="tui-hero-description">{description}</p>
    {#if children}<div class="tui-hero-actions">{@render children()}</div>{/if}
  </div>
  {#if art}<div class="tui-hero-art">{@render art()}</div>{/if}
</section>
