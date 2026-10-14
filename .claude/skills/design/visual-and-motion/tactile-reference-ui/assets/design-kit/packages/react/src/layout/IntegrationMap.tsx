'use client';
import type { ReactNode } from 'react';
import { cx } from '@tactile-ui/tokens';
import type { MapNode } from '@tactile-ui/tokens';
import { Orb } from '../display/Orb';

export interface IntegrationMapProps { nodes: MapNode[]; title: string; detail?: string; center?: ReactNode; className?: string }
export function IntegrationMap({ nodes, title, detail, center, className }: IntegrationMapProps) {
  const midpoint = Math.ceil(nodes.length / 2);
  const side = (items: MapNode[]) => <ul className="tui-map-side">{items.map(node => <li className="tui-map-node" key={node.id}><span className="tui-map-symbol" aria-hidden="true">{node.symbol || '↗'}</span><span><strong>{node.label}</strong>{node.detail && <small>{node.detail}</small>}</span></li>)}</ul>;
  return <section className={cx('tui-map', className)} aria-label={title}>
    <svg className="tui-map-connectors" viewBox="0 0 600 280" preserveAspectRatio="none" aria-hidden="true"><path d="M70 65H175Q195 65 195 85V120Q195 140 220 140H380Q405 140 405 120V85Q405 65 425 65H530M70 215H175Q195 215 195 195V160Q195 140 220 140M380 140Q405 140 405 160V195Q405 215 425 215H530" stroke="currentColor" strokeWidth="1" fill="none"/></svg>
    {side(nodes.slice(0, midpoint))}<div className="tui-map-center">{center || <Orb appearance="accent">↔</Orb>}<strong>{title}</strong>{detail && <small className="tui-caption">{detail}</small>}</div>{side(nodes.slice(midpoint))}
  </section>;
}
