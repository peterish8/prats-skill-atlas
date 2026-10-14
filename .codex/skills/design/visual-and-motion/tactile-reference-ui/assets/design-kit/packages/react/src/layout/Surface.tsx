'use client';
import type { HTMLAttributes } from 'react';
import { cx } from '@tactile-ui/tokens';
import type { Depth, Texture } from '@tactile-ui/tokens';

export interface SurfaceProps extends HTMLAttributes<HTMLDivElement> { depth?: Depth; texture?: Texture }
export function Surface({ depth = 'raised', texture = 'none', className, ...rest }: SurfaceProps) {
  return <div {...rest} className={cx('tui-surface', className)} data-depth={depth} data-texture={texture}/>;
}
