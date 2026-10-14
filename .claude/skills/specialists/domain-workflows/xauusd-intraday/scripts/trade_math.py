"""Offline gold-chart measurements and explicit, cost-aware trade arithmetic.

No network, orders, accounts, signals, or volume assumptions. Python 3.10+.
"""

import argparse
import csv
import json
import math
from datetime import datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation, ROUND_FLOOR
from pathlib import Path


def timestamp(value):
    if not isinstance(value, str):
        raise ValueError("Timestamp must be an ISO 8601 string with timezone")
    stamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if stamp.tzinfo is None or stamp.utcoffset() is None:
        raise ValueError("Timestamps require an explicit timezone offset or Z")
    return stamp.astimezone(timezone.utc)


def number(value):
    result = float(value)
    if not math.isfinite(result) or result <= 0:
        raise ValueError("OHLC prices must be finite and positive")
    return result


def dec(value, *, positive=False):
    result = Decimal(str(value))
    if not result.is_finite() or (result <= 0 if positive else result < 0):
        raise ValueError("Expected a finite positive value" if positive else
                         "Expected a finite nonnegative value")
    return result


def read_bars(path):
    bars = []
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"time", "open", "high", "low", "close"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("CSV requires time,open,high,low,close columns")
        for line, row in enumerate(reader, start=2):
            try:
                bar = {key: number(row[key]) for key in required - {"time"}}
                bar["time"] = timestamp(row["time"])
                if (bar["low"] > min(bar["open"], bar["close"]) or
                        bar["high"] < max(bar["open"], bar["close"]) or
                        bar["low"] > bar["high"]):
                    raise ValueError("Invalid OHLC bounds")
                if bars and bar["time"] <= bars[-1]["time"]:
                    raise ValueError("Bar timestamps must be strictly increasing")
            except (ValueError, TypeError, KeyError) as exc:
                raise ValueError(f"CSV line {line}: {exc}") from exc
            bars.append(bar)
    if not bars:
        raise ValueError("CSV has no bars")
    return bars


def wilder(values, period):
    if len(values) < period:
        return None
    average = sum(values[:period]) / period
    for value in values[period:]:
        average = (average * (period - 1) + value) / period
    return average


def ema(values, period):
    if len(values) < period:
        return None
    average = sum(values[:period]) / period
    alpha = 2 / (period + 1)
    for value in values[period:]:
        average = alpha * value + (1 - alpha) * average
    return average


def indicators(bars, as_of, bar_minutes, period=14):
    if bar_minutes <= 0 or period < 2:
        raise ValueError("Bar minutes must be positive and period at least 2")
    duration = timedelta(minutes=bar_minutes)
    for previous, current in zip(bars, bars[1:]):
        if current["time"] - previous["time"] < duration:
            raise ValueError("Overlapping bars or wrong --bar-minutes")
    closed = [bar for bar in bars if bar["time"] + duration <= as_of]
    if not closed:
        raise ValueError("No completed bars at the supplied as-of time")
    warnings = []
    gap_count = sum(current["time"] - previous["time"] > duration
                    for previous, current in zip(closed, closed[1:]))
    if gap_count:
        warnings.append("Gaps detected; distinguish market breaks from missing data")
    last = closed[-1]
    age = (as_of - (last["time"] + duration)).total_seconds()
    if age >= duration.total_seconds():
        warnings.append("Latest completed bar is at least one full bar old")
    if len(closed) < 250:
        warnings.append("Limited warmup; seeded indicators may differ from chart history")
    closes = [bar["close"] for bar in closed]
    changes = [current - previous for previous, current in zip(closes, closes[1:])]
    gains = [max(change, 0) for change in changes]
    losses = [max(-change, 0) for change in changes]
    avg_gain, avg_loss = wilder(gains, period), wilder(losses, period)
    rsi = None
    if avg_gain is not None:
        if avg_loss == 0:
            rsi = 100.0 if avg_gain > 0 else None
        else:
            rsi = 100 - 100 / (1 + avg_gain / avg_loss)
    if avg_gain is not None and avg_gain == avg_loss == 0:
        warnings.append("RSI undefined for entirely flat close changes")
    tr = []
    for index, bar in enumerate(closed):
        previous_close = closed[index - 1]["close"] if index else bar["close"]
        tr.append(max(bar["high"] - bar["low"],
                      abs(bar["high"] - previous_close),
                      abs(bar["low"] - previous_close)))
    span = last["high"] - last["low"]
    body = abs(last["close"] - last["open"])
    result = {
        "as_of_utc": as_of.isoformat(),
        "bar_minutes": bar_minutes,
        "completed_bars": len(closed),
        "excluded_unclosed_or_future_bars": len(bars) - len(closed),
        "gap_count": gap_count,
        "last_completed_open_utc": last["time"].isoformat(),
        "last_completed_close_utc": (last["time"] + duration).isoformat(),
        "age_since_close_seconds": age,
        "ohlc": {key: last[key] for key in ("open", "high", "low", "close")},
        "candle": {
            "range": span,
            "body": body,
            "upper_wick": last["high"] - max(last["open"], last["close"]),
            "lower_wick": min(last["open"], last["close"]) - last["low"],
            "body_fraction": body / span if span else None,
            "close_location": (last["close"] - last["low"]) / span if span else None,
        },
        "atr": wilder(tr, period),
        "rsi": rsi,
        "period": period,
        "ema20": ema(closes, 20),
        "ema50": ema(closes, 50),
        "seed_conventions": "ATR first TR uses H-L; Wilder SMA seed; EMA SMA seed",
        "warnings": warnings,
    }
    if any(result[key] is None for key in ("atr", "rsi", "ema20", "ema50")):
        warnings.append("Some indicators unavailable: inspect history or flat-RSI condition")
    return result


def risk(side, entry, stop, target, value_per_unit, loss_cost, win_cost,
         price_basis, risk_cash=None, quantity_step=None, minimum_quantity=None):
    if side not in {"long", "short"}:
        raise ValueError("Side must be long or short")
    if price_basis not in {"reference", "executable"}:
        raise ValueError("Choose reference or executable price basis")
    entry, stop, target, value = [dec(value, positive=True)
                                 for value in (entry, stop, target, value_per_unit)]
    loss_cost, win_cost = dec(loss_cost), dec(win_cost)
    direction = Decimal(1) if side == "long" else Decimal(-1)
    distance = direction * (entry - stop)
    gain = direction * (target - entry)
    if distance <= 0 or gain <= 0:
        raise ValueError("Stop and target must be on the correct sides of entry")
    gross_loss, gross_profit = distance * value, gain * value
    net_loss, net_profit = gross_loss + loss_cost, gross_profit - win_cost
    result = {
        "side": side, "price_basis": price_basis,
        "entry": entry, "stop": stop, "target": target,
        "stop_distance": distance, "target_distance": gain,
        "gross_loss_per_unit": gross_loss, "gross_profit_per_unit": gross_profit,
        "loss_cost_per_unit": loss_cost, "win_cost_per_unit": win_cost,
        "net_loss_per_unit": net_loss, "net_profit_per_unit": net_profit,
        "gross_reward_risk": gross_profit / gross_loss,
        "net_reward_risk": net_profit / net_loss,
        "break_even_win_rate": net_loss / (net_loss + net_profit) if net_profit > 0 else None,
        "target_profitable_after_costs": net_profit > 0,
        "execution_note": "Costs are additional to provided fills; do not double-charge spread",
        "quantity": None,
    }
    sizing = (risk_cash, quantity_step, minimum_quantity)
    if any(value is not None for value in sizing):
        if not all(value is not None for value in sizing):
            raise ValueError("Sizing requires risk cash, quantity step, and minimum quantity")
        budget, step, minimum = [dec(value, positive=True) for value in sizing]
        quantity = ((budget / net_loss) / step).to_integral_value(rounding=ROUND_FLOOR) * step
        can_size = quantity >= minimum and net_profit > 0
        result.update({
            "risk_cash": budget,
            "quantity_step": step,
            "minimum_quantity": minimum,
            "raw_quantity": budget / net_loss,
            "quantity": quantity if can_size else None,
            "within_minimum_and_profitable_target": can_size,
            "planned_loss": quantity * net_loss if can_size else None,
            "planned_profit": quantity * net_profit if can_size else None,
            "margin_check": "Not performed; verify broker and account limits separately",
        })
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    ind = commands.add_parser("indicators")
    ind.add_argument("csv_path")
    ind.add_argument("--as-of", required=True)
    ind.add_argument("--bar-minutes", type=int, required=True)
    ind.add_argument("--period", type=int, default=14)
    trade = commands.add_parser("risk")
    trade.add_argument("--side", choices=("long", "short"), required=True)
    for name in ("entry", "stop", "target", "value-per-unit", "loss-cost", "win-cost"):
        trade.add_argument("--" + name, required=True)
    trade.add_argument("--price-basis", choices=("reference", "executable"), required=True)
    for name in ("risk-cash", "quantity-step", "minimum-quantity"):
        trade.add_argument("--" + name)
    args = parser.parse_args()
    try:
        if args.command == "indicators":
            result = indicators(read_bars(args.csv_path), timestamp(args.as_of),
                                args.bar_minutes, args.period)
        else:
            values = vars(args).copy()
            values.pop("command")
            result = risk(**values)
        print(json.dumps(result, indent=2, allow_nan=False,
                         default=lambda value: str(value) if isinstance(value, Decimal) else value))
    except (ValueError, TypeError, InvalidOperation, OSError) as exc:
        parser.exit(2, f"Error: {exc}\n")


if __name__ == "__main__":
    main()
