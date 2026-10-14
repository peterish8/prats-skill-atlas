<script lang="ts">
  import { cx } from '@tactile-ui/tokens';
  interface Props {
    label: string; value: string; onValueChange: (value: string) => void; onSubmit: (value: string) => void;
    submitLabel?: string; placeholder?: string; hint?: string; error?: string;
    loading?: boolean; disabled?: boolean; maxLength?: number; className?: string;
  }
  const id = $props.id();
  let { label, value, onValueChange, onSubmit, submitLabel = 'Create outline', placeholder, hint, error,
    loading = false, disabled = false, maxLength = 1000, className }: Props = $props();
  const safeLimit = $derived(Number.isFinite(maxLength) ? Math.max(1, Math.floor(maxLength)) : 1000);
  let submitting = false;
  function submit(event: SubmitEvent) {
    event.preventDefault();
    const task = value.trim();
    if (disabled || loading || submitting || !task || value.length > safeLimit) return;
    submitting = true;
    try { onSubmit(task); } finally { queueMicrotask(() => { submitting = false; }); }
  }
</script>

<form class={cx('tui-composer', className)} onsubmit={submit} aria-busy={loading || undefined}>
  <label class="tui-composer-label" for={id}>{label}</label>
  <div class="tui-composer-row">
    <input class="tui-composer-input" {id} type="text" {value} {placeholder} maxlength={safeLimit}
      disabled={disabled || loading} required aria-invalid={error ? true : undefined}
      aria-describedby={hint || error ? `${id}-help` : undefined}
      oninput={event => onValueChange(event.currentTarget.value)} />
    <button class="tui-button" data-variant="primary" type="submit" disabled={disabled || loading || !value.trim() || value.length > safeLimit} aria-busy={loading || undefined}>
      {#if loading}<span class="tui-spinner" aria-hidden="true"></span>{/if}{submitLabel}
    </button>
  </div>
  {#if error || hint}<p id={`${id}-help`} class={cx('tui-composer-help', error && 'tui-composer-error')}>{error || hint}</p>{/if}
</form>
