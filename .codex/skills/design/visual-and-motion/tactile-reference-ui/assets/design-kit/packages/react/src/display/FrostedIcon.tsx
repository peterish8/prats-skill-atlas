'use client';
import { cx } from '@tactile-ui/tokens';

export interface FrostedIconProps { className?: string }
export function FrostedIcon({ className }: FrostedIconProps) {
  return <span className={cx('tui-frosted-icon', className)} aria-hidden="true"><span className="tui-frosted-back"/><span className="tui-frosted-front">
    <span className="tui-frosted-bar"/><span className="tui-frosted-bar"/><span className="tui-frosted-bar"/>
  </span></span>;
}
