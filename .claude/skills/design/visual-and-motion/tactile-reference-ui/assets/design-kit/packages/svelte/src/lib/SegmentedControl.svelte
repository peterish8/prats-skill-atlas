<script lang="ts">
  import { cx } from '@tactile-ui/tokens';
  interface Props { label: string; value: string; options: { value: string; label: string; disabled?: boolean }[]; onValueChange: (value: string) => void; className?: string }
  const name = $props.id();
  let { label, value, options, onValueChange, className }: Props = $props();
</script>

<fieldset class={cx('tui-segmented', className)}>
  <legend class="tui-segmented-legend">{label}</legend>
  <div class="tui-segmented-options">{#each options as option (option.value)}<label class="tui-segmented-option"><input type="radio" {name} value={option.value} checked={value === option.value} disabled={option.disabled} onchange={event => { if (event.currentTarget.checked) onValueChange(option.value); }} /><span>{option.label}</span></label>{/each}</div>
</fieldset>
