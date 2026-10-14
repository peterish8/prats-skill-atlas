'use client';
import type { ReactNode } from 'react';
import { cx } from '@tactile-ui/tokens';
import { Surface } from '../layout/Surface';
import type { SurfaceProps } from '../layout/Surface';

export interface FeatureCardProps extends Omit<SurfaceProps, 'title'> { title: string; description: string; art?: ReactNode; footer?: ReactNode }
export function FeatureCard({ title, description, art, footer, className, ...rest }: FeatureCardProps) {
  return <Surface {...rest} className={cx('tui-feature', className)}><div className="tui-feature-art">{art}</div><div className="tui-feature-copy"><h3 className="tui-heading">{title}</h3><p className="tui-caption">{description}</p>{footer}</div></Surface>;
}
