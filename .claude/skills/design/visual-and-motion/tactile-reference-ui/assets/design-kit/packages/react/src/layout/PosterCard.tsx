'use client';
import type { ReactNode } from 'react';
import { cx } from '@tactile-ui/tokens';

export interface PosterCardProps { title: string; description: string; palette?: 'blue' | 'violet' | 'ice'; symbol?: ReactNode; className?: string }
export function PosterCard({ title, description, palette='blue', symbol='✳', className }: PosterCardProps) {
  return <article className={cx('tui-poster',className)} data-palette={palette}><span className="tui-poster-symbol" aria-hidden="true">{symbol}</span><h3>{title}</h3><p>{description}</p></article>;
}
