'use client';
import { useId } from 'react';
import { cx } from '@tactile-ui/tokens';

export interface SegmentedOption { value: string; label: string; disabled?: boolean }
export interface SegmentedControlProps { label: string; value: string; options: SegmentedOption[]; onValueChange: (value: string) => void; className?: string }
export function SegmentedControl({ label, value, options, onValueChange, className }: SegmentedControlProps) {
  const name = useId();
  return <fieldset className={cx('tui-segmented', className)}><legend className="tui-segmented-legend">{label}</legend><div className="tui-segmented-options">{options.map((option, index) => <label className="tui-segmented-option" key={option.value} htmlFor={name + '-' + index}><input id={name + '-' + index} type="radio" name={name} value={option.value} checked={value === option.value} disabled={option.disabled} onChange={() => onValueChange(option.value)}/><span>{option.label}</span></label>)}</div></fieldset>;
}
