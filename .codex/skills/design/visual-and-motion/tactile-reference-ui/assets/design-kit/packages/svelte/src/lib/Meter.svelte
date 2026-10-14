<script lang="ts">
 interface Props {label:string;value:number;max:number;valueText:string}
 let {label,value,max,valueText}:Props=$props();
 const safeMax=$derived(Number.isFinite(max)&&max>0?max:1);
 const safeValue=$derived(Number.isFinite(value)?Math.min(safeMax,Math.max(0,value)):0);
</script>
<div class="tui-meter"><div class="tui-meter-label"><span>{label}</span><span>{valueText}</span></div><div class="tui-meter-track" role="meter" aria-label={label} aria-valuemin="0" aria-valuemax={safeMax} aria-valuenow={safeValue} aria-valuetext={valueText}><div class="tui-meter-fill" style:width={String(100*safeValue/safeMax)+'%'}></div></div></div>
