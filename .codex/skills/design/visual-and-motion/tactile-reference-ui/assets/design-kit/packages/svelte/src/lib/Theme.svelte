<script lang="ts">
 import type { Snippet } from 'svelte';
 import type { HTMLAttributes } from 'svelte/elements';
 import type { Direction } from '@tactile-ui/tokens';
 interface Props extends HTMLAttributes<HTMLDivElement> { direction?: Direction; children?: Snippet }
 let { direction='porcelain', children, class:className, ...rest }: Props = $props();
</script>
<div {...rest} class={['tui-theme',className]} data-tui-direction={direction}>{@render children?.()}</div>
