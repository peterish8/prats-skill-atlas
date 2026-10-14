<script lang="ts">
 import type { HTMLButtonAttributes } from 'svelte/elements';
 interface Props extends Omit<HTMLButtonAttributes,'onclick'|'role'|'aria-checked'> { checked?:boolean; onCheckedChange?:(value:boolean)=>void; label:string }
 let { checked=$bindable(false), onCheckedChange, label, class:className, ...rest }: Props = $props();
 function toggle(){checked=!checked;onCheckedChange?.(checked)}
</script>
<button {...rest} type="button" role="switch" aria-checked={checked} class={['tui-switch',className]} onclick={toggle}>
 <span class="tui-switch-track" aria-hidden="true"><span class="tui-switch-thumb"></span></span><span>{label}</span>
</button>
