<script lang="ts">
 import type { Snippet } from 'svelte';
 import type { HTMLAttributes } from 'svelte/elements';
 import type { Depth, Texture } from '@tactile-ui/tokens';
 interface Props extends HTMLAttributes<HTMLDivElement> { depth?: Depth; texture?: Texture; children?: Snippet }
 let { depth='raised', texture='none', children, class:className, ...rest }: Props = $props();
</script>
<div {...rest} class={['tui-surface',className]} data-depth={depth} data-texture={texture}>{@render children?.()}</div>
