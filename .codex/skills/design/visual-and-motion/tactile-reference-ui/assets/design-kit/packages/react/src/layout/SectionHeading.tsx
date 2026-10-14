'use client';
import { cx } from '@tactile-ui/tokens';

export interface SectionHeadingProps { eyebrow?: string; title: string; description?: string; align?: 'start' | 'center'; className?: string }
export function SectionHeading({ eyebrow, title, description, align = 'start', className }: SectionHeadingProps) {
  return <div className={cx('tui-section-heading', className)} data-align={align}>{eyebrow && <p className="tui-hero-eyebrow">{eyebrow}</p>}
    <h2>{title}</h2>{description && <p>{description}</p>}
  </div>;
}
