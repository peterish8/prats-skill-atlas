'use client';
import type { ReactNode } from 'react';
import { FeatureCard } from '../layout/FeatureCard';
import { Button } from '../controls/Button';

export interface OnboardingCardProps { title:string;description:string;art?:ReactNode;step:number;steps:number;onContinue:()=>void;continueLabel?:string }
export function OnboardingCard({title,description,art,step,steps,onContinue,continueLabel='Continue'}:OnboardingCardProps){
  const count=Math.max(1,Math.floor(steps)),current=Math.min(count,Math.max(1,Math.floor(step)));
  return <FeatureCard title={title} description={description} art={art} footer={<div className="tui-onboarding-footer"><Button onClick={onContinue}>{continueLabel}</Button><span className="tui-steps" aria-label={'Step '+current+' of '+count}>{Array.from({length:count},(_,i)=><span key={i} data-current={i===current-1} aria-hidden="true"/>)}</span></div>}/>;
}
