<script lang="ts">
  import { cx } from '@tactile-ui/tokens';
  interface Props { kind: 'orb' | 'coin' | 'sun' | 'certificate'; className?: string }
  let { kind, className }: Props = $props();
</script>

<span class={cx('tui-material-object', className)} data-kind={kind} aria-hidden="true">
  <span class="tui-material-core"></span><span class="tui-material-ring"></span><span class="tui-material-glint"></span>
</span>
