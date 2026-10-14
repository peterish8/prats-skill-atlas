'use client';
import { cx } from '@tactile-ui/tokens';
import type { Atmosphere } from '@tactile-ui/tokens';

export interface AmbientBackdropProps { kind: Atmosphere; animated?: boolean; className?: string }
/** Original CSS/SVG atmosphere. Keep all meaningful content outside this layer. */
export function AmbientBackdrop({ kind, animated = false, className }: AmbientBackdropProps) {
  return <div className={cx('tui-atmosphere', className)} data-kind={kind} data-animated={animated} aria-hidden="true">
    <span className="tui-atmosphere-layer"/><span className="tui-atmosphere-layer"/><span className="tui-atmosphere-layer"/>
  </div>;
}
