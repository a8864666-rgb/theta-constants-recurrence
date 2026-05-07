## Environment report

Purpose: Confirm Python/platform/package environment reporting works.

Command: `/opt/pyvenv/bin/python scripts/environment_report.py`

Exit code: 0

Elapsed seconds: 5.671

Output:

```text
Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/generated/interface/models.py", line 48821, in hydrate_crdt_from_proto
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/remote.py", line 747, in __call__
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
Python: 3.13.5 (main, Jun 25 2025, 18:55:22) [GCC 14.2.0]
Platform: Linux-4.4.0-x86_64-with-glibc2.41
Machine: x86_64
Processor: 
CPU count: 56
mpmath: 1.3.0
pytest: 9.0.2

```

## Unit tests

Purpose: Run the artifact test suite.

Command: `/opt/pyvenv/bin/python -m pytest -q`

Exit code: 0

Elapsed seconds: 8.594

Output:

```text
Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/generated/interface/models.py", line 48821, in hydrate_crdt_from_proto
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/remote.py", line 747, in __call__
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                                                   [100%][0m
[32m[32m[1m6 passed[0m[32m in 0.22s[0m[0m

```

## Single theta--Carlson run

Purpose: Compute pi using triple-conditioned mode at a small precision target.

Command: `/opt/pyvenv/bin/python scripts/run_single.py --digits 50 --m 2.0 --mode triple --validate`

Exit code: 0

Elapsed seconds: 5.942

Output:

```text
Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/generated/interface/models.py", line 48821, in hydrate_crdt_from_proto
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/remote.py", line 747, in __call__
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
digits=50
m=2.0
N=10
mode=triple
work_dps=125
exp_calls=2
tail_minus_log10=104.798234624849
verified_digits=103
value_prefix=3.141592653589793238462643383279502884197169399375105820974944592307816406286209

```

## Small scaling benchmark

Purpose: Generate a short scaling CSV using the triple-conditioned evaluator.

Command: `/opt/pyvenv/bin/python scripts/benchmark_scaling_triple.py --digits 50 100 --out results/results_scaling_triple_smoke.csv`

Exit code: 0

Elapsed seconds: 5.617

Output:

```text
Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/generated/interface/models.py", line 48821, in hydrate_crdt_from_proto
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/remote.py", line 747, in __call__
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
{'digits': 50, 'm': '2.0', 'N': 10, 'N_over_D': '0.2', 'N_over_sqrtD': '1.41421356237', 'D_over_N': '5.0', 'time_seconds': '0.002688', 'exp_calls': 2, 'verified_digits': 103, 'tail_minus_log10': '104.798234625'}
{'digits': 100, 'm': '2.0', 'N': 13, 'N_over_D': '0.13', 'N_over_sqrtD': '1.3', 'D_over_N': '7.69230769231', 'time_seconds': '0.002849', 'exp_calls': 2, 'verified_digits': 168, 'tail_minus_log10': '169.94240691'}

```

## Small correctness validation

Purpose: Generate correctness-validation CSV files at small precision targets.

Command: `/opt/pyvenv/bin/python scripts/validate_correctness.py --digits 50 100 --out-prefix results/results_correctness_smoke`

Exit code: 0

Elapsed seconds: 5.696

Output:

```text
Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/generated/interface/models.py", line 48821, in hydrate_crdt_from_proto
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/remote.py", line 747, in __call__
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
{'digits': 50, 'm': '2.0', 'N': 10, 'tail_minus_log10': '104.798234624849482903187569364822851761611753506000836425036501726086923349562626668481575082646837497666844311484499030377520635973510125647886328312', 'delta_theta2': '0.0', 'delta_theta3': '0.0', 'verified_digits': 103}
{'digits': 100, 'm': '2.0', 'N': 13, 'tail_minus_log10': '169.94240691041055310979753092556247190735684855286659685780395836784324073896588576271714510306658181700575455763949223666704782222468006820314003502518393906316170892667868307750562734619281885640599', 'delta_theta2': '0.0', 'delta_theta3': '0.0', 'verified_digits': 168}

```

## Small baseline comparison

Purpose: Run transparent mpmath, AGM, and Chudnovsky baselines at small precision.

Command: `/opt/pyvenv/bin/python scripts/benchmark_pi_baselines.py --digits 50 --mode mpmath --mode agm --mode chudnovsky --out results/results_pi_baselines_smoke.csv`

Exit code: 0

Elapsed seconds: 5.680

Output:

```text
Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/generated/interface/models.py", line 48821, in hydrate_crdt_from_proto
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/remote.py", line 747, in __call__
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
{'digits': 50, 'method': 'mpmath', 'time_seconds': '0.000067', 'verified_digits': 76}
{'digits': 50, 'method': 'agm', 'time_seconds': '0.000268', 'verified_digits': 74}
{'digits': 50, 'method': 'chudnovsky', 'time_seconds': '0.000131', 'verified_digits': 74}

```

## Theta-family reproduction script

Purpose: Check the theta-family reproduction script can produce output.

Command: `/opt/pyvenv/bin/python scripts/reproduce_theta_family_table.py --digits 50 100 --out results/results_theta_family_smoke.csv`

Exit code: 0

Elapsed seconds: 5.735

Output:

```text
Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/generated/interface/models.py", line 48821, in hydrate_crdt_from_proto
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/remote.py", line 747, in __call__
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
{'digits': 50, 'mode': 'naive', 'm': '2.0', 'N': 10, 'time_seconds': '0.002546', 'exp_calls': 21, 'verified_digits': 103}
{'digits': 50, 'mode': 'partial', 'm': '2.0', 'N': 10, 'time_seconds': '0.002009', 'exp_calls': 21, 'verified_digits': 103}
{'digits': 50, 'mode': 'triple', 'm': '2.0', 'N': 10, 'time_seconds': '0.001566', 'exp_calls': 2, 'verified_digits': 103}
{'digits': 100, 'mode': 'naive', 'm': '2.0', 'N': 13, 'time_seconds': '0.003195', 'exp_calls': 27, 'verified_digits': 168}
{'digits': 100, 'mode': 'partial', 'm': '2.0', 'N': 13, 'time_seconds': '0.002824', 'exp_calls': 27, 'verified_digits': 168}
{'digits': 100, 'mode': 'triple', 'm': '2.0', 'N': 13, 'time_seconds': '0.002274', 'exp_calls': 2, 'verified_digits': 168}

```
