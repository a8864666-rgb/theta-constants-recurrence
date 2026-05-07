"""End-to-end theta--Carlson evaluation."""

from __future__ import annotations

from dataclasses import dataclass

from mpmath import mp

from .theta import theta_sums


@dataclass
class PiDiagnostics:
    digits: int
    guard_digits: int
    work_dps: int
    m: str
    N: int
    mode: str
    exp_calls: int
    verified_digits: int | None = None
    tail_minus_log10: str | None = None


@dataclass
class PiResult:
    value: object
    diagnostics: PiDiagnostics


def default_guard_digits(digits: int) -> int:
    """Default guard policy used in the paper's reference artifact."""
    return max(50, int(mp.ceil(mp.mpf("0.10") * digits)))


def plan_truncation_depth(digits: int, m=mp.mpf(2), guard_digits: int | None = None) -> int:
    """Plan truncation depth from the Gaussian-tail rule."""
    if digits <= 0:
        raise ValueError("digits must be positive")
    m = mp.mpf(m)
    if m <= 0:
        raise ValueError("m must be positive")
    if guard_digits is None:
        guard_digits = default_guard_digits(digits)
    N = mp.ceil(mp.sqrt(((digits + guard_digits) * mp.log(10)) / m) - 1)
    return int(max(0, N))


def theta_carlson_pi(
    digits: int,
    m=mp.mpf(2),
    mode: str = "triple",
    N: int | None = None,
    guard_digits: int | None = None,
    validate: bool = False,
) -> PiResult:
    """Compute pi through the theta--Carlson pipeline.

    This is a transparent reference implementation. It is not intended to
    compete with dedicated pi engines.
    """
    if guard_digits is None:
        guard_digits = default_guard_digits(digits)
    work_dps = digits + guard_digits + 25
    old_dps = mp.dps
    mp.dps = work_dps
    try:
        m = mp.mpf(m)
        if N is None:
            N = plan_truncation_depth(digits, m=m, guard_digits=guard_digits)

        theta = theta_sums(m=m, N=N, mode=mode)
        theta2 = theta.theta2
        theta3 = theta.theta3

        k = (theta2 / theta3) ** 2
        K = mp.elliprf(0, 1 - k ** 2, 1)
        value = 2 * K / (theta3 ** 2)

        verified = None
        if validate:
            from .validation import verified_digits

            verified = verified_digits(value, mp.pi)

        diag = PiDiagnostics(
            digits=digits,
            guard_digits=guard_digits,
            work_dps=work_dps,
            m=str(m),
            N=N,
            mode=mode,
            exp_calls=theta.diagnostics.exp_calls,
            verified_digits=verified,
        )
        return PiResult(value=value, diagnostics=diag)
    finally:
        mp.dps = old_dps
