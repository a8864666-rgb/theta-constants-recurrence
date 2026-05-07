"""Correctness diagnostics for theta--Carlson evaluation."""

from __future__ import annotations

from mpmath import mp


def tail_bounds(m, N: int):
    """Return theta2 tail bound, theta3 tail bound, and combined bound."""
    m = mp.mpf(m)
    N = int(N)
    r3 = (2 * mp.e ** (-m * (N + 1) ** 2)) / (1 - mp.e ** (-m * (2 * N + 3)))
    r2 = (2 * mp.e ** (-m * (N + mp.mpf("1.5")) ** 2)) / (1 - mp.e ** (-m * (2 * N + 4)))
    return r2, r3, r2 + r3


def tail_minus_log10(m, N: int):
    """Return -log10(combined tail bound)."""
    _, _, total = tail_bounds(m, N)
    return -mp.log10(total)
