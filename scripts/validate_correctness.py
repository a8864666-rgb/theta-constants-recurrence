#!/usr/bin/env python
"""Generate correctness-validation CSV files."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from theta_carlson.validation import correctness_row
from theta_carlson.core import theta_carlson_pi


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--digits", nargs="+", type=int, required=True)
    parser.add_argument("--m", default="2.0")
    parser.add_argument("--out-prefix", default="results/results_correctness")
    args = parser.parse_args()

    rows = [correctness_row(D, m=args.m) for D in args.digits]

    prefix = Path(args.out_prefix)
    write_csv(prefix.with_name(prefix.name + "_certification.csv"), rows)
    write_csv(prefix.with_name(prefix.name + "_tail_bounds.csv"), [
        {
            "digits": r["digits"],
            "m": r["m"],
            "N": r["N"],
            "tail_minus_log10": r["tail_minus_log10"],
        }
        for r in rows
    ])
    write_csv(prefix.with_name(prefix.name + "_recurrence_vs_direct.csv"), [
        {
            "digits": r["digits"],
            "m": r["m"],
            "N": r["N"],
            "delta_theta2": r["delta_theta2"],
            "delta_theta3": r["delta_theta3"],
        }
        for r in rows
    ])

    # Guard stability: rerun at the same N with more guard digits.
    guard_rows = []
    for r in rows:
        D = int(r["digits"])
        N = int(r["N"])
        base = theta_carlson_pi(D, m=args.m, N=N, guard_digits=max(50, int(0.10 * D)), validate=True)
        high = theta_carlson_pi(D, m=args.m, N=N, guard_digits=max(100, int(0.20 * D)), validate=True)
        guard_rows.append({
            "digits": D,
            "m": r["m"],
            "N": N,
            "base_verified": base.diagnostics.verified_digits,
            "high_guard_verified": high.diagnostics.verified_digits,
            "cross_stable_digits": min(base.diagnostics.verified_digits, high.diagnostics.verified_digits),
        })
    write_csv(prefix.with_name(prefix.name + "_guard_stability.csv"), guard_rows)

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
