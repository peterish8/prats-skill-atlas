"""Meaningful arithmetic/data-boundary checks; no market-performance claim."""

import csv
import math
import tempfile
from datetime import timedelta
from decimal import Decimal
from pathlib import Path

from trade_math import ema, indicators, read_bars, risk, timestamp


def rejected(operation):
    try:
        operation()
    except ValueError:
        return
    raise AssertionError("Expected invalid input to be rejected")


def run():
    start = timestamp("2026-09-30T10:00:00+05:30")
    bars = []
    for index, close in enumerate([100, 101, 99, 102, 101]):
        bars.append(dict(time=start + timedelta(minutes=5 * index),
                         open=close, high=close + 1, low=close - 1, close=close))
    snapshot = indicators(bars, start + timedelta(minutes=23), 5, 3)
    assert snapshot["completed_bars"] == 4
    assert snapshot["excluded_unclosed_or_future_bars"] == 1
    assert math.isclose(snapshot["rsi"], 100 * 2 / 3)
    assert math.isclose(snapshot["atr"], 26 / 9)
    full = indicators(bars, start + timedelta(minutes=25), 5, 3)
    assert math.isclose(full["rsi"], 100 * 8 / 15)
    assert ema([1, 2, 3, 4], 3) == 3
    assert ema([1, 2], 3) is None

    gap_bars = [dict(time=start, open=100, high=101, low=99, close=100),
                dict(time=start + timedelta(minutes=5), open=110, high=111, low=109, close=110)]
    assert indicators(gap_bars, start + timedelta(minutes=10), 5, 2)["atr"] == 6.5
    flat = [dict(time=start + timedelta(minutes=5*i), open=100, high=100, low=100, close=100)
            for i in range(16)]
    flat_result = indicators(flat, start + timedelta(minutes=80), 5)
    assert flat_result["rsi"] is None and flat_result["atr"] == 0
    assert flat_result["candle"]["close_location"] is None

    short = risk("short", "4183.5", "4188.6", "4180", "1", ".6", ".6",
                 "reference", "50", "1", "1")
    assert short["net_loss_per_unit"] == Decimal("5.7")
    assert short["net_profit_per_unit"] == Decimal("2.9")
    assert short["quantity"] == 8 and short["planned_loss"] == Decimal("45.6")
    assert short["gross_reward_risk"] < 1
    assert short["net_reward_risk"] < short["gross_reward_risk"]
    assert math.isclose(float(short["break_even_win_rate"]), 5.7 / 8.6)
    long = risk("long", "100.2", "98", "105", "1", "0", "0", "executable")
    assert long["net_loss_per_unit"] == Decimal("2.2")
    assert long["net_profit_per_unit"] == Decimal("4.8")
    precision = risk("long", "100", "99", "103", "1", "0", "0",
                     "reference", "0.3", "0.1", "0.1")
    assert precision["quantity"] == Decimal("0.3")
    too_small = risk("long", "100", "99", "103", "1", "0", "0",
                     "reference", ".05", ".1", ".1")
    assert too_small["quantity"] is None
    costs_exceed_gain = risk("long", "100", "99", "101", "1", "0", "2", "reference")
    assert not costs_exceed_gain["target_profitable_after_costs"]
    assert costs_exceed_gain["break_even_win_rate"] is None

    rejected(lambda: timestamp("2026-09-30T10:00:00"))
    rejected(lambda: timestamp(None))
    rejected(lambda: indicators(bars, start, 5))
    rejected(lambda: indicators(bars, start + timedelta(hours=1), 15))
    rejected(lambda: risk("short", "100", "99", "95", "1", "0", "0", "reference"))
    rejected(lambda: risk("long", "NaN", "99", "103", "1", "0", "0", "reference"))
    rejected(lambda: risk("long", "100", "99", "103", "1", "0", "0", "reference", "50"))

    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "bars.csv"
        def write(rows):
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(["time", "open", "high", "low", "close"])
                writer.writerows(rows)
        write([["2026-09-30T10:00:00+05:30", 100, 101, 99, 100]])
        assert len(read_bars(path)) == 1
        write([["2026-09-30T10:00:00+05:30", 100, 99, 98, 100]])
        rejected(lambda: read_bars(path))
        write([["2026-09-30T10:00:00+05:30", 100, "inf", 99, 100]])
        rejected(lambda: read_bars(path))
        write([["2026-09-30T10:00:00+05:30", 100, 101, 99, 100]] * 2)
        rejected(lambda: read_bars(path))
    print("PASS: closed-bar exclusion, Wilder ATR/RSI, EMA seed, gap true range, flat bars,")
    print("cost-aware long/short payoff, exact sizing floor, minimum size, and invalid-input rejection.")
    print("These checks validate arithmetic and boundaries, not trading profitability.")


if __name__ == "__main__":
    run()
