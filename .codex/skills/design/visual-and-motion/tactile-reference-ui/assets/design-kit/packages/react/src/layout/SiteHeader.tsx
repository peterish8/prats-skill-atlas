'use client';
import { useRef } from 'react';
import { cx } from '@tactile-ui/tokens';
import type { NavigationItem, ActionItem } from '@tactile-ui/tokens';
import { ActionLink } from '../controls/ActionLink';

export interface SiteHeaderProps {
  brand: string;
  homeHref: string;
  items: NavigationItem[];
  action?: ActionItem;
  className?: string;
}
export function SiteHeader({ brand, homeHref, items, action, className }: SiteHeaderProps) {
  const menu = useRef<HTMLDetailsElement>(null);
  const closeMenu = () => { if (menu.current) menu.current.open = false; };
  return <header className={cx('tui-site-header', className)}>
    <a className="tui-site-brand" href={homeHref}>{brand}</a>
    <nav className="tui-site-nav" aria-label="Primary">{items.map(item => <a key={item.href + item.label} href={item.href}>{item.label}</a>)}</nav>
    {action && <ActionLink href={action.href} label={action.label} className="tui-site-action"/>}
    {(items.length > 0 || action) && <details className="tui-mobile-menu" ref={menu}>
      <summary>Menu<span className="tui-menu-icon" aria-hidden="true"/></summary>
      <nav className="tui-mobile-links" aria-label="Mobile primary">{items.map(item => <a key={item.href + item.label} href={item.href} onClick={closeMenu}>{item.label}</a>)}
        {action && <ActionLink href={action.href} label={action.label} onClick={closeMenu}/>}</nav>
    </details>}
  </header>;
}
