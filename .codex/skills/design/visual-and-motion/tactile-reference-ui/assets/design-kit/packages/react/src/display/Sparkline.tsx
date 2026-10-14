'use client';
import { useId } from 'react';
import { cx, sparklinePoints } from '@tactile-ui/tokens';

export interface SparklineProps { values: number[]; label: string; className?: string }
export function Sparkline({ values, label, className }: SparklineProps) {
  const id = useId(), points = sparklinePoints(values);
  return <svg className={cx('tui-sparkline', className)} viewBox="0 0 320 100" role="img" aria-labelledby={id}><title id={id}>{label}</title>
    <path d="M8 92H312" fill="none" stroke="currentColor" opacity=".12"/>
    {points ? <polyline points={points} fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"/> : <text x="8" y="50" fill="currentColor" fontSize="14">No chart data</text>}
  </svg>;
}
