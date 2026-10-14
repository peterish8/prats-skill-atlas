'use client';
import type { ReactNode } from 'react';
import { cx } from '@tactile-ui/tokens';

export interface AccordionItem { id: string; title: string; content: ReactNode }
export interface AccordionProps { items: AccordionItem[]; label?: string; className?: string }
export function Accordion({ items, label, className }: AccordionProps) {
  return <section className={cx('tui-accordion', className)} aria-label={label}>{items.map(item => <details className="tui-accordion-item" key={item.id}><summary className="tui-accordion-summary">{item.title}</summary><div className="tui-accordion-content">{item.content}</div></details>)}</section>;
}
