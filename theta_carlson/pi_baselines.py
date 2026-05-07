"""Transparent pi-computation baselines for scope comparison."""

from __future__ import annotations

from mpmath import mp


def pi_mpmath(digits: int):
    old = mp.dps
    mp.dps = digits + 25
    try:
        return +mp.pi
    finally:
        mp.dps = old


def pi_agm(digits: int):
    """Gauss--Legendre / AGM-style pi computation."""
    old = mp.dps
    mp.dps = digits + 25
    try:
        a = mp.mpf(1)
        b = 1 / mp.sqrt(2)
        t = mp.mpf(1) / 4
        p = mp.mpf(1)
        for _ in range(int(mp.ceil(mp.log(digits, 2))) + 3):
            an = (a + b) / 2
            b = mp.sqrt(a * b)
            t = t - p * (a - an) ** 2
            a = an
            p *= 2
        return (a + b) ** 2 / (4 * t)
    finally:
        mp.dps = old


def pi_chudnovsky(digits: int):
    """Simple transparent Chudnovsky implementation.

    This is included for scope comparison only, not as an optimized baseline.
    """
    old = mp.dps
    mp.dps = digits + 25
    try:
        C = 426880 * mp.sqrt(10005)
        total = mp.mpf(0)
        # About 14 digits per term; add guard terms.
        terms = int(mp.ceil(digits / 14)) + 3
        for k in range(terms):
            num = mp.factorial(6 * k) * (13591409 + 545140134 * k)
            den = mp.factorial(3 * k) * (mp.factorial(k) ** 3) * ((-640320) ** (3 * k))
            total += num / den
        return C / total
    finally:
        mp.dps = old
