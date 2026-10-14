<script lang="ts">
 import type { Snippet } from 'svelte';
 import type { HTMLAttributes } from 'svelte/elements';
 import type { Depth,Texture } from '@tactile-ui/tokens';
 import Surface from './Surface.svelte';
 interface Props extends HTMLAttributes<HTMLDivElement> {label:string;value:string;detail?:string;note?:string;depth?:Depth;texture?:Texture;children?:Snippet}
 let {label,value,detail,note,children,...rest}:Props=$props();
</script>
<Surface {...rest}><p class="tui-metric-label">{label}</p><div class="tui-metric-value">{value}</div>{#if detail}<p class="tui-caption">{detail}</p>{/if}{@render children?.()}{#if note}<p class="tui-metric-note">{note}</p>{/if}</Surface>
