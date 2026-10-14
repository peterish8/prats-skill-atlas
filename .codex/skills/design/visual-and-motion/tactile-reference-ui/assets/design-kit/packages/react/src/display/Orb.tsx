'use client';
import type { HTMLAttributes } from 'react';
import { cx } from '@tactile-ui/tokens';

export interface OrbProps extends HTMLAttributes<HTMLSpanElement> { appearance?: 'neutral' | 'accent' | 'iridescent' }
/** Decorative by default. Put the meaningful name in adjacent visible content. */
export function Orb({ appearance = 'neutral', className, ...rest }: OrbProps) {
  return <span aria-hidden="true" {...rest} className={cx('tui-orb', className)} data-appearance={appearance}/>;
}
