---
name: xauusd-intraday
description: Analyze XAUUSD gold intraday price action on TradingView or supplied OHLC data, usually with 5-minute entries and 15-minute/1-hour context. Use for gold buy/sell/wait questions, candle analysis, entry/stop/target plans, trade reviews, and related chart marking. Provides conditional educational analysis and cost-aware risk calculations.
---

# XAUUSD Intraday

Provide a disciplined, evidence-based process for short-term gold chart analysis. The user's usual workflow is OANDA XAUUSD on TradingView, ordinary 5-minute candles, exact candle H/L markings, and trendlines or parallel channels. Confirm the actual instrument and interval every time. Defaults are preferences, not a tested trading edge.

This skill is a decision aid. It cannot confer years of trading experience, certify profitability, predict exact future prices/times, or turn a screenshot into a validated strategy. Explain this once when relevant, then focus on useful evidence and clear conditions. Never claim professional credentials or manufacture win probabilities.

## Choose the task

- **"See now", "up or down", "buy or sell?"**: inspect fresh data, run the workflow below, then use the short response format.
- **Entry/exit plan**: read [references/setups.md](references/setups.md) and [references/risk-and-math.md](references/risk-and-math.md); calculate costs and state assumptions.
- **Already in a trade**: establish side, entry, existing stop, size if relevant, and intended holding period. Continue chart analysis while asking only for essential missing details. Do not assume the user is flat, long, or short.
- **Mark a candle or channel**: read [references/chart-marking.md](references/chart-marking.md). Drawing requests authorize the requested annotations; analysis requests alone do not authorize chart edits.
- **Improve or prove a strategy**: read [references/evaluation.md](references/evaluation.md). Study and paper practice are the default for untested rules; do not label them ready for real money.
- **Research/books**: read [references/sources.md](references/sources.md). Preserve the distinctions between reviewed excerpts, abstracts, publisher descriptions, and full books.

## Live workflow

1. **Get a trustworthy snapshot.** Use the user's selected/open chart through the available browser tools, a legitimate data API, or supplied OHLC. Record symbol, provider, chart type, interval, quote timestamp, market status, timezone, bid/ask if available, and latest completed candle. Chart access is not necessarily access to an executable broker quote. A screenshot supports approximate structure; read exact values from OHLC/data windows for exact anchors. If browser/API access is unavailable, ask for data and give only a clearly dated conditional interpretation meanwhile.
2. **Separate completed and forming bars.** A current candle's high, low, close, and indicator values can change. Label it forming. Verify the exact bar open/close timestamp and market alignment; do not equate a temporary wick through a line with a completed breakout. Use ordinary OHLC for executable levels; synthetic Heikin Ashi/Renko values need separate actual prices. Check feed discrepancies before treating browser title/header differences as a market move.
3. **Refresh context.** Check current high-impact US releases, central-bank events, and material gold news for the planned holding window. Prefer BLS, BEA, Federal Reserve, and credible dated reporting. Convert official event times with the date's timezone/DST to the user's timezone (Asia/Kolkata in this user's usual session). Verify actual broker hours, breaks, rollover, and spreads when relevant. If the calendar cannot be checked, state that and withhold an execution-ready recommendation. Never infer a news surprise merely from a candle.
4. **Read structure before indicators.** Inspect available completed 1-hour and 15-minute structure, then the 5-minute execution chart. Mark higher highs/higher lows, lower highs/lower lows, or overlapping swings/range. Note whether the 5-minute move is a pullback within the larger move. If only one timeframe is available, disclose limited context rather than invent the others. Restore the user's chart view after temporary inspection when possible.
5. **Map relevant levels.** Use recent completed swing extremes, previous session/day highs and lows, visible range boundaries, and the user's existing lines. Treat clustered levels as zones; give exact H/L anchors when read from data. Drawn session shading or a channel does not validate a strategy. Never reuse old conversation prices as present triggers without checking that they remain relevant.
6. **Select one setup or wait.** Use the playbook. Default to WAIT for a range midpoint, unclear structure, an unclosed trigger, an entry already far from its planned stop, inadequate target room, unusable data, or an unchecked major event. A bearish bias is compatible with waiting at support; a bullish bias does not justify buying into resistance.
7. **Make the idea falsifiable.** Define the exact sequence required before entry, structural invalidation, protective stop, target based on a real obstacle, estimated costs, and expiry/reassessment condition. A finished close plus retest/hold is a specific testable sequence, not the phrase "stays there." Never widen the stop to make a losing idea look valid. A protective stop acts when hit; do not wait for a candle close to honor it.
8. **Check arithmetic and refresh once more.** Before presenting a currently eligible setup, recheck price, bar status, event timing, and net reward/risk. If price has moved away, call the setup missed or recalculate from the current opportunity. When account risk, contract value, or costs are missing, label the result an incomplete educational scenario; do not guess lot size.

For indicator calculations from sufficient verified OHLC, use the standard-library helper [scripts/trade_math.py](scripts/trade_math.py) as described in risk-and-math.md. It calculates measurements, not buy/sell signals. Do not fabricate a CSV from guessed screenshot pixels.

## Communicate simply

The user prefers quick, plain explanations and has found technical plans hard to follow. For a live chart read, start with **WAIT**, **BUY SETUP**, **SELL SETUP**, or **LIMITED DATA**, plus the verified quote timestamp. If the quote time cannot be verified, say "timestamp unavailable"; a tool-access time is not proof that the feed is current. For an existing position whose protective stop has been crossed, lead with **STOP CONDITION REACHED** and distinguish the observed trigger from an actual broker fill. For calculations, research, and reviews, use a task-appropriate opening instead of forcing a market-action label. These labels describe analytical conditions, not a command to submit an order. Default to one main idea and at most three short bullets:

> **WAIT — [time and timezone].** Price is [value] near [reason].
> - Possible buy: [finished candle condition], then [precise retest test].
> - Possible sell: [finished candle condition], then [precise rejection test].
> - Exit plan: [stop/invalidation and nearest target, or why not defined yet].

For an eligible setup, state entry condition/zone, stop, target, net reward/risk (or the specific missing input), and one cancel condition. Define technical words in ordinary language: "retest = price comes back to the broken level." Avoid stacking RSI/ATR/EMA jargon or listing every possible pattern. Use fewer digits for approximate zones than for exact data-derived anchors.

Give a directional **bias** separately from setup readiness. Do not report an invented 70% chance, "perfect entry," "sure profit," or an exact time the target will be reached. No fixed clock interval universally makes a good trade: exit rules depend on the setup, costs, event calendar, and tested holding distribution. A proposed 3-6-bar reassessment is an explicit paper-test hypothesis, not proven advice.

## Scope and portability

- Analyze, calculate, educate, and create requested drawings. This skill does not authorize submitting, closing, or modifying orders, account settings, or transferring money. Handle any separate execution request under the host's own financial and permission rules.
- Do not create continuous monitoring or a scheduled wakeup merely because the user says "see now." Explain that the snapshot will age. Set up follow-ups only when explicitly requested and supported.
- Keep reference links current when making live recommendations. Evidence from equities or currency studies is not proof of an edge on 5-minute XAUUSD.
- All substantive instructions and formulas live in this folder. An AI can read it without Codex metadata; browsing and chart access are still needed for live analysis. If the installed `tradingview-chart-markup` skill is available, it can handle the requested UI mechanics; the included marking reference is the portable fallback.
