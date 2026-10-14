export const directions = [
  { id: 'porcelain', name: 'Porcelain desk', note: 'Quiet depth. Clear edges. Space to think.', refs: '07 · 09 · 10 · 15 · 18', accent: '#3967d8' },
  { id: 'spectral', name: 'Spectral atmosphere', note: 'Blue light, lavender air, luminous focal objects.', refs: '02 · 03 · 05 · 11 · 12 · 13', accent: '#3755d8' },
  { id: 'editorial', name: 'Warm editorial', note: 'Confident typography and one warm physical detail.', refs: '08 · 13 · 16', accent: '#bd4808' },
  { id: 'citrus', name: 'Citrus playground', note: 'Generous shapes with a bright, optimistic center.', refs: '14 · 18 · 29 · 30 · 31', accent: '#29632c' },
  { id: 'signal', name: 'Precision signal', note: 'Compact data, deliberate hierarchy, readable states.', refs: '01 · 04 · 06', accent: '#4338ca' },
  { id: 'connected', name: 'Connected canvas', note: 'Thin paths, tactile nodes, a visible relationship.', refs: '05 · 07 · 09 · 10 · 16 · 17 · 20 · 21', accent: '#286ac1' },
  { id: 'meadow', name: 'Meadow light', note: 'Soft botanical light, an editorial headline, one clear invitation.', refs: '22 · 26', accent: '#273e2c' },
  { id: 'equilibrium', name: 'Lime equilibrium', note: 'Fine vertical rules, ample white space, quiet institutional confidence.', refs: '23', accent: '#38451c' },
  { id: 'systems', name: 'Mint infrastructure', note: 'A readable network of paths, crisp copy, and mint light.', refs: '24', accent: '#093e34' },
  { id: 'prism', name: 'Refracted blue', note: 'Blue light through fine ribs; a warm, spacious editorial plane.', refs: '25 · 26', accent: '#1d3d68' },
  { id: 'atelier', name: 'Pixel atelier', note: 'Monochrome typography, cyan pixels, and precise graphic texture.', refs: '27 · 28', accent: '#151719' },
  { id: 'landscape', name: 'Landscape product', note: 'Real product details staged in open air and soft pastel landscapes.', refs: '32 · 33 · 34 · 35 · 36', accent: '#233fad' }
] as const;
export type Direction = typeof directions[number]['id'];
export type Tone = 'neutral' | 'info' | 'success' | 'warning' | 'danger';
export type Depth = 'flat' | 'raised' | 'recessed' | 'floating';
export type Texture = 'none' | 'dots' | 'grain' | 'lines';
export type ButtonVariant = 'primary' | 'secondary' | 'ghost' | 'danger';
export interface MapNode { id: string; label: string; detail?: string; symbol?: string }
export interface FileItem { id: string; name: string; detail: string; kind?: 'folder' | 'document' }
export interface NavigationItem { label: string; href: string }
export interface ActionItem { label: string; href: string }
export type Atmosphere = 'meadow' | 'contours' | 'paths' | 'ribs' | 'pixels' | 'scanlines' | 'landscape';
export type ShowcaseTone = 'meadow' | 'blue' | 'mint' | 'lavender';
export const motion = { press: 110, control: 180, panel: 260, reveal: 560, stagger: 70, maxStagger: 280 } as const;
export { createMotionStage } from './motion.js';
export type { MotionStageOptions, MotionStageController } from './motion.js';
export type MaterialKind = 'orb' | 'coin' | 'sun' | 'certificate';
export interface SegmentOption { value: string; label: string; disabled?: boolean }
export interface AvatarItem { id: string; name: string; initials: string }
export const cx = (...parts: (string | false | null | undefined)[]) => parts.filter(Boolean).join(' ');
/** Chart coordinates only. Callers own dates, units and the source of values. */
export function sparklinePoints(values: number[], width = 320, height = 100): string {
  if (values.length < 2 || values.some(v => !Number.isFinite(v))) return '';
  const min = Math.min(...values), max = Math.max(...values), span = max - min || 1;
  return values.map((v, i) => [8 + i * (width - 16) / (values.length - 1), height - 8 - (v - min) / span * (height - 16)].join(',')).join(' ');
}
