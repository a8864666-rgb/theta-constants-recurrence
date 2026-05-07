# Artifact Evaluation Report — Short-Run Smoke Validation

Artifact: `theta-carlson-toms-artifact-v0.2.zip`  
Evaluation date: 2026-05-07  
Overall result: **PASS**

## 1. Purpose

This report verifies that the software artifact accompanying the manuscript

**Triple Conditioning for High-Precision Theta--Carlson Evaluation: Algorithm, Software Artifact, and Benchmarks**

is executable in a clean extracted directory and that the main commands described in the manuscript's software-artifact section can run at small precision targets.

This is a short-run smoke validation, not a replacement for the full benchmark reproduction. The goal is to confirm installability, script availability, unit-test execution, basic numerical evaluation, CSV generation, and environment reporting.

## 2. Artifact root and execution setup

The artifact was extracted and commands were executed from:

```text
theta-carlson-toms/
```

with:

```text
PYTHONPATH=/mnt/data/artifact_eval_v0_2/theta-carlson-toms
```

## 3. Command results

| Check | Exit code | Time (s) | Status |
|---|---:|---:|---|
| Environment report | 0 | 5.671 | PASS |
| Unit tests | 0 | 8.594 | PASS |
| Single theta--Carlson run | 0 | 5.942 | PASS |
| Small scaling benchmark | 0 | 5.617 | PASS |
| Small correctness validation | 0 | 5.696 | PASS |
| Small baseline comparison | 0 | 5.680 | PASS |
| Theta-family reproduction script | 0 | 5.735 | PASS |


## 4. Generated output files

| Output file | Exists | Size bytes |
|---|---:|---:|
| `results/results_scaling_triple_smoke.csv` | yes | 224 |
| `results/results_correctness_smoke_certification.csv` | yes | 472 |
| `results/results_correctness_smoke_tail_bounds.csv` | yes | 406 |
| `results/results_correctness_smoke_recurrence_vs_direct.csv` | yes | 77 |
| `results/results_correctness_smoke_guard_stability.csv` | yes | 113 |
| `results/results_pi_baselines_smoke.csv` | yes | 114 |
| `results/results_theta_family_smoke.csv` | yes | 261 |


## 5. Output previews

### Scaling smoke CSV

```csv
digits,m,N,N_over_D,N_over_sqrtD,D_over_N,time_seconds,exp_calls,verified_digits,tail_minus_log10
50,2.0,10,0.2,1.41421356237,5.0,0.002688,2,103,104.798234625
100,2.0,13,0.13,1.3,7.69230769231,0.002849,2,168,169.94240691

```

### Correctness certification smoke CSV

```csv
digits,m,N,tail_minus_log10,delta_theta2,delta_theta3,verified_digits
50,2.0,10,104.798234624849482903187569364822851761611753506000836425036501726086923349562626668481575082646837497666844311484499030377520635973510125647886328312,0.0,0.0,103
100,2.0,13,169.94240691041055310979753092556247190735684855286659685780395836784324073896588576271714510306658181700575455763949223666704782222468006820314003502518393906316170892667868307750562734619281885640599,0.0,0.0,168

```

### Baseline comparison smoke CSV

```csv
digits,method,time_seconds,verified_digits
50,mpmath,0.000067,76
50,agm,0.000268,74
50,chudnovsky,0.000131,74

```

### Theta-family smoke CSV

```csv
digits,mode,m,N,time_seconds,exp_calls,verified_digits
50,naive,2.0,10,0.002546,21,103
50,partial,2.0,10,0.002009,21,103
50,triple,2.0,10,0.001566,2,103
100,naive,2.0,13,0.003195,27,168
100,partial,2.0,13,0.002824,27,168
100,triple,2.0,13,0.002274,2,168

```

## 6. Interpretation

The short-run validation confirms that:

1. the package can be imported from the repository root using `PYTHONPATH=.`;
2. the environment-report script runs;
3. the unit tests run successfully;
4. a small triple-conditioned theta--Carlson computation completes and verifies digits against reference pi;
5. the scaling benchmark writes a CSV file;
6. the correctness-validation workflow writes CSV files;
7. the baseline comparison script runs;
8. the theta-family reproduction script produces output.

Absolute runtime values in this report are not intended to match the manuscript tables. They are smoke-test values at small precision targets. Full reproduction of manuscript tables should use the commands and digit targets listed in `README.md` and `USER_MANUAL.md`.

## 7. Notes

- If run in an environment with startup warnings unrelated to this artifact, such warnings may appear before the test output. The relevant criterion is the process exit code and test result.
- The artifact is a Python/mpmath reference implementation, not a low-level optimized MPFR/GMP/Arb backend.
- Before formal submission, run the full benchmark commands listed in the manuscript and compare the resulting CSV files with the manuscript tables.

## 8. Recommended submission checklist status

- [x] Artifact zip exists.
- [x] README exists.
- [x] User manual exists.
- [x] License exists.
- [x] Requirements file exists.
- [x] Unit tests pass in short-run validation.
- [x] Environment report runs.
- [x] Single-run computation works.
- [x] Scaling smoke benchmark works.
- [x] Correctness smoke validation works.
- [x] Baseline smoke comparison works.
- [x] Theta-family smoke script works.
- [ ] Full manuscript-scale benchmarks should be rerun before final submission.
- [ ] Final CSV values should be checked against manuscript tables before final submission.

## 9. Raw command log

The complete raw command log is included inside the evaluated artifact at:

```text
results/artifact_evaluation_raw_log.md
```
