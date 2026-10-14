'use client';
import type { HTMLAttributes } from 'react';
import { cx } from '@tactile-ui/tokens';
import type { Tone } from '@tactile-ui/tokens';

export interface BadgeProps extends HTMLAttributes<HTMLSpanElement> { tone?: Tone }
export function Badge({ tone = 'neutral', className, children, ...rest }: BadgeProps) {
  return <span {...rest} className={cx('tui-badge', className)} data-tone={tone}><span className="tui-badge-dot" aria-hidden="true"/>{children}</span>;
}
