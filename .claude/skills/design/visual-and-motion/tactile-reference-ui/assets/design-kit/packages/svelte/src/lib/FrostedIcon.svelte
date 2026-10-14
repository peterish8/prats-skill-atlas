<script lang="ts">
  import { cx } from '@tactile-ui/tokens';
  let { className }: { className?: string } = $props();
</script>

<span class={cx('tui-frosted-icon', className)} aria-hidden="true">
  <span class="tui-frosted-back"></span>
  <span class="tui-frosted-front"><span class="tui-frosted-bar"></span><span class="tui-frosted-bar"></span><span class="tui-frosted-bar"></span></span>
</span>
