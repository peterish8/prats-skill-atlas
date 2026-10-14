'use client';
import type { ReactNode } from 'react';
import { cx } from '@tactile-ui/tokens';

export interface EmptyStateProps { title: string; description: string; art?: ReactNode; children?: ReactNode; className?: string }
export function EmptyState({ title, description, art, children, className }: EmptyStateProps) {
  return <div className={cx('tui-empty-state', className)}>{art && <div className="tui-empty-art">{art}</div>}<h3>{title}</h3><p>{description}</p>{children && <div className="tui-empty-actions">{children}</div>}</div>;
}
