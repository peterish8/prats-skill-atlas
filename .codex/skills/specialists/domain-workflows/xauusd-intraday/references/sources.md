# Source register and research limits

Reviewed on 2026-09-30. This folder contains original synthesis and short research notes, not reproduced books. Two legal publisher excerpts were accessible; several other books were represented only by publisher descriptions or chapter summaries. No full-book reading or ten years of practice is claimed. Publication scope matters: none of the reviewed material validates this specific OANDA 5-minute strategy. The playbook's combined rules are our testable synthesis, not a named author's certified method.

## Books: what was actually reviewed

| ID | Work and direct source | Access reviewed | Useful contribution / limit |
|---|---|---|---|
| B01 | Adam Grimes, *The Art and Science of Technical Analysis* (2012), [Wiley chapter excerpt](https://catalogimages.wiley.com/images/db/pdf/9781118115121.excerpt.pdf) | Selected sections of the 30-page publisher excerpt: The Trader's Edge, expectancy, randomness/costs, and multiple timeframes | An edge needs positive expectancy after friction. Bar patterns belong in structure and timeframe context; discipline alone does not create an edge. Full book not reviewed. |
| B02 | Al Brooks, *Trading Price Action Trends* (2012), [Wiley excerpt](https://catalogimages.wiley.com/images/db/pdf/9781118066515.excerpt.pdf), [chapter summary](https://onlinelibrary.wiley.com/doi/10.1002/9781119202592.ch1) | Selected sections of 24-page excerpt and official chapter summary | Trend versus range changes entry logic; candle appearance can reverse before close. Examples use other instruments and don't establish gold win rates. Full trilogy not reviewed. |
| B03 | David R. Aronson, *Evidence-Based Technical Analysis* (2006/2007), [Wiley book contents](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118268315), [Objective Rules chapter summary](https://onlinelibrary.wiley.com/doi/10.1002/9781118268315.ch1) | Publisher description, contents, and public chapter summaries; full chapters unavailable | Motivates objective rules, benchmarks, look-ahead/cost checks, and scrutiny of data-mined signals. Do not claim to have read its experiments or adopt unaccessed details. |
| B04 | John J. Murphy, *Technical Analysis of the Financial Markets* (1999), [publisher](https://www.penguinrandomhouse.com/books/350647/technical-analysis-of-the-financial-markets-by-john-j-murphy/) | Publisher description and bibliographic data | Broad chart/indicator/intermarket reading reference. Detailed operational rules here are supported by accessible documentation and original synthesis, not inaccessible book pages. |
| B05 | Steve Nison, *Japanese Candlestick Charting Techniques*, revised edition (2001), [publisher](https://www.penguinrandomhouse.com/books/350650/japanese-candlestick-charting-techniques-by-steve-nison/) | Publisher description | Candlestick study combined with Western analysis and capital preservation. Publisher claims are not statistical evidence of a candle strategy. Full text not reviewed. |
| B06 | Mark Douglas, *Trading in the Zone* (2001), [publisher](https://www.penguinrandomhouse.com/books/350665/trading-in-the-zone-by-mark-douglas/) | Publisher description | Probability/risk mindset as a reading theme. Psychology does not establish the setup's expectancy. Full text not reviewed. |

## Empirical research

| ID | Source | Reviewed material / decision impact |
|---|---|---|
| R01 | Lo, Mamaysky & Wang (2000), [Foundations of Technical Analysis, NBER](https://www.nber.org/papers/w7613) | Abstract: some systematically defined indicators contained incremental information in historical US daily stocks. This is neither a demonstrated implementable profit after costs nor evidence for 5-minute gold. |
| R02 | Tharavanij, Siraprapasiri & Rajchamaha (2017), [Profitability of Candlestick Charting Patterns in the Stock Exchange of Thailand](https://journals.sagepub.com/doi/10.1177/2158244017736799) | Abstract and selected introduction/literature sections: daily SET50 constituents, 2006-2016; most reversal rules lacked reliable direction/profitability, and the examined filters generally did not fix it. Literature is mixed. Do not extrapolate this as proof that every price-action rule fails everywhere. |
| R03 | Carol Osler (2001), [Currency Orders and Exchange-Rate Dynamics, NY Fed SR125](https://www.newyorkfed.org/research/staff_reports/sr125.html) | Public research summary: clustered take-profit and stop-loss orders provide a currency-market explanation for reactions and acceleration around levels. Gold transfer is a hypothesis; actual current order locations are unknown. |
| R04 | Carol Osler (2002), [Stop-Loss Orders and Price Cascades, NY Fed SR150](https://www.newyorkfed.org/research/staff_reports/sr150.html) | Public summary: documented currency stop clusters can intensify high-frequency moves. Supports planning for adverse fills, not assertions of deliberate stop hunting. |
| R05 | Bailey, Borwein, Lopez de Prado & Zhu (2015 preprint; journal 2017), [The Probability of Backtest Overfitting](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf), [university publication record](https://scholarworks.wmich.edu/math_pubs/42/) | Abstract and selected introduction/method overview/conclusion material. Strategy selection from many trials can inflate apparent performance; a simple holdout is not sufficient protection in all investment backtests. CSCV is an advanced assessment method, not performed by this skill. |

## Practitioner and gold context

| ID | Source | Reviewed material / decision impact |
|---|---|---|
| A01 | Adam Grimes, [Elementary Market Structure](https://www.adamhgrimes.com/market-structure/) | Public article: swing hierarchy and the later information required to confirm pivots. Prevents hindsight-based entry claims. |
| A02 | Adam Grimes, [The Art and Science: A Deeper Look](https://www.adamhgrimes.com/the-art-and-science-a-deeper-look-12/) | Author's chapter overview: precision, randomness, and four broad technical trade categories. Supplementary explanation rather than empirical validation. |
| M01 | World Gold Council (2021), [Short-term gold performance model](https://www.gold.org/goldhub/gold-focus/2021/06/short-term-gold-performance-model-how-it-works-and-why-it-matters) | Article's methodology discussion: multiple macro/flow variables and changing sensitivities. Model uses monthly and weekly horizons; its name does not imply a 5-minute forecasting model. |
| M02 | World Gold Council (2018), [Gold tracks the dollar as rates take a back seat](https://www.gold.org/goldhub/research/investment-update-gold-tracks-dollar-rates-take-back-seat) | Historical analysis illustrates changing gold/dollar/rate relationships. Use it to avoid universal "dollar up => gold down" rules, not as today's outlook. |

Current USD, real/nominal yields, positioning, and geopolitical news can add context when synchronized and available; don't fetch monthly/daily values and misrepresent them as contemporaneous 5-minute triggers. World Gold Council is a gold industry organization; CME and brokers/platforms also have commercial interests. Their descriptions are useful with that perspective and empirical cross-checks.

## Indicators, execution, and planning

| ID | Direct primary reference | What the skill uses |
|---|---|---|
| T01 | TradingView, [Average True Range](https://www.tradingview.com/support/solutions/43000501823-average-true-range-atr/) | True-range definition, RMA default, volatility rather than directional prediction. |
| T02 | TradingView, [Relative Strength Index](https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/) | Wilder gain/loss smoothing, RSI definition, limitations of isolated interpretations. |
| T03 | TradingView, [Moving Averages](https://www.tradingview.com/support/solutions/43000502589-moving-averages/) | Moving averages react to historical price; configuration and lag matter. |
| T04 | TradingView, [Volume Weighted Average Price](https://www.tradingview.com/support/solutions/43000502018-volume-weighted-average-price-vwap/) | Typical-price bar formula, anchor/reset, lag, completed higher-timeframe settings. |
| T05 | TradingView, [Missing or tick volume](https://www.tradingview.com/support/solutions/43000481397-the-volume-indicator-on-my-chart-looks-odd-or-displays-zero-or-n-a-values/) | Volume depends on provider; tick volume can mean price-update counts. Verify actual feed. |
| E01 | TradingView, [Stop-market orders](https://www.tradingview.com/support/solutions/43000754944-mastering-stop-market-orders/) | Stops become market orders; specified stop price is not a guaranteed fill. |
| E02 | TradingView, [Long/short position drawing tools](https://www.tradingview.com/support/solutions/43000475660-how-to-use-long-and-short-position-drawing-tools/) | Visualized risk, position/contract inputs, and distinction between drawings/practice and orders. |
| P01 | CME, [Risk Management and Your Trade Plan](https://www.cmegroup.com/education/courses/building-a-trade-plan/risk-management-and-your-trade-plan) | Explicit leverage, maximum trade/day loss, account exposure; illustrative CME risk percentages are not this user's recommendation. |
| P02 | CME, [Position and Risk Management](https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/position-and-risk-management) | Contract/tick values and size change financial exposure. Futures details cannot be assumed for spot/CFD units. |
| P03 | CME, [Building a Trade Plan](https://www.cmegroup.com/education/courses/building-a-trade-plan) | Objectives, methodology, strategy, risk, and logs belong together; a plan doesn't guarantee money. |

## Live event lookup locations

| ID | Official source | Use at invocation time |
|---|---|---|
| C01 | [BLS release calendar](https://www.bls.gov/schedule/) | CPI/PPI/jobs and relevant releases; read the current dated schedule. Calendar times are US Eastern; convert for the actual date. |
| C02 | [BEA release schedule](https://www.bea.gov/news/schedule) | Personal Income and Outlays/PCE, GDP, and other releases. Dynamic content may require browser viewing; inability to read it isn't proof of no event. |
| C03 | [Federal Reserve FOMC calendars](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) | Current meeting dates, statements/minutes, linked press conferences; inspect exact announcement times and include material unscheduled news. |

The static source register is not a checked live news calendar. It was created on the date above. Refresh current schedules, execution details, and source access before using them in a live scenario. Consult actual broker specifications for the user's entity; no fixed gold lot/pip/session table is embedded.

## How to extend the research

Prefer author/publisher-hosted previews and primary research; don't download pirated full books or claim inaccessible material was read. Record source, publication date, market/sample/timeframe, what was accessed, conflicts, and the change it supports. Convert marketing claims into questions to test. Keep source-specific paraphrases short, original, and within applicable quotation/summarization limits. New indicators or attractive examples do not automatically justify new strategy rules.
