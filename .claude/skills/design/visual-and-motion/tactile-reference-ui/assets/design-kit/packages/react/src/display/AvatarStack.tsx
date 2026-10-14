'use client';
import { cx } from '@tactile-ui/tokens';

export interface AvatarItem { id: string; name: string; initials: string }
export interface AvatarStackProps { items: AvatarItem[]; max?: number; className?: string }
export function AvatarStack({ items, max = 4, className }: AvatarStackProps) {
  const limit = Number.isFinite(max) ? Math.max(1, Math.floor(max)) : 4;
  const shown = items.slice(0, limit), remaining = Math.max(0, items.length - shown.length);
  return <div className={cx('tui-avatar-stack', className)}><span className="tui-avatar-visuals" aria-hidden="true">{shown.map(item => <span className="tui-avatar" key={item.id}>{item.initials}</span>)}{remaining > 0 && <span className="tui-avatar-overflow">+{remaining}</span>}</span><ul className="tui-sr-only">{items.map(item => <li key={item.id}>{item.name}</li>)}</ul></div>;
}
