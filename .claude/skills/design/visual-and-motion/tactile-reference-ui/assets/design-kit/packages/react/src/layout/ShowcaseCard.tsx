'use client';
import type { ReactNode } from 'react';
import { cx } from '@tactile-ui/tokens';
import type { ShowcaseTone } from '@tactile-ui/tokens';

export interface ShowcaseCardProps { title: string; description: string; art: ReactNode; tone?: ShowcaseTone; className?: string }
export function ShowcaseCard({ title, description, art, tone = 'meadow', className }: ShowcaseCardProps) {
  return <article className={cx('tui-showcase-card', className)} data-tone={tone}>
    <div className="tui-showcase-art">{art}</div><div className="tui-showcase-copy"><h3>{title}</h3><p>{description}</p></div>
  </article>;
}
