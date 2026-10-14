'use client';
import type { AnchorHTMLAttributes } from 'react';
import { cx } from '@tactile-ui/tokens';

export interface ActionLinkProps extends AnchorHTMLAttributes<HTMLAnchorElement> {
  href: string;
  variant?: 'primary' | 'secondary' | 'ghost';
  label?: string;
}
/** Navigation remains an anchor, including in a client-side router. */
export function ActionLink({ href, variant = 'primary', label, children, className, ...rest }: ActionLinkProps) {
  return <a {...rest} href={href} className={cx('tui-button', 'tui-action-link', className)} data-variant={variant}>{children ?? label}</a>;
}
