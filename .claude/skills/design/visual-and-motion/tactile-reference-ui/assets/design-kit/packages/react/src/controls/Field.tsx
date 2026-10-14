'use client';
import { useId } from 'react';
import type { InputHTMLAttributes } from 'react';
import { cx } from '@tactile-ui/tokens';

export interface FieldProps extends InputHTMLAttributes<HTMLInputElement> { label: string; hint?: string; error?: string }
export function Field({ label, hint, error, id, className, 'aria-describedby': describedBy, ...rest }: FieldProps) {
  const generated = useId(), inputId = id || generated;
  const descriptionId = inputId + '-description';
  return <label className="tui-field" htmlFor={inputId}>{label}
    <input {...rest} id={inputId} className={cx('tui-input', className)} aria-invalid={error ? true : undefined} aria-describedby={cx(describedBy, (hint || error) && descriptionId) || undefined}/>
    {(hint || error) && <span id={descriptionId} className={cx('tui-help', error && 'tui-error')}>{error || hint}</span>}
  </label>;
}
