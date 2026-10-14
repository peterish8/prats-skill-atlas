<script lang="ts">
  import type { Snippet } from 'svelte';
  import type { HTMLAnchorAttributes } from 'svelte/elements';

  interface Props extends HTMLAnchorAttributes {
    href: string;
    variant?: 'primary' | 'secondary' | 'ghost';
    className?: string;
    children?: Snippet;
  }
  let { href, variant = 'primary', className, class: nativeClass, children, ...rest }: Props = $props();
</script>

<a {...rest} {href} class={['tui-button', 'tui-action-link', className, nativeClass]} data-variant={variant}>
  {@render children?.()}
</a>
