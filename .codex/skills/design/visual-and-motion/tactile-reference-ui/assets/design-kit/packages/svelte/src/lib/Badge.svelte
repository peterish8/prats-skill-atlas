<script lang="ts">
 import type { Snippet } from 'svelte';
 import type { HTMLAttributes } from 'svelte/elements';
 import type { Tone } from '@tactile-ui/tokens';
 interface Props extends HTMLAttributes<HTMLSpanElement> { tone?: Tone; children?: Snippet }
 let { tone='neutral', children, class:className, ...rest }: Props = $props();
</script>
<span {...rest} class={['tui-badge',className]} data-tone={tone}><span class="tui-badge-dot" aria-hidden="true"></span>{@render children?.()}</span>
