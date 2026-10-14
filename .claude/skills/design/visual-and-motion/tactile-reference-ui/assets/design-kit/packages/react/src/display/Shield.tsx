'use client';
import { useId } from 'react';
import { cx } from '@tactile-ui/tokens';

export interface ShieldProps { className?: string }
export function Shield({className}:ShieldProps) {
  const id=useId();
  return <svg viewBox="0 0 180 210" className={cx('tui-shield',className)} aria-hidden="true"><defs><linearGradient id={id} x1="0" y1="0" x2=".3" y2="1"><stop stopColor="#316cf6"/><stop offset=".55" stopColor="#327bf8"/><stop offset="1" stopColor="#65c1f0"/></linearGradient></defs><path d="M90 10Q48 34 18 30V121Q18 164 90 198Q162 164 162 121V30Q130 34 90 10Z" fill={'url(#'+id+')'} stroke="#afdcff" strokeWidth="1.5"/><path d="M90 12V52M38 32V56Q38 72 49 79M142 32V56Q142 72 131 79M90 158V196" fill="none" stroke="#d4ecff" opacity=".35"/><path d="M69 100C73 84 97 81 107 96M105 87L109 99L97 100M110 110C106 127 82 130 72 115M74 125L70 113L82 112" fill="none" stroke="#f1faff" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"/></svg>;
}
