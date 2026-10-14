<script lang="ts">
 import { cx,sparklinePoints } from '@tactile-ui/tokens';
 interface Props {values:number[];label:string;class?:string}
 const id=$props.id();
 let {values,label,class:className}:Props=$props();
 const points=$derived(sparklinePoints(values));
</script>
<svg class={cx('tui-sparkline',className)} viewBox="0 0 320 100" role="img" aria-labelledby={id}><title {id}>{label}</title><path d="M8 92H312" fill="none" stroke="currentColor" opacity=".12"/>{#if points}<polyline {points} fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>{:else}<text x="8" y="50" fill="currentColor" font-size="14">No chart data</text>{/if}</svg>
