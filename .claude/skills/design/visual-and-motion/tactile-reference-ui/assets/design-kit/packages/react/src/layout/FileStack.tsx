'use client';
import { cx } from '@tactile-ui/tokens';
import type { FileItem } from '@tactile-ui/tokens';

export interface FileStackProps { title: string; files: FileItem[]; className?: string }
export function FileStack({ title, files, className }: FileStackProps) {
  return <section className={cx('tui-file-stack', className)} aria-label={title}><h3 className="tui-heading">{title}</h3><ul className="tui-file-list">{files.map(file => <li className="tui-file" key={file.id} data-kind={file.kind || 'folder'}><div className="tui-file-icon" aria-hidden="true"/><strong>{file.name}</strong><small>{file.detail}</small></li>)}</ul></section>;
}
