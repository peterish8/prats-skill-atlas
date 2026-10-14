'use client';

export interface MeterProps { label: string; value: number; max: number; valueText: string }
export function Meter({ label, value, max, valueText }: MeterProps) {
  const safeMax = Number.isFinite(max) && max > 0 ? max : 1;
  const safeValue = Number.isFinite(value) ? Math.min(safeMax, Math.max(0, value)) : 0;
  return <div className="tui-meter"><div className="tui-meter-label"><span>{label}</span><span>{valueText}</span></div><div className="tui-meter-track" role="meter" aria-label={label} aria-valuemin={0} aria-valuemax={safeMax} aria-valuenow={safeValue} aria-valuetext={valueText}><div className="tui-meter-fill" style={{ width: String(100 * safeValue / safeMax) + '%' }}/></div></div>;
}
