'use client';
import type { HTMLAttributes } from 'react';
import { cx } from '@tactile-ui/tokens';
import type { Direction } from '@tactile-ui/tokens';

export interface ThemeProps extends HTMLAttributes<HTMLDivElement> { direction?: Direction }
export function Theme({ direction = 'porcelain', className, ...rest }: ThemeProps) {
  return <div {...rest} className={cx('tui-theme', className)} data-tui-direction={direction}/>;
}
