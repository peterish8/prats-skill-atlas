<script lang="ts">
 import type {Snippet} from 'svelte';
 import FeatureCard from './FeatureCard.svelte';
 import Button from './Button.svelte';
 interface Props {title:string;description:string;art?:Snippet;step:number;steps:number;onContinue:()=>void;continueLabel?:string}
 let {title,description,art,step,steps,onContinue,continueLabel='Continue'}:Props=$props();
 const count=$derived(Math.max(1,Math.floor(steps))),current=$derived(Math.min(count,Math.max(1,Math.floor(step))));
</script>
<FeatureCard {title} {description} {art}>{#snippet footer()}<div class="tui-onboarding-footer"><Button onclick={onContinue}>{continueLabel}</Button><span class="tui-steps" aria-label={'Step '+current+' of '+count}>{#each Array.from({length:count}) as _,i}<span data-current={i===current-1} aria-hidden="true"></span>{/each}</span></div>{/snippet}</FeatureCard>
