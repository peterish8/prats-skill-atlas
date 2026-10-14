<script lang="ts">
 import type { Snippet } from 'svelte';
 import type { HTMLAttributes } from 'svelte/elements';
 interface Props extends HTMLAttributes<HTMLSpanElement> {appearance?:'neutral'|'accent'|'iridescent';children?:Snippet}
 let {appearance='neutral',children,class:className,...rest}:Props=$props();
</script>
<span aria-hidden="true" {...rest} class={['tui-orb',className]} data-appearance={appearance}>{@render children?.()}</span>
