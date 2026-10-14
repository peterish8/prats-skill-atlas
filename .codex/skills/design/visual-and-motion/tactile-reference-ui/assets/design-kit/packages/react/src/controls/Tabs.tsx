'use client';
import { useId, useRef } from 'react';
import type { ReactNode, KeyboardEvent } from 'react';

export interface TabItem { id: string; label: string; content: ReactNode }
export interface TabsProps { items: TabItem[]; value: string; onValueChange: (value: string) => void; label: string; className?: string }
export function Tabs({ items, value, onValueChange, label, className }: TabsProps) {
  const base = useId(), list = useRef<HTMLDivElement>(null);
  const selected = items.some(t => t.id === value) ? value : items[0]?.id;
  function move(event: KeyboardEvent<HTMLButtonElement>, index: number) {
    let next = index;
    if (event.key === 'ArrowRight') next = (index + 1) % items.length;
    else if (event.key === 'ArrowLeft') next = (index - 1 + items.length) % items.length;
    else if (event.key === 'Home') next = 0;
    else if (event.key === 'End') next = items.length - 1;
    else return;
    event.preventDefault(); onValueChange(items[next].id);
    list.current?.querySelectorAll<HTMLButtonElement>('[role=tab]')[next]?.focus();
  }
  return <div className={className}><div className="tui-tabs-list" role="tablist" aria-label={label} ref={list}>
    {items.map((item, index) => <button key={item.id} type="button" className="tui-tab" role="tab" id={base + '-tab-' + item.id} aria-controls={base + '-panel-' + item.id} aria-selected={selected === item.id} tabIndex={selected === item.id ? 0 : -1} onClick={() => onValueChange(item.id)} onKeyDown={e => move(e, index)}>{item.label}</button>)}
  </div>{items.map(item => <div key={item.id} className="tui-tab-panel" role="tabpanel" tabIndex={0} id={base + '-panel-' + item.id} aria-labelledby={base + '-tab-' + item.id} hidden={selected !== item.id}>{item.content}</div>)}</div>;
}
