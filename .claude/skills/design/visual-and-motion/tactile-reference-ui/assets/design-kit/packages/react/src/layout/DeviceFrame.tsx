'use client';
import { useId } from 'react';
import type { ReactNode } from 'react';
import { cx } from '@tactile-ui/tokens';

export interface DeviceFrameProps { label: string; variant?: 'desktop' | 'phone'; children: ReactNode; className?: string }
export function DeviceFrame({ label, variant = 'desktop', children, className }: DeviceFrameProps) {
  const caption = useId();
  return <figure className={cx('tui-device-frame', className)} data-variant={variant} aria-labelledby={caption}>
    <div className="tui-device-chrome" aria-hidden="true"><span/><span/><span/></div><div className="tui-device-content">{children}</div><figcaption className="tui-device-caption" id={caption}>{label}</figcaption>
  </figure>;
}
