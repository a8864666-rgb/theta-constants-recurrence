#!/usr/bin/env python
"""Run a single theta--Carlson computation."""

from __future__ import annotations

import argparse
from mpmath import mp

from theta_carlson.core import theta_carlson_pi
from theta_carlson.correctness import tail_minus_log10


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--digits", type=int, required=True)
    parser.add_argument("--m", type=str, default="2.0")
    parser.add_argument("--mode", choices=["naive", "partial", "triple"], default="triple")
    parser.add_argument("--N", type=int, default=None)
    parser.add_argument("--validate", action="store_true")
    args = parser.parse_args()

    result = theta_carlson_pi(
        digits=args.digits,
        m=mp.mpf(args.m),
        mode=args.mode,
        N=args.N,
        validate=args.validate,
    )

    d = result.diagnostics
    print(f"digits={d.digits}")
    print(f"m={d.m}")
    print(f"N={d.N}")
    print(f"mode={d.mode}")
    print(f"work_dps={d.work_dps}")
    print(f"exp_calls={d.exp_calls}")
    print(f"tail_minus_log10={tail_minus_log10(args.m, d.N)}")
    if d.verified_digits is not None:
        print(f"verified_digits={d.verified_digits}")
    print(f"value_prefix={mp.nstr(result.value, 80)}")


if __name__ == "__main__":
    main()
