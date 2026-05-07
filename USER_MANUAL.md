# User Manual and Reproducibility Guide

## 1. Artifact overview

The artifact implements a reference version of the triple-conditioned
theta--Carlson evaluator. The main package is `theta_carlson`.

## 2. Main commands

### Single run

```bash
PYTHONPATH=. python scripts/run_single.py --digits 1000 --m 2.0 --mode triple --validate
```

### Scaling benchmark

```bash
PYTHONPATH=. python scripts/benchmark_scaling_triple.py --digits 1000 5000 10000 20000
```

### Correctness validation

```bash
PYTHONPATH=. python scripts/validate_correctness.py --digits 1000 5000 10000
```

### Baselines

```bash
PYTHONPATH=. python scripts/benchmark_pi_baselines.py --digits 1000 5000 --mode mpmath --mode agm --mode chudnovsky
```

### Tests

```bash
PYTHONPATH=. pytest
```

## 3. Expected outputs

Benchmark and validation scripts write CSV files to the `results/` directory.
Absolute timings depend on hardware and Python/mpmath versions, so exact
runtime values may differ from the manuscript. Scaling quantities such as
`N`, `N/D`, `N/sqrt(D)`, exponential-call count, and verified digits should
remain consistent up to implementation and guard-precision settings.

## 4. Limitations

The artifact is a Python/mpmath reference implementation. It is designed for
transparent reproduction, not maximum performance. Low-level MPFR/GMP/Arb/C/C++
implementations are future work.
