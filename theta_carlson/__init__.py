"""Reference implementation for triple-conditioned theta--Carlson evaluation."""

from .core import theta_carlson_pi, plan_truncation_depth
from .theta import theta_sums
from .validation import verified_digits

__all__ = [
    "theta_carlson_pi",
    "plan_truncation_depth",
    "theta_sums",
    "verified_digits",
]
