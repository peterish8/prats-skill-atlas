<script lang="ts">
  import { cx } from '@tactile-ui/tokens';
  interface Props { eyebrow?: string; title: string; description?: string; align?: 'start' | 'center'; className?: string }
  let { eyebrow, title, description, align = 'start', className }: Props = $props();
</script>

<div class={cx('tui-section-heading', className)} data-align={align}>
  {#if eyebrow}<p class="tui-hero-eyebrow">{eyebrow}</p>{/if}
  <h2>{title}</h2>
  {#if description}<p>{description}</p>{/if}
</div>
