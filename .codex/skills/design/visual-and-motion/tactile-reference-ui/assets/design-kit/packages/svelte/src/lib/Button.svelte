<script lang="ts">
 import type { Snippet } from 'svelte';
 import type { HTMLButtonAttributes } from 'svelte/elements';
 import type { ButtonVariant } from '@tactile-ui/tokens';
 interface Props extends HTMLButtonAttributes { variant?: ButtonVariant; loading?: boolean; children?: Snippet }
 let { variant='primary', loading=false, disabled=false, children, type='button', class:className, ...rest }: Props = $props();
</script>
<button {...rest} {type} disabled={disabled || loading} aria-busy={loading || undefined} class={['tui-button',className]} data-variant={variant}>
 {#if loading}<span class="tui-spinner" aria-hidden="true"></span>{/if}{@render children?.()}
</button>
