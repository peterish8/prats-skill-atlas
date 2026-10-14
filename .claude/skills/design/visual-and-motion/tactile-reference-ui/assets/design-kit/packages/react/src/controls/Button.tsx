'use client';
import type { ButtonHTMLAttributes } from 'react';
import { cx } from '@tactile-ui/tokens';
import type { ButtonVariant } from '@tactile-ui/tokens';

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> { variant?: ButtonVariant; loading?: boolean }
export function Button({ variant = 'primary', loading = false, disabled, className, children, type = 'button', ...rest }: ButtonProps) {
  return <button {...rest} type={type} disabled={disabled || loading} aria-busy={loading || undefined} className={cx('tui-button', className)} data-variant={variant}>
    {loading && <span className="tui-spinner" aria-hidden="true"/>}{children}
  </button>;
}
