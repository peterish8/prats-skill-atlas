'use client';
import { Surface } from '../layout/Surface';
import type { SurfaceProps } from '../layout/Surface';

export interface MetricCardProps extends SurfaceProps { label: string; value: string; detail?: string; note?: string }
export function MetricCard({ label, value, detail, note, children, ...rest }: MetricCardProps) {
  return <Surface {...rest}><p className="tui-metric-label">{label}</p><div className="tui-metric-value">{value}</div>{detail && <p className="tui-caption">{detail}</p>}{children}{note && <p className="tui-metric-note">{note}</p>}</Surface>;
}
