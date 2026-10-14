'use client';
import { cx } from '@tactile-ui/tokens';

export interface MaterialObjectProps { kind: 'orb' | 'coin' | 'sun' | 'certificate'; className?: string }
export function MaterialObject({ kind, className }: MaterialObjectProps) {
  return <span className={cx('tui-material-object', className)} data-kind={kind} aria-hidden="true"><span className="tui-material-core"/><span className="tui-material-ring"/><span className="tui-material-glint"/></span>;
}
