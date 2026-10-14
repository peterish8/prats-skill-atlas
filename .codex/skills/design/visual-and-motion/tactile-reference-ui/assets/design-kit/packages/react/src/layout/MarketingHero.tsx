'use client';
import type { ReactNode } from 'react';
import { cx } from '@tactile-ui/tokens';

export interface MarketingHeroProps {
  eyebrow?: string;
  title: string;
  description: string;
  align?: 'center' | 'split';
  art?: ReactNode;
  children?: ReactNode;
  className?: string;
}
/** Use once per page: this component owns the page's h1. */
export function MarketingHero({ eyebrow, title, description, align = 'center', art, children, className }: MarketingHeroProps) {
  return <section className={cx('tui-marketing-hero', className)} data-align={align}>
    <div className="tui-hero-copy">{eyebrow && <p className="tui-hero-eyebrow">{eyebrow}</p>}<h1 className="tui-hero-title">{title}</h1>
      <p className="tui-hero-description">{description}</p>{children && <div className="tui-hero-actions">{children}</div>}</div>
    {art && <div className="tui-hero-art">{art}</div>}
  </section>;
}
