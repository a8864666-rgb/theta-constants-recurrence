# Artifact Checklist for TOMS Resubmission

## Package completeness

- [x] `README.md` included
- [x] `USER_MANUAL.md` included
- [x] `LICENSE` included
- [x] `requirements.txt` included
- [x] Python package `theta_carlson/` included
- [x] Reproduction scripts included in `scripts/`
- [x] Tests included in `tests/`
- [x] Results directory included

## Installability

- [ ] Create a fresh virtual environment
- [ ] Run `python -m pip install -r requirements.txt`
- [ ] Set `PYTHONPATH=.` from repository root

## Smoke tests

- [ ] Run `PYTHONPATH=. pytest`
- [ ] Run `PYTHONPATH=. python scripts/environment_report.py`
- [ ] Run `PYTHONPATH=. python scripts/run_single.py --digits 1000 --m 2.0 --mode triple --validate`

## Reproducibility commands

- [ ] Run scaling table:
  `PYTHONPATH=. python scripts/benchmark_scaling_triple.py --digits 1000 5000 10000 20000`

- [ ] Run correctness validation:
  `PYTHONPATH=. python scripts/validate_correctness.py --digits 1000 5000 10000`

- [ ] Run baseline comparisons:
  `PYTHONPATH=. python scripts/benchmark_pi_baselines.py --digits 1000 5000 --mode mpmath --mode agm --mode chudnovsky`

## Manuscript consistency

- [x] Repository structure matches manuscript Section 6
- [x] Artifact includes validation commands described in manuscript
- [x] Artifact includes environment-report script
- [x] Artifact includes tests
- [ ] Final benchmark CSV values checked against manuscript tables
- [ ] Cover letter states that this is a complete reworking of TOMS-2026-0010

## Notes

The unchecked items should be completed immediately before formal submission
on the final machine or environment used to prepare the artifact.


## Consistency pass v0.2

- [x] Root directory renamed to `theta-carlson-toms/` to match manuscript Section 6.1.
- [x] All files listed in manuscript Section 6.1 are present.
- [x] Manuscript-named result CSV files are included in `results/`.
- [x] `reproduce_theta_family_table.py` produces naive/partial/triple ablation rows.
- [x] `benchmark_append.py` appends one theta-family row while preserving completed CSV rows.
- [x] Smoke commands passed on the packaging machine.
