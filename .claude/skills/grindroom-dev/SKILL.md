---
name: grindroom-dev
description: GrindRoom app development context. This skill should be used whenever working on the GrindRoom React Native fitness accountability app at c:\grindroom. Provides the Convex schema, design tokens, animation primitives, and coding conventions so Claude never needs re-explanation of the project setup.
---

# GrindRoom Development Context

GrindRoom is a React Native / Expo fitness accountability app. Users log daily workouts, maintain streaks, compete in rooms (squads), and track monthly leaderboard rankings.

## Stack

- **Framework**: React Native + Expo (Expo Router for file-based navigation)
- **Backend**: Convex (real-time database + auth + cron jobs)
- **Auth**: Convex Auth — Google OAuth + password
- **Styling**: NativeWind v4 (Tailwind CSS for React Native via `className` props)
- **Animations**: React Native Reanimated — NEVER Framer Motion, NEVER CSS animations
- **State**: Zustand (`store/uiStore.ts`) for UI state only; Convex queries for server state
- **Icons**: Lucide React Native

## CRITICAL: Animation Rule

This app uses **React Native Reanimated**. Never suggest Framer Motion, CSS transitions, or web animation APIs. All animations use `withSpring`, `withTiming`, `withSequence`, `useAnimatedStyle`, `useSharedValue` from `react-native-reanimated`.

Standard spring config used everywhere:
```ts
{ damping: 15, stiffness: 500, mass: 0.8 }
```

Reusable animation primitives live in `components/animations/`:
- `FadeIn` — staggered entrance with delay, direction, distance props
- `ScalePress` — tap feedback (scales 0.96 on press)
- `StaggeredList` — cascade list item animations
- `AnimatedModal` — spring-based modal backdrop + bottom sheet
- `AnimatedDropdown` — animated dropdown menu
- `Skeleton` — loading placeholders (SkeletonCard, SkeletonStats)
- `AnimatedNumber` — animated number counter
- `SuccessCelebration` — confetti on 5/5 daily goal completion

Always reuse these primitives before writing new animation code.

## Design Tokens

See `references/design-tokens.md` for full token reference.

Key values:
- Background: `#0e0e0e`
- Primary accent (lime): `#C8F135`
- Surface: `#1A1A1A`
- Surface 2: `#2A2A2A`
- Fonts: Oswald (headings/display), Inter (body/UI)

## Convex Schema

See `references/schema.md` for full schema with field types, indexes, and relationships.

Key tables: `profiles`, `rooms`, `roomMembers`, `workoutLogs`, `monthlySnapshots`

## Business Logic

- **Points**: beginner = 10pts, medium = 20pts, advanced = 30pts
- **Streaks**: increment if user logged yesterday; reset to 1 if gap > 1 day; no change if already logged today
- **Monthly reset**: Convex cron on 1st of month freezes scores into `monthlySnapshots`, resets all `monthlyPoints` to 0
- **Invite codes**: 6-character alphanumeric, stored on `rooms.inviteCode`
- **Leaderboard sort**: `monthlyPoints DESC`, then `currentStreak DESC`

## Navigation Structure

```
Root (_layout.tsx)
  app/index.tsx              -- auth guard / redirect
  app/auth-callback.tsx      -- OAuth redirect handler
  app/(auth)/splash.tsx      -- landing + Google sign-in
  app/(auth)/login.tsx       -- email/password login
  app/(tabs)/index.tsx       -- Home (daily progress, streaks, points)
  app/(tabs)/log.tsx         -- Workout logger (10 presets x 3 levels)
  app/(tabs)/rooms.tsx       -- Room list + join/create
  app/(tabs)/profile.tsx     -- Stats, heatmap, monthly history
  app/room/[id]/index.tsx    -- Room detail + leaderboard
  app/create-room/index.tsx  -- Create room step 1
  app/create-room/settings.tsx -- Create room step 2
```

## Convex File Map

```
convex/schema.ts        -- table definitions
convex/users.ts         -- profile queries/mutations
convex/workoutLogs.ts   -- logging + streak logic
convex/rooms.ts         -- room CRUD + join/leave
convex/leaderboard.ts   -- getRoomLeaderboard, getTodayActivity
convex/snapshots.ts     -- monthly freeze cron
convex/auth.ts          -- Convex Auth config
convex/crons.ts         -- scheduled jobs
```

## Coding Conventions

- Use `className` (NativeWind) for all styling — avoid `StyleSheet.create` unless required by a library
- Convex queries with `useQuery`, mutations with `useMutation` from `convex/react`
- All Convex functions are in `convex/` directory, imported via `api` object
- Loading states: use `Skeleton` components while queries return `undefined`
- Error states: `Alert.alert()` for user-facing errors
- Always check if user is authenticated before Convex calls (`useQuery(api.users.getCurrentUser)`)
