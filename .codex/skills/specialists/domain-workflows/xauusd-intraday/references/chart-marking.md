# TradingView marking workflow

Use the host's browser/computer-use tool and its current documentation. Do not hardcode viewport coordinates or rely on private undocumented TradingView internals. If the separate installed tradingview-chart-markup skill is available, follow it for UI mechanics; these instructions are self-contained for other environments.

## Exact candle high/low

1. Read the live screenshot, symbol, interval, and target timestamp. Match the marked candle to the live chart; historical comment coordinates may have shifted.
2. Hover/select the target and read exact H and L in the header/data window. Check that the hovered timestamp is correct. A forming candle's current extreme may change; tell the user if marking that one.
3. Choose Horizontal Line (Alt+H where supported). Open the new drawing's settings, Coordinates, and type the exact price. Repeat for the other extreme.
4. Verify labels and geometry from a fresh screenshot, save the layout with TradingView's save control, and verify saved state. Don't claim an actual order or alert exists because a drawing exists.

## Trendline/ray/channel

Read each requested anchor's time and exact price before placement. For a simple connection use Trend Line or Ray as requested; for Parallel Channel set the two baseline anchors on the specified points, then a third point for width. The user may say "touch these lows and extend right"; the baseline must touch those wick lows, not candle bodies. If channel width is unspecified, derive a clearly described opposite swing boundary or ask if no sensible width exists.

Use drawing settings to set prices/times accurately where supported. For a requested right extension, use the relevant extension setting; Parallel Channel commonly offers Style -> Extend -> Extend right line. Inspect actual UI labels because TradingView changes.

Keep the user's existing drawings. Undo only your incorrect new drawing; never undo prior user actions or clear the whole chart. Preserve original interval/viewport after analytical inspection where possible. Use consistent unobtrusive labels (support/resistance, entry hypothesis, invalidation, target) when asked to annotate a plan. A long/short position drawing is a visual risk model [E02], not a filled trade. Create alerts only if explicitly requested.
