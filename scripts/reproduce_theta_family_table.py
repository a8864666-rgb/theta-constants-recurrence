#!/usr/bin/env python
"""Reproduce theta-family ablation table: naive, partial, and triple."""

from __future__ import annotations

import argparse
import csv
import time
from pathlib import Path
from mpmath import mp

from theta_carlson.core import theta_carlson_pi


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--digits", nargs="+", type=int, required=True)
    parser.add_argument("--m", default="2.0")
    parser.add_argument("--out", default="results/results_theta_family.csv")
    args = parser.parse_args()

    rows = []
    for D in args.digits:
        for mode in ["naive", "partial", "triple"]:
            t0 = time.perf_counter()
            result = theta_carlson_pi(digits=D, m=mp.mpf(args.m), mode=mode, validate=True)
            elapsed = time.perf_counter() - t0
            d = result.diagnostics
            row = {
                "digits": D,
                "mode": mode,
                "m": str(mp.mpf(args.m)),
                "N": d.N,
                "time_seconds": f"{elapsed:.6f}",
                "exp_calls": d.exp_calls,
                "verified_digits": d.verified_digits,
            }
            rows.append(row)
            print(row)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
