from mpmath import mp

from theta_carlson.core import plan_truncation_depth, theta_carlson_pi
from theta_carlson.theta import theta_sums


def test_plan_truncation_depth_positive():
    assert plan_truncation_depth(100, m=2) > 0


def test_recurrence_agrees_with_direct_small():
    mp.dps = 80
    rec = theta_sums(m=2, N=8, mode="triple")
    direct = theta_sums(m=2, N=8, mode="partial")
    assert abs(rec.theta2 - direct.theta2) < mp.mpf("1e-70")
    assert abs(rec.theta3 - direct.theta3) < mp.mpf("1e-70")


def test_theta_carlson_pi_small():
    result = theta_carlson_pi(digits=50, m=2, mode="triple", validate=True)
    assert result.diagnostics.N > 0
    assert result.diagnostics.exp_calls == 2
    assert result.diagnostics.verified_digits >= 45
