#!/usr/bin/env python
"""Append one theta-family benchmark row to a CSV file."""

from __future__ import annotations

import argparse
import csv
import time
from pathlib import Path
from mpmath import mp

from theta_carlson.core import theta_carlson_pi


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--digits", type=int, required=True)
    parser.add_argument("--m", default="2.0")
    parser.add_argument("--mode", choices=["naive", "partial", "triple"], default="triple")
    parser.add_argument("--out", default="results/results_theta_family.csv")
    args = parser.parse_args()

    t0 = time.perf_counter()
    result = theta_carlson_pi(digits=args.digits, m=mp.mpf(args.m), mode=args.mode, validate=True)
    elapsed = time.perf_counter() - t0
    d = result.diagnostics
    row = {
        "digits": args.digits,
        "mode": args.mode,
        "m": str(mp.mpf(args.m)),
        "N": d.N,
        "time_seconds": f"{elapsed:.6f}",
        "exp_calls": d.exp_calls,
        "verified_digits": d.verified_digits,
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    write_header = not out.exists()
    with out.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(row.keys()))
        if write_header:
            writer.writeheader()
        writer.writerow(row)
    print(row)


if __name__ == "__main__":
    main()
