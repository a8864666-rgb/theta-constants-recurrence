"""Validation helpers."""

from __future__ import annotations

from mpmath import mp

from .theta import theta_sums
from .correctness import tail_minus_log10


def verified_digits(x, ref=None) -> int:
    """Estimate matching decimal digits against a reference value."""
    if ref is None:
        ref = mp.pi
    err = abs(mp.mpf(x) - mp.mpf(ref))
    if err == 0:
        return max(0, mp.dps - 1)
    return max(0, int(mp.floor(-mp.log10(err))))


def recurrence_vs_direct(m, N: int):
    """Compare recurrence-generated theta sums against direct exponentials."""
    triple = theta_sums(m=m, N=N, mode="triple")
    direct = theta_sums(m=m, N=N, mode="partial")
    return {
        "delta_theta2": abs(triple.theta2 - direct.theta2),
        "delta_theta3": abs(triple.theta3 - direct.theta3),
    }


def correctness_row(digits: int, m=2, N: int | None = None):
    """Generate a correctness-validation row."""
    from .core import theta_carlson_pi, plan_truncation_depth, default_guard_digits

    guard = default_guard_digits(digits)
    if N is None:
        N = plan_truncation_depth(digits, m=m, guard_digits=guard)
    mp.dps = digits + guard + 50
    result = theta_carlson_pi(digits=digits, m=m, N=N, mode="triple", guard_digits=guard, validate=True)
    deltas = recurrence_vs_direct(m=m, N=N)
    return {
        "digits": digits,
        "m": str(mp.mpf(m)),
        "N": N,
        "tail_minus_log10": str(tail_minus_log10(m=m, N=N)),
        "delta_theta2": str(deltas["delta_theta2"]),
        "delta_theta3": str(deltas["delta_theta3"]),
        "verified_digits": result.diagnostics.verified_digits,
    }
