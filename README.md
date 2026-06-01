# Recurrence-Accelerated Jacobi Theta Constants

Reference implementation for the manuscript:

**Recurrence-Accelerated High-Precision Evaluation of Jacobi Theta Constants with Gaussian-Tail Certification**

Author: Lâu Thiat-uí
Affiliation: Independent Researcher (Taiwan)

## Purpose

This repository provides a transparent reference implementation for high-precision evaluation of the Jacobi theta constants

[
\theta_2(e^{-m}), \qquad \theta_3(e^{-m}), \qquad m>0,
]

together with theta-ratio evaluation, Gaussian-tail truncation certification, recurrence-versus-direct validation, guard-precision stability checks, and reproducible benchmark scripts.

The primary purpose of this software is **theta-constant and Gaussian theta-series evaluation**.

The Carlson elliptic-integral identity involving (\pi) is included only as an optional end-to-end validation example. It is not the main computational target of this repository.

## Main features

The artifact supports:

* recurrence-generated evaluation of (\theta_2(e^{-m})) and (\theta_3(e^{-m}));
* theta-ratio evaluation, including (\theta_2/\theta_3) and ((\theta_2/\theta_3)^2);
* Gaussian lattice-sum experiments related to (\theta_3(e^{-m}));
* Gaussian-tail truncation planning and tail-bound diagnostics;
* recurrence-versus-direct theta validation;
* guard-precision stability checks;
* benchmark scaling experiments for (N = O(\sqrt D));
* optional Carlson elliptic-integral validation using (\pi) as an external reference;
* CSV-based reproducibility workflows;
* environment reporting.

## Difference from the earlier TOMS artifact

An earlier version of this repository was prepared as a TOMS-style theta--Carlson artifact.

The present version has been reorganized for the Numerical Algorithms manuscript:

**Recurrence-Accelerated High-Precision Evaluation of Jacobi Theta Constants with Gaussian-Tail Certification**

The main computational target is now:

* high-precision evaluation of (\theta_2(e^{-m})) and (\theta_3(e^{-m}));
* theta-ratio evaluation;
* Gaussian lattice sums and theta-like Gaussian series;
* explicit Gaussian-tail certification;
* recurrence-generated term construction reducing high-precision exponential calls from (O(N)) to (O(1)).

The Carlson/(\pi) computation is retained only as an optional validation example and is not the primary contribution.

## Mathematical idea

For (q=e^{-m}), (m>0), the theta constants are

[
\theta_3(e^{-m}) = 1 + 2\sum_{n=1}^{\infty} e^{-mn^2},
]

and

[
\theta_2(e^{-m}) = 2\sum_{n=0}^{\infty} e^{-m(n+1/2)^2}.
]

A direct implementation evaluates one high-precision exponential for each retained term.

The recurrence implementation initializes only a constant number of exponentials and then generates terms by multiplication:

[
a_{n+1}=a_n r^{2n+1},
\qquad
b_{n+1}=b_n r^{2n+2},
\qquad
r=e^{-m}.
]

The ratio factors are also updated recursively, so the number of high-precision exponential evaluations in an (N)-term theta summation is reduced from (O(N)) to (O(1)).

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

Run a single recurrence-generated theta evaluation:

```bash
PYTHONPATH=. python scripts/run_single.py --digits 1000 --m 2.0 --mode triple --validate
```

In the current codebase, `--mode triple` refers to the recurrence-generated theta evaluator.

## Reproduce theta scaling table

```bash
PYTHONPATH=. python scripts/benchmark_scaling_triple.py \
  --digits 1000 5000 10000 20000 \
  --out results/results_scaling_triple.csv
```

This reproduces the Gaussian-tail scaling experiment showing that, for fixed (m), the selected truncation depth satisfies approximately

[
N = O(\sqrt D).
]

## Reproduce correctness validation

```bash
PYTHONPATH=. python scripts/validate_correctness.py \
  --digits 1000 5000 10000 \
  --out-prefix results/results_correctness
```

This generates:

* `results/results_correctness_certification.csv`
* `results/results_correctness_tail_bounds.csv`
* `results/results_correctness_recurrence_vs_direct.csv`
* `results/results_correctness_guard_stability.csv`

These files support the manuscript tables for tail certification, recurrence-versus-direct agreement, digit validation, and guard-precision stability.

## Optional Carlson validation

The Carlson elliptic-integral validation reconstructs (\pi) from theta constants and Carlson's (R_F). This is used only as an end-to-end pipeline check.

```bash
PYTHONPATH=. python scripts/validate_digits.py --digits 1000 5000 10000
```

The Carlson/(\pi) validation is not the primary purpose of the artifact.

## Optional baseline comparisons

The repository also contains earlier comparison scripts for standard (\pi)-computation baselines:

```bash
PYTHONPATH=. python scripts/benchmark_pi_baselines.py \
  --digits 1000 5000 \
  --mode mpmath --mode agm --mode chudnovsky \
  --out results/results_pi_baselines.csv
```

These scripts are retained only for historical comparison and optional validation context. They are not part of the main contribution of the Numerical Algorithms manuscript.

## Run tests

```bash
PYTHONPATH=. pytest
```

## Environment report

```bash
PYTHONPATH=. python scripts/environment_report.py
```

## Repository organization

```text
theta-carlson-toms/
├── theta_carlson/          # Reference theta and Carlson implementation
├── scripts/                # Benchmark and validation scripts
├── tests/                  # Unit tests
├── results/                # Reproducibility CSV files
├── README.md
├── USER_MANUAL.md
├── ARTIFACT_CHECKLIST.md
├── ARTIFACT_EVALUATION_REPORT.md
├── CITATION.cff
├── LICENSE
└── requirements.txt
```

The package name and repository name retain the earlier theta--Carlson naming for continuity. The current manuscript and release use the code primarily for recurrence-accelerated theta-constant and Gaussian theta-series evaluation.

## Scope

This reference implementation prioritizes clarity, reproducibility, and inspectability.

It is not intended to be:

* a record-setting (\pi)-computation library;
* a replacement for optimized AGM, Chudnovsky, MPFR, GMP, Arb, or library-level special-function implementations;
* a fully certified ball-arithmetic implementation.

It is intended to provide:

* a transparent recurrence-generated theta evaluator;
* explicit Gaussian-tail truncation certification;
* reproducible numerical diagnostics;
* validation scripts for theta constants, theta ratios, and Gaussian theta-series computations.

## Code release for the Numerical Algorithms manuscript

The version associated with the Numerical Algorithms manuscript should be archived as a tagged release, for example:

```text
v1.0-theta
```

Recommended release title:

```text
Numerical Algorithms theta-constant artifact v1.0
```

The release should accompany the manuscript:

**Recurrence-Accelerated High-Precision Evaluation of Jacobi Theta Constants with Gaussian-Tail Certification**

## License

This repository is released under the MIT License.

## Citation

If you use this software, please cite the associated manuscript and the tagged software release.

Suggested citation title:

**Recurrence-Accelerated High-Precision Evaluation of Jacobi Theta Constants with Gaussian-Tail Certification**
