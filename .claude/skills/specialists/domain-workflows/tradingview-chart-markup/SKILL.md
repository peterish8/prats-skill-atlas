---
name: tradingview-chart-markup
description: Use when the user asks to mark candle highs or lows, connect chart points, draw a parallel channel, or extend a line on TradingView, including quick requests like "do the same" or "mark this one."
---

# TradingView Chart Markup

Use the open TradingView chart to add only the annotations the user requested, then save the layout.

## Mark a candle's high and low

1. Match the user's highlighted candle to the live chart. Check the current screenshot and chart interval first; comment screenshots can be stale or the chart can have moved.
2. Select or hover the candle and read its exact `H` and `L` from the chart's OHLC status line or accessibility text. Confirm the selected timestamp/candle matches the highlight.
3. Add a horizontal line with TradingView's horizontal-line shortcut (`Alt+H`). Open that line's settings, go to **Coordinates**, and set its price to the exact high. Repeat for the low. Avoid placing precision levels by pixel approximation.
4. Save with **Save all charts for all symbols and intervals on your layout**, and visually verify both price labels and lines.

## Connect points or draw a parallel channel

- For a simple connection, use a trendline or ray that touches both requested points. Turn on the right extension when the user asks to extend it.
- When the user specifies a parallel channel or selects that tool in the floating drawing toolbar, use **Parallel Channel**. Place its baseline anchors on the requested points. A channel needs a third point to set its width; choose an offset that follows the visible swing structure when the user has not specified a width.
- If the user asks to extend the channel, open its settings, choose **Style → Extend → Extend right line**, apply the setting, and save the layout.
- Keep existing annotations. If a drawing lands at the wrong point, undo only that newly created drawing before retrying.

## Operating constraints

- Use browser UI automation on the user's open TradingView page. Re-check the live screenshot before using coordinates; derive anchors from the current chart, not from stale pixel positions.
- Do not place or modify orders. Chart drawings and layout saves are the scope of this skill.
- After acting, verify the requested geometry is visible and the layout is saved. If the target candle or point cannot be matched confidently, ask one concise clarification instead of drawing on a different bar.
