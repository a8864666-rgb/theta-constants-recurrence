from mpmath import mp

from theta_carlson.pi_baselines import pi_agm, pi_chudnovsky, pi_mpmath
from theta_carlson.validation import verified_digits


def test_baselines_small():
    mp.dps = 100
    for fn in [pi_mpmath, pi_agm, pi_chudnovsky]:
        val = fn(50)
        assert verified_digits(val, mp.pi) >= 40
