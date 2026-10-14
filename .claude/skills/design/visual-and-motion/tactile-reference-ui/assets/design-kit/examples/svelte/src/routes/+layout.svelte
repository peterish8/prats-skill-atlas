<script lang="ts">
  import type { Snippet } from 'svelte';
  import '@tactile-ui/tokens/styles.css';
  import '../../../gallery.css';
  import './gallery.css';
  let { children }: { children: Snippet } = $props();
</script>

{@render children()}
