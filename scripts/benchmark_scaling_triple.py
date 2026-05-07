#!/usr/bin/env python
"""Generate high-precision scaling table for the triple-conditioned evaluator."""

from __future__ import annotations

import argparse
import csv
import time
from pathlib import Path
from mpmath import mp

from theta_carlson.core import theta_carlson_pi
from theta_carlson.correctness import tail_minus_log10


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--digits", nargs="+", type=int, required=True)
    parser.add_argument("--m", default="2.0")
    parser.add_argument("--out", default="results/results_scaling_triple.csv")
    args = parser.parse_args()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    for D in args.digits:
        t0 = time.perf_counter()
        result = theta_carlson_pi(digits=D, m=mp.mpf(args.m), mode="triple", validate=True)
        elapsed = time.perf_counter() - t0
        diag = result.diagnostics
        N = diag.N
        rows.append({
            "digits": D,
            "m": str(mp.mpf(args.m)),
            "N": N,
            "N_over_D": mp.nstr(mp.mpf(N) / D, 12),
            "N_over_sqrtD": mp.nstr(mp.mpf(N) / mp.sqrt(D), 12),
            "D_over_N": mp.nstr(mp.mpf(D) / N, 12),
            "time_seconds": f"{elapsed:.6f}",
            "exp_calls": diag.exp_calls,
            "verified_digits": diag.verified_digits,
            "tail_minus_log10": mp.nstr(tail_minus_log10(args.m, N), 12),
        })
        print(rows[-1])

    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
