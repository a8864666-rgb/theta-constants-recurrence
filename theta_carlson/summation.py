"""Deterministic summation routines."""

from __future__ import annotations

from typing import Iterable, Sequence


def sequential_sum(values: Iterable):
    """Sequential left-to-right summation."""
    total = None
    for value in values:
        total = value if total is None else total + value
    return 0 if total is None else total


def pairwise_sum(values: Sequence):
    """Pairwise recursive summation.

    This keeps the total work linear in the number of terms but reduces the
    reduction depth from O(N) to O(log N). It is used for deterministic,
    depth-controlled accumulation.
    """
    n = len(values)
    if n == 0:
        return 0
    if n == 1:
        return values[0]
    mid = n // 2
    return pairwise_sum(values[:mid]) + pairwise_sum(values[mid:])


def sum_values(values: Sequence, mode: str = "pairwise"):
    """Sum values using the requested summation mode."""
    if mode == "sequential":
        return sequential_sum(values)
    if mode == "pairwise":
        return pairwise_sum(values)
    raise ValueError(f"unknown summation mode: {mode}")
