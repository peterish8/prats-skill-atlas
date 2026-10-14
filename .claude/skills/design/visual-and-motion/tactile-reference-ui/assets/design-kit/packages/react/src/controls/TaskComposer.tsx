'use client';
import { useId, useRef } from 'react';
import type { FormEvent } from 'react';
import { cx } from '@tactile-ui/tokens';
import { Button } from '../controls/Button';

export interface TaskComposerProps {
  label: string;
  value: string;
  onValueChange: (value: string) => void;
  onSubmit: (value: string) => void;
  submitLabel?: string;
  placeholder?: string;
  hint?: string;
  error?: string;
  loading?: boolean;
  disabled?: boolean;
  maxLength?: number;
  className?: string;
}
export function TaskComposer({ label, value, onValueChange, onSubmit, submitLabel = 'Create outline', placeholder, hint, error, loading = false, disabled = false, maxLength = 1000, className }: TaskComposerProps) {
  const id = useId(), submitting = useRef(false);
  const limit = Number.isFinite(maxLength) ? Math.max(1, Math.floor(maxLength)) : 1000;
  const blocked = disabled || loading;
  const valid = value.trim().length > 0 && value.length <= limit;
  function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (blocked || !valid || submitting.current) return;
    submitting.current = true;
    try { onSubmit(value.trim()); }
    finally { queueMicrotask(() => { submitting.current = false; }); }
  }
  return <form className={cx('tui-composer', className)} onSubmit={submit} aria-busy={loading || undefined}>
    <label className="tui-composer-label" htmlFor={id}>{label}</label>
    <div className="tui-composer-row"><input id={id} className="tui-composer-input" type="text" value={value} placeholder={placeholder} maxLength={limit} required disabled={blocked} autoComplete="off" onChange={event => onValueChange(event.target.value)} aria-invalid={error ? true : undefined} aria-describedby={cx(hint && id + '-hint', error && id + '-error') || undefined}/>
      <Button type="submit" loading={loading} disabled={blocked || !valid}>{submitLabel}</Button></div>
    {hint && <p className="tui-composer-help" id={id + '-hint'}>{hint}</p>}{error && <p className="tui-composer-error" id={id + '-error'}>{error}</p>}
  </form>;
}
