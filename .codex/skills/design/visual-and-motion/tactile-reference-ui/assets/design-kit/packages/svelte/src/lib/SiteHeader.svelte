<script lang="ts">
  import { cx, type ActionItem, type NavigationItem } from '@tactile-ui/tokens';
  import ActionLink from './ActionLink.svelte';

  interface Props { brand: string; homeHref: string; items: NavigationItem[]; action?: ActionItem; className?: string }
  let { brand, homeHref, items, action, className }: Props = $props();
  let menu: HTMLDetailsElement | undefined;
  function closeMenu() { if (menu) menu.open = false; }
</script>

<header class={cx('tui-site-header', className)}>
  <a class="tui-site-brand" href={homeHref}>{brand}</a>
  <nav class="tui-site-nav" aria-label="Primary navigation">
    {#each items as item, index (`${item.href}-${index}`)}<a href={item.href}>{item.label}</a>{/each}
  </nav>
  {#if action}<ActionLink href={action.href} className="tui-site-action">{action.label}</ActionLink>{/if}
  <details class="tui-mobile-menu" bind:this={menu}>
    <summary>Menu <span class="tui-menu-icon" aria-hidden="true"></span></summary>
    <nav class="tui-mobile-links" aria-label="Mobile navigation">
      {#each items as item, index (`${item.href}-${index}`)}<a href={item.href} onclick={closeMenu}>{item.label}</a>{/each}
      {#if action}<a href={action.href} onclick={closeMenu}>{action.label}</a>{/if}
    </nav>
  </details>
</header>

