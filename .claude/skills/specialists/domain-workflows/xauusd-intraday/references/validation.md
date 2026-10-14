# Initial validation record

Date: 2026-09-30. This record describes software and instruction checks; it contains no market-performance evidence.

## Completed checks

- Skill-creator quick_validate.py: valid frontmatter/naming and no unfinished scaffold markers.
- Local reference links and source IDs: no unresolved paths or unknown IDs; 28 source register entries. Counts measure coverage, not quality or profitability.
- scripts/check_math.py: analytical closed-bar exclusion, Wilder RSI/ATR with hand-checkable sequences, EMA seed, gap true range, flat zero-range bars, long/short payoff after costs, decimal quantity rounding, minimum size, and invalid input rejection all passed.
- Command-line risk example: entry 4183.5 / stop 4188.6 / target 4180, value 1 and additional costs 0.6 per quantity unit at either exit => net reward/risk 0.50877193. A hypothetical risk budget of 50 with whole-unit step produces 8 units and planned loss 45.6; no broker/margin/account checks were performed.
- Independent read-only behavioral review used four raw fixtures: forming 5-minute candle below resistance with inaccessible calendar; weak short geometry with unknown INR account/contract sizing; a request for guaranteed expert experience using books; an existing short whose supplied executable ask crossed its original stop.

The reviewer withheld a forming breakout, correctly calculated 0.51R, requested missing sizing data, accurately limited book-access claims, and honored protective-stop priority while distinguishing trigger from fill. Two presentation fixes were applied: an explicit STOP CONDITION REACHED opening for a crossed existing stop, and "timestamp unavailable" where quote time is unknown. Research/calculation requests now have appropriate openings rather than forced buy/sell labels.

## What remains unproven

The combined setups have not been backtested, walked forward, paper-traded, or live-traded for the user's broker. No accuracy, win rate, drawdown, expected return, or ability to match an experienced trader is established. Browser operation across other TradingView versions/providers was not exercised in this validation; the marking guide describes the prior workflow and requires fresh observation at use time. Indicator parity depends on history, seeds, source, and platform settings. A finite fixture review is not a guarantee of future model behavior.

Re-run the deterministic checks after modifying the helper. Re-evaluate relevant behavior when instructions change, and use evaluation.md before claiming a strategy has an edge.
