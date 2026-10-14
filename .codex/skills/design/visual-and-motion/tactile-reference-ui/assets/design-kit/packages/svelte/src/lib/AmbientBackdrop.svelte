<script lang="ts">
  import { cx, type Atmosphere } from '@tactile-ui/tokens';
  interface Props { kind: Atmosphere; animated?: boolean; className?: string }
  let { kind, animated = false, className }: Props = $props();
</script>

<div class={cx('tui-atmosphere', className)} data-kind={kind} data-animated={animated} aria-hidden="true">
  <span class="tui-atmosphere-layer"></span>
  <span class="tui-atmosphere-layer"></span>
  <span class="tui-atmosphere-layer"></span>
</div>
