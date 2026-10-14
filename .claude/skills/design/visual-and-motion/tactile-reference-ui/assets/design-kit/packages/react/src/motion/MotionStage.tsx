'use client';
import { useEffect, useRef } from 'react';
import type { ReactNode } from 'react';
import { cx, motion, createMotionStage } from '@tactile-ui/tokens';

export interface MotionStageProps { children: ReactNode; paused?: boolean; intensity?: number; className?: string }
export function MotionStage({ children, paused = false, intensity = .6, className }: MotionStageProps) {
  const stage = useRef<HTMLDivElement>(null);
  const controller = useRef<ReturnType<typeof createMotionStage> | null>(null);
  const safeIntensity = Number.isFinite(intensity) ? Math.min(1, Math.max(0, intensity)) : .6;
  useEffect(() => {
    if (!stage.current) return;
    controller.current = createMotionStage(stage.current, { paused, intensity: safeIntensity });
    return () => { controller.current?.destroy(); controller.current = null; };
  }, []);
  useEffect(() => { controller.current?.update({ paused, intensity: safeIntensity }); }, [paused, safeIntensity]);
  return <div ref={stage} className={cx('tui-motion-stage', className)} data-paused={paused}>{children}</div>;
}
