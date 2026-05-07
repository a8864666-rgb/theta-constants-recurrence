"""Theta-sum generation for the theta--Carlson evaluator."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from mpmath import mp

from .summation import sum_values


ThetaMode = Literal["naive", "partial", "triple"]


@dataclass
class ThetaDiagnostics:
    mode: str
    N: int
    m: str
    exp_calls: int
    summation: str


@dataclass
class ThetaResult:
    theta2: object
    theta3: object
    diagnostics: ThetaDiagnostics


def _direct_terms(m, N: int):
    """Generate theta terms using direct high-precision exponentials."""
    terms3 = [mp.e ** (-m * (n * n)) for n in range(1, N + 1)]
    terms2 = [mp.e ** (-m * ((n + mp.mpf("0.5")) ** 2)) for n in range(0, N + 1)]
    exp_calls = N + (N + 1)
    return terms2, terms3, exp_calls


def _recurrence_terms(m, N: int):
    """Generate theta terms using recurrence acceleration.

    The recurrence uses:
      a_{n+1} = a_n r^(2n+1)
      b_{n+1} = b_n r^(2n+2)
    with the ratio factors updated by multiplication by r^2.
    """
    r = mp.e ** (-m)
    r2 = r * r
    b = mp.e ** (-m / 4)

    # theta3 terms a_1, ..., a_N
    a = mp.mpf(1)
    u = r
    terms3 = []
    for _ in range(N):
        a = a * u
        terms3.append(a)
        u = u * r2

    # theta2 terms b_0, ..., b_N
    v = r2
    terms2 = [b]
    for _ in range(N):
        b = b * v
        terms2.append(b)
        v = v * r2

    exp_calls = 2
    return terms2, terms3, exp_calls


def theta_sums(m, N: int, mode: ThetaMode = "triple", summation: str | None = None) -> ThetaResult:
    """Evaluate truncated theta2 and theta3 sums.

    Parameters
    ----------
    m:
        Positive spectral parameter. The nome is q = exp(-m).
    N:
        Truncation depth.
    mode:
        "naive": direct exponentials and sequential summation.
        "partial": direct exponentials and pairwise summation.
        "triple": recurrence-generated terms and pairwise summation.
    summation:
        Optional override for summation mode.
    """
    m = mp.mpf(m)
    if N < 0:
        raise ValueError("N must be nonnegative")
    if m <= 0:
        raise ValueError("m must be positive")

    if mode == "naive":
        terms2, terms3, exp_calls = _direct_terms(m, N)
        default_summation = "sequential"
    elif mode == "partial":
        terms2, terms3, exp_calls = _direct_terms(m, N)
        default_summation = "pairwise"
    elif mode == "triple":
        terms2, terms3, exp_calls = _recurrence_terms(m, N)
        default_summation = "pairwise"
    else:
        raise ValueError(f"unknown mode: {mode}")

    summation = summation or default_summation
    theta3 = mp.mpf(1) + 2 * sum_values(terms3, summation)
    theta2 = 2 * sum_values(terms2, summation)

    return ThetaResult(
        theta2=theta2,
        theta3=theta3,
        diagnostics=ThetaDiagnostics(
            mode=mode,
            N=N,
            m=str(m),
            exp_calls=exp_calls,
            summation=summation,
        ),
    )
