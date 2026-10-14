# Measurements, costs, sizing, and examples

Use verified data and explicit assumptions. All prices below are invented arithmetic examples, not live triggers. Source IDs refer to sources.md. The included script performs these calculations; it is not a strategy, data source, or broker simulator.

## Candle measurements

For ordinary OHLC with H >= max(O,C), L <= min(O,C):

- Range = H-L; body = abs(C-O).
- Upper wick = H-max(O,C); lower wick = min(O,C)-L.
- Body fraction = body/range; close location = (C-L)/range.
- If range is zero, body fraction and close location are undefined (null), not directional signals.

A body fraction of 0.7 or a close near the top measures bar shape, not a 70% probability of winning. Forming bars must be excluded from confirmed signal calculations.

## ATR, EMA, RSI, and VWAP

**True range** = max(H-L, abs(H-previous C), abs(L-previous C)). For the first available candle without previous close, use H-L and disclose the boundary convention. **Wilder ATR(n)**: seed with the mean of the first n true ranges, then ATR = (previous ATR*(n-1)+TR)/n [T01].

**EMA(n)**: alpha = 2/(n+1); EMA = alpha*C+(1-alpha)*previous EMA. The helper seeds with the first n closes' SMA; some platforms use a different initial seed. Supply substantial warmup (prefer at least 5*n bars when possible), record the convention, and don't claim bit-for-bit chart parity from short history [T03].

**RSI(n)**: compute n close-to-close changes (needs n+1 closes), split gains=max(change,0), losses=max(-change,0), and use Wilder smoothing for both averages. RSI=100-100/(1+average gain/average loss). Zero loss with positive gain => 100; zero gain with positive loss => 0; both zero => null in the helper (platform conventions differ) [T02].

**Session VWAP proxy** = sum(((H+L+C)/3)*V)/sum(V), reset at the documented anchor [T04]. Actual execution VWAP uses trade prices/size; OHLC typical-price VWAP is a bar approximation. Do not compute with missing/zero volume or present quote tick counts as consolidated transactions [T05]. VWAP is deliberately not calculated by the helper because it cannot infer the correct volume type or session anchor.

ATR and indicators use bars on the specified timeframe: ATR14 on 5-minute data is a 14-bar measure, not 14 days. They summarize historical data; none guarantees the next candle.

## Cost model and reward/risk

Choose one price convention and disclose it:

1. **Executable-price convention**: entry, protective exit, and target are expected actual bid/ask fills. Longs generally enter ask and exit bid; shorts enter bid and exit ask. Spread is already represented in those fills. Add only commissions, expected slippage beyond those fills, and relevant financing/conversion costs.
2. **Reference-price convention**: levels are all consistently chart/reference prices. Add the estimated full round-trip spread effect, commissions, slippage, and financing as additional costs. This is an approximation, not an executable quote model.

Never charge spread twice. A chart may use bid, mid, or another source; verify it. Quote precision and a display label such as "44.0" do not themselves identify a universal gold pip size. Use ask-bid in actual price units.

Let D=abs(entry-stop), G=direction*(target-entry) where direction is +1 long, -1 short, and V is account-currency value of a 1.00 price move per quantity unit. Costs per unit can differ at stop versus target:

```text
gross loss per unit   = D*V
gross profit per unit = G*V
net loss per unit     = gross loss + stop-side total costs
net profit per unit   = gross profit - target-side total costs
net reward/risk       = net profit / net loss
break-even win rate   = net loss / (net loss + net profit)
```

The break-even probability is an algebraic threshold for a fixed binary payoff, not an estimated win rate. For variable payouts use the actual outcome distribution. Negative net profit makes the hypothetical target economically unsuitable.

The user's tested minimum reward/risk governs eligibility. If none exists, an illustrative 1.5-2R paper-study filter can help reject cramped trades, but it is not universal or proof of positive expectancy. Do not move targets beyond intervening levels to pass the filter.

**Example exposing a weak short:** entry 4183.5, stop 4188.6, target 4180.0 => risk 5.1 and reward 3.5, gross reward/risk only 0.686. With 0.6 additional price-equivalent round-trip costs at either exit and V=1: net risk 5.7, net reward 2.9, ratio 0.509, break-even win rate 66.28%. That is not a good 2R setup merely because price looks bearish. This example repairs a weakness of casually combining a wide stop with a nearby target.

## Position size

Ask for account equity/currency, maximum cash or percentage loss per trade, remaining daily loss allowance, broker/entity/platform, contract multiplier, minimum quantity, increment, and margin constraints before calculating a real position. The OANDA label on a chart is not proof of which broker account the user trades.

```text
risk cash = equity * chosen risk fraction
raw quantity = min(risk cash, remaining daily loss allowance) / net loss per unit
quantity = floor(raw quantity / quantity step) * quantity step
```

Reject quantity below the minimum; never round up past the risk cap. Check broker margin/notional limits separately. **Leverage and margin are not the chosen loss budget.** Contract value differs among spot units, CFDs, MT4 lots, COMEX contracts, and account currencies; no universal "1 gold lot" is assumed [P01,P02,E02]. If account currency differs from P&L currency, use a current, dated conversion or withhold sizing. Scheduled swaps and gaps can exceed the estimate.

There is no personally appropriate risk fraction in this skill. If the user has none, use a clearly labeled hypothetical/paper budget rather than inventing an amount suitable for their finances. Never martingale, increase size to recover a loss, or infer permission to place the result as an order.

For partial targets with fractions f_i summing to 1, weighted gross gain=sum(f_i*gain_i). Include costs for each partial fill, then divide by the original planned net risk. Calculate possible paths as well: the first partial exit may be followed by a stop on the remainder.

## Expectancy and drawdown

For comparable recorded trades, E=p*average net win-(1-p)*average net loss. If wins/losses are already net, do not deduct fees twice [B01]. Historical p comes with sample size, time period, setup definition, and uncertainty; do not replace it with confidence in a screenshot. Include zero outcomes and variable losses in the full mean where relevant.

A loss fraction d requires gain d/(1-d) to recover equity (e.g. 20% drawdown needs 25% recovery). This is arithmetic, not a recovery trading instruction. Stable risk controls cannot rescue an unprofitable signal.

## Use scripts/trade_math.py

Python 3.10+; standard library only; relative examples run from this skill folder. The tool writes JSON to stdout and touches no accounts. Choose the interpreter available on the host.

```text
python scripts/trade_math.py indicators candles.csv --as-of 2026-09-30T16:02:00+05:30 --bar-minutes 5
python scripts/trade_math.py risk --side short --entry 4183.5 --stop 4188.6 --target 4180 --value-per-unit 1 --loss-cost 0.6 --win-cost 0.6 --price-basis reference --risk-cash 50 --quantity-step 1 --minimum-quantity 1
```

CSV columns: `time,open,high,low,close`. `time` is an ISO 8601 **bar opening timestamp with timezone offset** (or Z), rows strictly increasing without duplicates/overlapping bars, one instrument/feed/interval. `--as-of` is explicit and timezone-aware; rows whose close time exceeds it are excluded. The script flags gaps and stale data for the chosen time, but cannot tell market closure from missing history. Other CSV columns are ignored. It requires finite positive prices and valid OHLC.

Risk inputs: `--value-per-unit` is account-currency cash per 1.00 price change per one quantity unit; `--loss-cost`/`--win-cost` are total additional account-currency cash per unit at each exit. `--price-basis` requires the convention above. Risk budget and quantity increment/minimum must be supplied together when sizing. Output does not establish affordability, margin, guaranteed fills, or market suitability.

Missing history => null indicators and warnings, not made-up estimates. Naive dates, nonfinite prices, invalid OHLC, reversed stop/target, and inconsistent sizing arguments => an error exit. Reconcile seed/source/settings if chart indicators disagree. For accuracy-critical calculations, verify the broker convention and independently check the arithmetic before presenting it as executable.
