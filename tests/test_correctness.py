from mpmath import mp

from theta_carlson.correctness import tail_bounds, tail_minus_log10
from theta_carlson.validation import correctness_row


def test_tail_bounds_positive():
    mp.dps = 80
    r2, r3, total = tail_bounds(2, 10)
    assert r2 > 0
    assert r3 > 0
    assert total == r2 + r3
    assert tail_minus_log10(2, 10) > 0


def test_correctness_row_small():
    row = correctness_row(50, m=2)
    assert row["N"] > 0
    assert int(row["verified_digits"]) >= 45
