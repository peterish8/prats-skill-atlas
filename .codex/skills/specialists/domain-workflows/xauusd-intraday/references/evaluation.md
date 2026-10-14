# Strategy evaluation and honest evidence

Validate two different things: (1) the assistant follows the skill and its arithmetic works, and (2) a trading rule has a reproducible edge after costs. Passing (1) proves nothing about (2).

## Define the hypothesis before testing

Specify instrument/feed, actual broker price basis, timezone/session, ordinary candles, execution/context intervals, entry sequence, trigger price, structural stop and buffer, target/partial exits, expiry, event/spread filters, sizing, and each parameter. Record versions and all variants tried. Write enough detail for another person to reproduce the same signal. Do not optimize line placement retrospectively.

## Build an honest simulation

- Use legitimate, timestamped data representative of the traded venue. Document bid/ask availability, missing bars, revisions, session breaks, and futures roll/basis if applicable.
- Signals use information available at the moment: completed context bars and pivots only after their confirmation. Execute at the next realistically available price, not automatically at the signal close. Include gap/slippage cases and unfilled limits.
- Model spread, commission, slippage, conversion, financing/rollover, and partial fills. Compare ordinary and stressed costs, particularly at news and low-liquidity periods.
- If stop and target are both inside one OHLC bar, the order is unknown. Use legitimate finer data or conservative stop-first assumptions and report the ambiguity. Do not silently assume target-first.
- Use chronological development/validation/holdout and walk-forward evaluations; account for overlapping outcomes with an appropriate separation/embargo. Final holdout must not repeatedly guide tuning. Multiple experiments still create selection bias even with a nominal holdout [R05,B03].
- Report sample size, date range, independent sessions/regimes, trades by setup, average/median net R, net expectancy, win rate with uncertainty, profit factor, maximum drawdown, loss streak, exposure/turnover, missed fills, and sensitivity. A few winning screenshots or arbitrary 30/100-trade cutoff cannot establish robustness.
- Compare with a clear baseline and untouched parameter variations. State what fails. Evidence in daily Thai/US stocks or older currency-market studies does not transfer automatically to intraday gold [R01,R02,R03].

## Paper practice and logging

Record each eligible opportunity and skipped one: timestamp and timezone, symbol/feed, before screenshot, regime, setup version, actual entry/exit, original stop, costs, exit reason, net R, event context, maximum favorable/adverse excursion where known, and adherence. Write only to a user-authorized location; don't silently create persistent personal or financial records. Grade rule adherence separately from profit: a correct losing trade can follow the rules; a lucky chase can violate them.

Paper fills differ from live liquidity and psychology. Describe the result as paper/simulated/observed, not broker-proven performance. Use forward practice after a frozen rule and conservative costs. Skill improvements should fix demonstrated behavior errors; change strategy rules only with explicit versioning and new evaluation. Don't update the user's memory store without their direct request.

## Behavioral validation scenarios

Evaluate the finished skill with varied fixtures, ideally independently when the skill-creator workflow and host authorize evaluation. Use no account/order side effects. Useful invariants:

1. A forming green candle below resistance is WAIT, not a confirmed breakout.
2. A wick over resistance that finishes below it does not satisfy a close-above trigger.
3. Downtrend at support does not become an immediate short merely because bias is bearish.
4. Already broken old chat levels do not remain active triggers without fresh validation.
5. A 5.1-point stop with a 3.5-point target is recognized as less than 1R before costs; costs reduce it further.
6. Actual bid/ask prices do not receive a second spread charge.
7. No history => no invented RSI/ATR; no contract value => no lot guess; no calendar verification => no execution-ready claim.
8. Future-confirmed pivots and incomplete higher-timeframe bars cannot generate earlier signals.
9. Missing long/short/entry details for an open trade prompt a concise question while visible-chart analysis continues.
10. Protective stop hit => protective exit condition, without waiting for a candle close. Exact target arrival time remains unknown.

Save the actual validation outcome only when relevant to maintaining this skill. Keep structural validation, arithmetic checks, behavioral review, and trading-performance evidence explicitly separate.

See [validation.md](validation.md) for the initial validation record and its limits.
