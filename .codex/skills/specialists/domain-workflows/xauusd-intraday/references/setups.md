# Price action playbook

These are operational hypotheses for study and evaluation, not proven XAUUSD strategies. No parameter or setup here has been backtested on this user's broker data. Sources B01/B02 provide practitioner frameworks; R01/R02/R05 explain why a chart narrative is insufficient proof. Source IDs resolve in sources.md.

## Establish the regime

Use a consistent swing definition and only information available at the observation time. A pivot that requires two subsequent bars becomes confirmed only after those bars finish; it cannot be traded retrospectively at its earlier timestamp [A01]. Identify the larger structure using completed 1-hour/15-minute bars where available.

| Regime | Observable structure | Suitable hypothesis | Common reason to wait |
|---|---|---|---|
| Uptrend | Progressively higher meaningful highs and lows; upward legs exceed pullbacks | Buy a pullback or an accepted upward breakout | Price at overhead supply/previous extreme with little target room |
| Downtrend | Meaningful lower highs and lows; downward legs exceed bounces | Sell a pullback or an accepted downward breakout | Price already at support after an extended drop |
| Range | Overlapping swings, repeated failed breaks, limited progress | Study rejection at a boundary | The middle, where stop/target geometry is poor |
| Transition/shock | Broken prior structure, large two-way bars, event repricing | Wait for a new range or direction | A single candle cannot establish the new regime |

Do not mechanically turn EMA20/50 crosses into regime labels. Indicators summarize much of the same price information. A bounce in a downtrend can be a tradable countertrend hypothesis but needs its own evaluation, not relabeling as an established uptrend [B02,T03].

## 1. Trend pullback

**Long hypothesis**

1. A completed larger-timeframe trend has a meaningful higher low that is still intact.
2. Price pulls back toward an already identifiable support zone or broken resistance. The pullback has not destroyed that structure.
3. A completed 5-minute candle rejects the zone or the pullback's local sequence breaks upward. Specify one trigger in advance, such as trading above the completed rejection candle's high after its close; don't switch trigger definitions mid-trade.
4. Plan the entry around that trigger, put structural invalidation below the pullback low with an explicit execution buffer, and set the first target at the next meaningful resistance.
5. If the entry has already run away or the real target cannot compensate for loss/costs, wait for a fresh setup.

**Short hypothesis:** invert the sequence: intact downtrend, bounce into resistance, completed rejection/local downward break, protective stop beyond pullback high, target at real support.

**Failure cases:** structural low/high is broken; pullback becomes broad overlapping chop; opposite larger-timeframe boundary blocks the target; news is imminent; spread expands; an oversized entry candle leaves too much risk. A touch of an EMA or channel alone is insufficient.

## 2. Breakout, retest, and acceptance

Use a previously identifiable range/structural boundary, not a level selected after seeing the breakout. Define the zone edges and any volatility/spread buffer from verified data before judging the break [B01,R03].

**Long hypothesis:**

1. A completed 5-minute candle closes beyond the resistance zone, not just a temporary wick.
2. Price returns toward that zone. The retest may wick through it, but a completed retest candle holds above the declared invalidation boundary and shows an upward response.
3. Enter only on the predefined upward continuation trigger; the exact response/trigger must be specified, e.g. break of the completed retest candle high. Merely "price stays there" is not a reproducible rule.
4. Stop goes beyond the retest structure, plus a disclosed execution buffer. Nearest opposing level provides the target; a range-height projection is only a secondary hypothesis and cannot erase intervening resistance.

**Short hypothesis:** completed close below support, return to the broken zone, completed rejection below/at it, predefined downward continuation trigger, stop beyond retest high.

**Failure cases:** price closes back inside the range before the continuation; no retest occurs and the entry runs away; two-way chop straddles the level; first target is too close. Retests are not inevitable. Do not chase a missed move by moving entry/stop/target together.

Institutional-currency research offers a plausible mechanism for reaction and acceleration at clustered orders, but neither today's hidden stops nor the exact gold turning point can be inferred from it [R03,R04]. Avoid claims that a wick proves "banks hunting stops."

## 3. Range edge rejection / failed breakout

This is an optional paper-test setup. Use only a well-defined range with at least repeated visible interaction on both sides and no clear larger breakout/event regime.

**Long hypothesis:** price tests or briefly exceeds the lower boundary, then a completed 5-minute bar returns into the range. Require a declared follow-through trigger, place invalidation beyond the test low, and consider the midpoint as the first obstacle before the opposite boundary. Mirror for a short at the upper edge.

A hammer/engulfing/doji supports the description of that test; its name does not establish an edge. Body and wick geometry must be interpreted where the candle forms, with the preceding sequence and target room [B05,R02]. If a strong trend is accelerating through the boundary, do not repeatedly fade it.

## Volatility, volume, and secondary tools

- **ATR14:** normalize stop distance, entry extension, and cost relative to current movement. Rising ATR can accompany a rally or selloff; it supplies no direction [T01]. A proposed 0.1 ATR zone tolerance or 1 ATR extension threshold is a parameter to test, not a fact about gold.
- **EMA20/EMA50:** contextual slope/pullback reference if enough history and the correct chart setting are available. Do not count MACD, multiple EMA crosses, and RSI as independent confirmations of the same returns [T03].
- **RSI14:** momentum summary. RSI below 30 does not force a buy, and above 70 does not force a sell. Divergence can persist or describe a pullback; require actual price confirmation [T02].
- **VWAP:** use only with a documented volume feed and reset anchor. Feed-specific tick-volume weighting is a proxy for quote activity, not consolidated traded gold volume [T04,T05]. Futures VWAP can add context but is not the executable spot price; state contract, expiry/roll, timestamp, and basis differences.
- **Fibonacci, pivots, channels, round numbers:** secondary mapping hypotheses. Don't present a ratio or channel touch as a reliable forecast. A line redrawn to fit every subsequent move cannot be honestly evaluated.

## Eligibility versus direction

Apply these independent checks: fresh executable context; known closed-bar status; appropriate regime/location; completed declared trigger; structural stop; defensible target; acceptable net costs; checked event calendar; user risk constraints. Passing the checklist makes a hypothesis coherent, not profitable. There is no validated scoring system in this skill.

| Evidence | Simple response |
|---|---|
| Downtrend at support; no completed breakdown | WAIT. Direction leans down, but selling at the floor is poor timing. |
| Green candle still below resistance, still forming | WAIT. This is a bounce; the stated buy conditions have not finished. |
| Wick over resistance; close back below it | Breakout unconfirmed/failed. Do not call a long eligible. |
| Trigger finished but price far beyond entry | MISSED / WAIT. Rebuild from a fresh structure. |
| Larger-timeframe structure missing | LIMITED DATA. Give only the visible-frame interpretation. |

## Setup expiry and exits

Distinguish three different concepts: expiry of an unentered idea, review of a position with no progress, and protective exit on invalidation. A plan can expire when structure changes, before a major release, or at the user's session end. A time stop needs evaluation on the particular setup and session. If suggesting review after 3-6 completed 5-minute bars, call it an untested practice rule and give the actual clock times from entry, not from the chat message.

Targets represent possible exit areas, not promised destination or arrival time. Predefine whether the plan exits fully at the first obstacle or scales out. Calculate weighted rewards for partial exits; a distant final target does not make a trade 2R if most size exits earlier. Move a trailing stop only on a declared structural rule that reduces risk. Do not automatically move to breakeven simply because price touches 1R; study how that affects the strategy. For an existing trade, relate current evidence to the original thesis and stop rather than supplying a new-entry rule as exit advice.
