<script lang="ts">
 import type { Snippet } from 'svelte';
 interface TabItem { id:string; label:string; content:Snippet }
 interface Props { items:TabItem[]; value?:string; onValueChange?:(value:string)=>void; label:string; class?:string }
 const base=$props.id();
 let { items, value=$bindable(''), onValueChange, label, class:className }: Props=$props();
 let list:HTMLDivElement|undefined=$state();
 const selected=$derived(items.some(t=>t.id===value)?value:items[0]?.id);
 function select(id:string){value=id;onValueChange?.(id)}
 function move(event:KeyboardEvent,index:number){
  let next=index;
  if(event.key==='ArrowRight') next=(index+1)%items.length;
  else if(event.key==='ArrowLeft') next=(index-1+items.length)%items.length;
  else if(event.key==='Home') next=0;
  else if(event.key==='End') next=items.length-1;
  else return;
  event.preventDefault();select(items[next].id);list?.querySelectorAll<HTMLButtonElement>('[role=tab]')[next]?.focus();
 }
</script>
<div class={className}><div class="tui-tabs-list" role="tablist" aria-label={label} bind:this={list}>
 {#each items as item,index (item.id)}<button type="button" class="tui-tab" role="tab" id={base+'-tab-'+item.id} aria-controls={base+'-panel-'+item.id} aria-selected={selected===item.id} tabindex={selected===item.id?0:-1} onclick={()=>select(item.id)} onkeydown={e=>move(e,index)}>{item.label}</button>{/each}
</div>
{#each items as item (item.id)}<div class="tui-tab-panel" role="tabpanel" tabindex="0" id={base+'-panel-'+item.id} aria-labelledby={base+'-tab-'+item.id} hidden={selected!==item.id}>{@render item.content()}</div>{/each}</div>
