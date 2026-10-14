'use client';
import type { ButtonHTMLAttributes } from 'react';
import { cx } from '@tactile-ui/tokens';

export interface SwitchProps extends Omit<ButtonHTMLAttributes<HTMLButtonElement>, 'onChange' | 'onClick' | 'role' | 'aria-checked'> {
  checked: boolean; onCheckedChange: (value: boolean) => void; label: string;
}
export function Switch({ checked, onCheckedChange, label, className, ...rest }: SwitchProps) {
  return <button {...rest} type="button" role="switch" aria-checked={checked} className={cx('tui-switch', className)} onClick={() => onCheckedChange(!checked)}>
    <span className="tui-switch-track" aria-hidden="true"><span className="tui-switch-thumb"/></span><span>{label}</span>
  </button>;
}
