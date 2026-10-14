<script lang="ts">
 import type { HTMLInputAttributes } from 'svelte/elements';
 import { cx } from '@tactile-ui/tokens';
 interface Props extends Omit<HTMLInputAttributes,'value'> { label:string; hint?:string; error?:string; value?:string }
 const generated=$props.id();
 let { label, hint, error, id=generated, value=$bindable(''), class:className, 'aria-describedby':describedBy, ...rest }: Props = $props();
</script>
<label class="tui-field" for={id}>{label}
 <input {...rest} {id} bind:value class={['tui-input',className]} aria-invalid={error ? true : undefined} aria-describedby={cx(describedBy,(hint || error) && id+'-description') || undefined}/>
 {#if hint || error}<span id={id+'-description'} class={cx('tui-help',error && 'tui-error')}>{error || hint}</span>{/if}
</label>
