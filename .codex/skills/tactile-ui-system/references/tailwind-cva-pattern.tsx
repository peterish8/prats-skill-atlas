/*
 * Tactile UI System — Tailwind + class-variance-authority pattern.
 *
 * Use this instead of button-system.css when the target project uses Tailwind and
 * already has `cva` (class-variance-authority) as a dependency. Swap the `vyra-*`
 * color tokens (vyra-cream, vyra-ink, vyra-accent, vyra-text, vyra-muted) for the
 * project's real Tailwind theme colors — the arbitrary shadow values encode the
 * physics and should stay as-is.
 */
import { cva } from "class-variance-authority";

export const buttonVariants = cva(
  [
    "inline-flex items-center justify-center gap-2",
    "rounded-[9px] border",
    "text-[13px] font-[600] tracking-[-0.01em]",
    "transition-[transform,background-color,border-color,box-shadow]",
    "duration-150",
    "disabled:pointer-events-none disabled:opacity-45",
    "focus-visible:outline-none focus-visible:ring-3",
    "active:translate-y-0.5",
  ],
  {
    variants: {
      variant: {
        primary: [
          "border-white/60 bg-vyra-cream text-vyra-ink",
          "shadow-[inset_0_1px_0_#fffef8,inset_0_-1px_0_rgba(0,0,0,.18),0_2px_0_#89877e,0_5px_14px_rgba(0,0,0,.30)]",
          "hover:bg-white",
          "active:shadow-[inset_0_2px_3px_rgba(0,0,0,.20)]",
        ],

        secondary: [
          "border-white/12 bg-white/[0.055] text-vyra-text",
          "shadow-[inset_0_1px_0_rgba(255,255,255,.08),0_2px_0_#070806]",
          "hover:border-white/20 hover:bg-white/[0.08]",
        ],

        accent: [
          "border-vyra-accent/35 bg-vyra-accent/10",
          "text-vyra-accent",
          "shadow-[inset_0_1px_0_rgba(235,255,160,.10),0_2px_0_rgba(44,51,20,.80)]",
          "hover:border-vyra-accent/50 hover:bg-vyra-accent/15",
        ],

        ghost: [
          "border-transparent bg-transparent text-vyra-muted",
          "shadow-none",
          "hover:bg-white/[0.055] hover:text-vyra-text",
        ],

        destructive: [
          "border-red-400/25 bg-red-400/10 text-red-300",
          "hover:border-red-400/40 hover:bg-red-400/15",
        ],
      },

      size: {
        xs: "h-7 px-2 text-[11px]",
        sm: "h-8 px-2.5 text-xs",
        md: "h-9 px-3.5",
        lg: "h-10 px-4 text-sm",
        icon: "size-8 p-0",
      },
    },

    defaultVariants: {
      variant: "secondary",
      size: "md",
    },
  },
);
