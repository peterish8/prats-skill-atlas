<script lang="ts">
 import type { Snippet } from 'svelte';
 import type { HTMLAttributes } from 'svelte/elements';
 import type { Depth, Texture } from '@tactile-ui/tokens';
 import Surface from './Surface.svelte';
 interface Props extends Omit<HTMLAttributes<HTMLDivElement>,'title'> {title:string;description:string;art?:Snippet;footer?:Snippet;depth?:Depth;texture?:Texture}
 let {title,description,art,footer,class:className,...rest}:Props=$props();
</script>
<Surface {...rest} class={['tui-feature',className]}><div class="tui-feature-art">{@render art?.()}</div><div class="tui-feature-copy"><h3 class="tui-heading">{title}</h3><p class="tui-caption">{description}</p>{@render footer?.()}</div></Surface>
