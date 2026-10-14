'use client';
import { useEffect, useRef, useState } from 'react';
import type { CSSProperties, ReactNode } from 'react';
import { cx, motion } from '@tactile-ui/tokens';

export interface RevealProps { children: ReactNode; className?: string; delay?: number }
/** Server/no-JS content stays visible. Only below-viewport content is prepared for entry. */
export function Reveal({ children, className, delay = 0 }: RevealProps) {
  const element = useRef<HTMLDivElement>(null);
  const [revealed, setRevealed] = useState(true);
  const safeDelay = Number.isFinite(delay) ? Math.min(motion.maxStagger, Math.max(0, delay)) : 0;
  useEffect(() => {
    const node = element.current;
    if (!node || typeof window.matchMedia !== 'function' || typeof IntersectionObserver === 'undefined') return;
    const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
    if (preference.matches || node.getBoundingClientRect().top < window.innerHeight) return;
    setRevealed(false);
    const reveal = () => { setRevealed(true); observer.disconnect(); };
    const observer = new IntersectionObserver(entries => {
      if (entries.some(entry => entry.isIntersecting)) reveal();
    }, { threshold: 0, rootMargin: '0px 0px -24px 0px' });
    const changePreference = () => { if (preference.matches) reveal(); };
    node.addEventListener('focusin', reveal);
    preference.addEventListener('change', changePreference);
    observer.observe(node);
    return () => {
      observer.disconnect();
      node.removeEventListener('focusin', reveal);
      preference.removeEventListener('change', changePreference);
    };
  }, []);
  return <div ref={element} className={cx('tui-reveal', className)} data-revealed={revealed} style={{ '--tui-reveal-delay': safeDelay + 'ms' } as CSSProperties}>{children}</div>;
}
