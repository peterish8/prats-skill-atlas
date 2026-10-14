'use client';
import { cx } from '@tactile-ui/tokens';

export interface SkeletonProps { className?: string; lines?: number }
export function Skeleton({ className, lines = 3 }: SkeletonProps) {
  const count = Number.isFinite(lines) ? Math.min(12, Math.max(1, Math.floor(lines))) : 3;
  return <div className={cx('tui-skeleton', className)} aria-hidden="true">{Array.from({ length: count }, (_, index) => <span className="tui-skeleton-line" key={index}/>)}</div>;
}
