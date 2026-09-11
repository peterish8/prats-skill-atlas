# GrindRoom Design Tokens

## Colors (`constants/theme.ts`)

### Core Palette
| Token | Hex | Usage |
|---|---|---|
| background | `#0e0e0e` | App background, screen bg |
| surface | `#1A1A1A` | Cards, modals, bottom sheets |
| surface2 | `#2A2A2A` | Input fields, nested surfaces |
| primary | `#C8F135` | CTA buttons, active states, accents |
| primaryDark | `#A8D015` | Pressed primary button |
| text | `#FFFFFF` | Primary text |
| textSecondary | `#888888` | Subtitles, labels, metadata |
| textMuted | `#555555` | Disabled, placeholder |
| border | `#2A2A2A` | Dividers, card borders |
| error | `#FF4444` | Error states, streak at-risk |
| success | `#C8F135` | Same as primary — success = lime |

### Gradient Usage
- Hero cards: `['#1A1A1A', '#0e0e0e']` vertical
- Primary button: solid `#C8F135`
- Streak at-risk: `['#FF4444', '#CC0000']`

## Typography

### Fonts
| Font | Weight | Usage |
|---|---|---|
| Oswald | 700 (Bold) | Screen titles, stats, big numbers |
| Oswald | 600 (SemiBold) | Section headers, card titles |
| Inter | 500 (Medium) | Buttons, labels |
| Inter | 400 (Regular) | Body text, descriptions |

### Scale
| Name | Size | Font | Usage |
|---|---|---|---|
| Display | 48px | Oswald 700 | Streak number, hero stat |
| H1 | 32px | Oswald 700 | Screen titles |
| H2 | 24px | Oswald 600 | Section headers |
| H3 | 18px | Oswald 600 | Card titles |
| Body | 16px | Inter 400 | Body text |
| Label | 14px | Inter 500 | Buttons, badges |
| Caption | 12px | Inter 400 | Metadata, timestamps |

## Spacing (`constants/theme.ts`)
| Token | Value |
|---|---|
| xs | 4px |
| sm | 8px |
| md | 16px |
| lg | 24px |
| xl | 32px |
| 2xl | 48px |

## Border Radius
| Token | Value | Usage |
|---|---|---|
| default | 16px | Cards, modals |
| large | 24px | Bottom sheets, hero cards |
| full | 9999px | Badges, pills, avatar circles |

## NativeWind Class Conventions

Common patterns used in GrindRoom:

```
bg-[#0e0e0e]        -- screen background
bg-[#1A1A1A]        -- card/surface
bg-[#C8F135]        -- primary button/accent
text-white          -- primary text
text-[#888]         -- secondary text
rounded-2xl         -- default card radius (16px)
rounded-3xl         -- large card radius (24px)
rounded-full        -- pill/badge radius
p-4                 -- standard padding (16px)
px-4 py-3           -- button padding
gap-3               -- standard gap between items
```

## Animation Tokens

Standard Reanimated spring (used across all components):
```ts
const SPRING = { damping: 15, stiffness: 500, mass: 0.8 }
```

Press scale: `0.96` (ScalePress component)
Modal enter: translateY from `screenHeight` to `0`
FadeIn default: opacity 0->1, translateY 20->0
Stagger delay: `50ms` per item
