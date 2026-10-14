<script lang="ts">
 import type { Snippet } from 'svelte';
 import { cx,type MapNode } from '@tactile-ui/tokens';
 import Orb from './Orb.svelte';
 interface Props {nodes:MapNode[];title:string;detail?:string;center?:Snippet;class?:string}
 let {nodes,title,detail,center,class:className}:Props=$props();
 const midpoint=$derived(Math.ceil(nodes.length/2));
</script>
{#snippet side(items:MapNode[])}<ul class="tui-map-side">{#each items as node (node.id)}<li class="tui-map-node"><span class="tui-map-symbol" aria-hidden="true">{node.symbol || '↗'}</span><span><strong>{node.label}</strong>{#if node.detail}<small>{node.detail}</small>{/if}</span></li>{/each}</ul>{/snippet}
<section class={cx('tui-map',className)} aria-label={title}>
 <svg class="tui-map-connectors" viewBox="0 0 600 280" preserveAspectRatio="none" aria-hidden="true"><path d="M70 65H175Q195 65 195 85V120Q195 140 220 140H380Q405 140 405 120V85Q405 65 425 65H530M70 215H175Q195 215 195 195V160Q195 140 220 140M380 140Q405 140 405 160V195Q405 215 425 215H530" stroke="currentColor" stroke-width="1" fill="none"/></svg>
 {@render side(nodes.slice(0,midpoint))}<div class="tui-map-center">{#if center}{@render center()}{:else}<Orb appearance="accent">↔</Orb>{/if}<strong>{title}</strong>{#if detail}<small class="tui-caption">{detail}</small>{/if}</div>{@render side(nodes.slice(midpoint))}
</section>
