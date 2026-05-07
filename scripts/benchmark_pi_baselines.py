#!/usr/bin/env python
"""Run transparent pi baselines."""

from __future__ import annotations

import argparse
import csv
import time
from pathlib import Path
from mpmath import mp

from theta_carlson.pi_baselines import pi_mpmath, pi_agm, pi_chudnovsky
from theta_carlson.validation import verified_digits


METHODS = {
    "mpmath": pi_mpmath,
    "agm": pi_agm,
    "chudnovsky": pi_chudnovsky,
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--digits", nargs="+", type=int, required=True)
    parser.add_argument("--mode", action="append", choices=METHODS.keys(), required=True)
    parser.add_argument("--out", default="results/results_pi_baselines.csv")
    args = parser.parse_args()

    rows = []
    for D in args.digits:
        for mode in args.mode:
            t0 = time.perf_counter()
            val = METHODS[mode](D)
            elapsed = time.perf_counter() - t0
            mp.dps = D + 50
            rows.append({
                "digits": D,
                "method": mode,
                "time_seconds": f"{elapsed:.6f}",
                "verified_digits": verified_digits(val, mp.pi),
            })
            print(rows[-1])

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
