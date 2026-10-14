<script lang="ts">
 import type {Snippet} from 'svelte';
 import {cx} from '@tactile-ui/tokens';
 interface Props {title:string;description:string;palette?:'blue'|'violet'|'ice';symbol?:Snippet;class?:string}
 let {title,description,palette='blue',symbol,class:className}:Props=$props();
</script>
<article class={cx('tui-poster',className)} data-palette={palette}><span class="tui-poster-symbol" aria-hidden="true">{#if symbol}{@render symbol()}{:else}✳{/if}</span><h3>{title}</h3><p>{description}</p></article>
