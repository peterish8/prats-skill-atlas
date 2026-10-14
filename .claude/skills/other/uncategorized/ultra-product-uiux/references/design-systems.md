# Design systems

For multi-screen products, make recurring decisions explicit with semantic tokens for color, typography, spacing, radius, borders, elevation, z-index, breakpoints, durations, and easing. Components should consume semantic roles rather than scattered literals.

Define reusable variants and states for buttons, fields, selects, badges, cards, navigation, tabs, modals, toasts, tables, and empty/loading/error surfaces. The system should be opinionated enough to prevent drift and flexible enough for a deliberate exception.

Before adding a component, inspect the closest existing implementation. Extend it if it preserves its contracts; create a new primitive only when behavior or accessibility needs differ materially. Document the rule that makes any exception intentional.

Keep surface hierarchy shallow. A card should clarify grouping or elevation; it is not default decoration. Confirm dark mode and high-contrast states at the token level so component consistency follows naturally.

## Component contract

Each reusable component should document or demonstrate:

- intent and semantic role;
- supported variants and size options;
- default, hover, focus-visible, active, disabled, loading, error, and selected states where applicable;
- keyboard behavior and accessible naming;
- responsive behavior and content-overflow strategy;
- whether it can contain other controls;
- token roles it uses, rather than raw visual values.

When a new screen needs a visual exception, first decide whether it is a reusable variant, a domain-specific composition, or a one-off. Only promote it to a token or primitive if it is likely to recur.
