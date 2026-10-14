'use client';
import type { ReactNode } from 'react';
import { cx } from '@tactile-ui/tokens';
import type { Tone } from '@tactile-ui/tokens';

export interface InlineNoticeProps { title: string; tone?: Tone; children: ReactNode; className?: string }
export function InlineNotice({ title, tone = 'neutral', children, className }: InlineNoticeProps) {
  return <aside className={cx('tui-notice', className)} data-tone={tone}><h3 className="tui-notice-title">{title}</h3><div>{children}</div></aside>;
}
