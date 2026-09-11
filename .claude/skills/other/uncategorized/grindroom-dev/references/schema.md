# GrindRoom Convex Schema Reference

## profiles
Stores user identity and fitness stats.

| Field | Type | Notes |
|---|---|---|
| userId | string | Convex Auth user ID, indexed |
| displayName | string | Full name from OAuth or manual |
| username | string | Unique @handle, sanitized |
| avatarUrl | string (optional) | Profile photo URL |
| currentStreak | number | Days in current streak |
| longestStreak | number | All-time best streak |
| monthlyPoints | number | Resets to 0 on 1st of month |
| lastLogDate | string (optional) | YYYY-MM-DD of last workout |
| createdAt | number | Unix timestamp |

Indexes: `by_userId`

## rooms
Workout accountability groups.

| Field | Type | Notes |
|---|---|---|
| name | string | Room display name |
| inviteCode | string | 6-char alphanumeric, indexed |
| description | string (optional) | |
| goal | string | e.g. "Build consistency" |
| isPublic | boolean | Public discovery vs invite-only |
| memberLimit | number | Max members allowed |
| weeklyRequirement | number | Target workouts per week (stored, not yet enforced) |
| createdBy | Id<"profiles"> | Owner reference |
| createdAt | number | Unix timestamp |

Indexes: `by_inviteCode`

## roomMembers
Junction table linking users to rooms.

| Field | Type | Notes |
|---|---|---|
| roomId | Id<"rooms"> | |
| userId | string | Convex Auth user ID |
| joinedAt | number | Unix timestamp |

Indexes: `by_userId`, compound `by_room_and_user` (roomId + userId)

## workoutLogs
Individual workout entries per user per day.

| Field | Type | Notes |
|---|---|---|
| userId | string | Convex Auth user ID |
| workoutKey | string | e.g. "pushups", "squats" |
| level | "beginner" | "medium" | "advanced" | Difficulty |
| points | number | 10 / 20 / 30 |
| logDate | string | YYYY-MM-DD |
| loggedAt | number | Unix timestamp |

Indexes: `by_userId`, compound `by_user_and_date` (userId + logDate)

## monthlySnapshots
Frozen month-end rankings per user per room.

| Field | Type | Notes |
|---|---|---|
| userId | string | Convex Auth user ID |
| roomId | Id<"rooms"> | |
| month | string | YYYY-MM format |
| totalPoints | number | Points earned that month |
| finalStreak | number | Streak at month end |
| rankInRoom | number | 1-based rank in that room |

Indexes: compound `by_room_and_month` (roomId + month), `by_user_and_month` (userId + month)

## Key Relationships

```
profiles (1) ---- (many) roomMembers (many) ---- (1) rooms
profiles (1) ---- (many) workoutLogs
profiles (1) ---- (many) monthlySnapshots (many) ---- (1) rooms
```

## Convex Auth Tables (managed by library)
`authAccounts`, `authSessions`, `authVerificationCodes`, `authRateLimits` — do not modify directly.
