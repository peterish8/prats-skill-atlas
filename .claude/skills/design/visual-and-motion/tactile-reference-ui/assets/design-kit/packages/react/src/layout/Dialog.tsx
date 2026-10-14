'use client';
import { useEffect, useId, useRef } from 'react';
import type { ReactNode } from 'react';

export interface DialogProps { open: boolean; onOpenChange: (open: boolean) => void; title: string; children: ReactNode }
export function Dialog({ open, onOpenChange, title, children }: DialogProps) {
  const dialog = useRef<HTMLDialogElement>(null), opener = useRef<HTMLElement | null>(null), id = useId();
  useEffect(() => {
    const element = dialog.current;
    if (open && element && !element.open) { opener.current = document.activeElement as HTMLElement; element.showModal(); }
    else if (!open && element?.open) element.close();
  }, [open]);
  useEffect(() => () => { opener.current?.focus(); }, []);
  return <dialog ref={dialog} className="tui-dialog" aria-labelledby={id} onClose={() => { onOpenChange(false); opener.current?.focus(); }}>
    <div className="tui-dialog-header"><h2 id={id} className="tui-heading">{title}</h2><button type="button" className="tui-dialog-close" aria-label="Close dialog" onClick={() => dialog.current?.close()}>×</button></div>{children}
  </dialog>;
}
