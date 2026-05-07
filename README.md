# Theta--Carlson TOMS Artifact

Reference software artifact for:

**Triple Conditioning for High-Precision Theta--Carlson Evaluation: Algorithm, Software Artifact, and Benchmarks**

Author: Lâu Thiat-uí (Taiwan)

## Purpose

This repository provides a transparent reference implementation of the
triple-conditioned theta--Carlson evaluator described in the manuscript.
It is intended for reproducibility, inspection, and validation rather than
maximum low-level performance.

The artifact supports:

- theta--Carlson evaluation of pi;
- naive, partially conditioned, and triple-conditioned theta variants;
- Gaussian-tail truncation planning;
- recurrence-versus-direct theta validation;
- digit certification against reference pi;
- guard-precision stability checks;
- baseline comparisons with mpmath, AGM, and Chudnovsky-style pi routines;
- environment reporting.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

For local use from the repository root:

```bash
export PYTHONPATH=.
```

On Windows PowerShell:

```powershell
$env:PYTHONPATH="."
```

## Quick start

```bash
PYTHONPATH=. python scripts/run_single.py --digits 1000 --m 2.0 --mode triple --validate
```

## Reproduce scaling table

```bash
PYTHONPATH=. python scripts/benchmark_scaling_triple.py \
  --digits 1000 5000 10000 20000 \
  --out results/results_scaling_triple.csv
```

## Reproduce correctness validation

```bash
PYTHONPATH=. python scripts/validate_correctness.py \
  --digits 1000 5000 10000 \
  --out-prefix results/results_correctness
```

This generates:

- `results/results_correctness_certification.csv`
- `results/results_correctness_tail_bounds.csv`
- `results/results_correctness_recurrence_vs_direct.csv`
- `results/results_correctness_guard_stability.csv`

## Reproduce baseline comparisons

```bash
PYTHONPATH=. python scripts/benchmark_pi_baselines.py \
  --digits 1000 5000 \
  --mode mpmath --mode agm --mode chudnovsky \
  --out results/results_pi_baselines.csv
```

## Run tests

```bash
PYTHONPATH=. pytest
```

## Environment report

```bash
PYTHONPATH=. python scripts/environment_report.py
```

## Scope

This reference implementation prioritizes clarity and reproducibility.
It is not a record-setting pi computation library and is not intended to
replace optimized Chudnovsky, AGM, MPFR, GMP, Arb, or library-level pi engines.


## Included manuscript CSV files

The `results/` directory includes the CSV files named in manuscript Section 6.1. These files record the manuscript table values and can be regenerated or overwritten by the scripts. Timing values may differ on another machine.
