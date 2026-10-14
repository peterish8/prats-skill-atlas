<script lang="ts">
 import type { Snippet } from 'svelte';
 interface Props {open?:boolean;onOpenChange?:(open:boolean)=>void;title:string;children:Snippet}
 const id=$props.id();
 let {open=$bindable(false),onOpenChange,title,children}:Props=$props();
 let dialog:HTMLDialogElement|undefined=$state();
 let opener:HTMLElement|null=null;
 $effect(()=>{if(open && dialog && !dialog.open){opener=document.activeElement as HTMLElement;dialog.showModal()}else if(!open && dialog?.open)dialog.close()});
 function closed(){open=false;onOpenChange?.(false);opener?.focus()}
</script>
<dialog bind:this={dialog} class="tui-dialog" aria-labelledby={id} onclose={closed}><div class="tui-dialog-header"><h2 {id} class="tui-heading">{title}</h2><button type="button" class="tui-dialog-close" aria-label="Close dialog" onclick={()=>dialog?.close()}>×</button></div>{@render children()}</dialog>
