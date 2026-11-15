# Methods of the workload by self time (before)

Mean of 10 repetitions of the same benchmark.
Each repetition got its own profile file.

Profiles: /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.before.run1.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.before.run2.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.before.run3.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.before.run4.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.before.run5.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.before.run6.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.before.run7.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.before.run8.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.before.run9.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.before.run10.speedscope.json
Sampled: 6.557s per run across 6.4910000000000005s of code frames (0.066s of profiler overhead)
Ranking: all

Percentages are of the sampled time, not of the benchmark run: py-spy sampled 6.557s per run. The 74 methods below account for 6.3s, 96.1% of the profile.

| # | method | self time | sampled | where |
| - | ------ | --------- | ------- | ----- |
| 1 | `_cmp_method` | 2.259s | 34.45% | `/testbed/pandas/core/arrays/datetimelike.py:939` |
| 2 | `_isna_ndarraylike` | 1.566s | 23.88% | `/testbed/pandas/core/dtypes/missing.py:230` |
| 3 | `_isnan` | 1.52s | 23.18% | `/testbed/pandas/core/arrays/datetimelike.py:766` |
| 4 | `generate_regular_range` | 0.514s | 7.84% | `/testbed/pandas/core/arrays/_ranges.py:62` |
| 5 | `_wrapreduction` | 0.125s | 1.91% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/core/fromnumeric.py:88` |
| 6 | `_any` | 0.096s | 1.46% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/core/_methods.py:58` |
| 7 | `__lt__` | 0.08s | 1.22% | `/testbed/pandas/core/arraylike.py:37` |
| 8 | `setup` | 0.014s | 0.21% | `/home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/workload.py:11` |
| 9 | `_generate_range` | 0.009s | 0.14% | `/testbed/pandas/core/arrays/datetimes.py:376` |
| 10 | `dedent` | 0.009s | 0.14% | `/opt/miniconda3/envs/testbed/lib/python3.10/textwrap.py:438` |
| 11 | `__init__` | 0.008s | 0.12% | `/opt/miniconda3/envs/testbed/lib/python3.10/typing.py:663` |
| 12 | `new_method` | 0.006s | 0.09% | `/testbed/pandas/core/ops/common.py:58` |
| 13 | `_parse` | 0.006s | 0.09% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_parse.py:532` |
| 14 | `sub` | 0.004s | 0.06% | `/opt/miniconda3/envs/testbed/lib/python3.10/re.py:209` |
| 15 | `__setattr__` | 0.003s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.10/typing.py:971` |
| 16 | `namedtuple` | 0.003s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.10/collections/__init__.py:414` |
| 17 | `_validate_comparison_value` | 0.003s | 0.05% | `/testbed/pandas/core/arrays/datetimelike.py:446` |
| 18 | `asi8` | 0.003s | 0.05% | `/testbed/pandas/core/arrays/datetimelike.py:243` |
| 19 | `_compile` | 0.003s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.10/re.py:311` |
| 20 | `getargs` | 0.002s | 0.03% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/_utils/_inspect.py:74` |
| 21 | `update_wrapper` | 0.002s | 0.03% | `/opt/miniconda3/envs/testbed/lib/python3.10/functools.py:52` |
| 22 | `parse_parts` | 0.002s | 0.03% | `/opt/miniconda3/envs/testbed/lib/python3.10/pathlib.py:67` |
| 23 | `_optimize_charset` | 0.002s | 0.03% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_compile.py:338` |
| 24 | `_type_convert` | 0.002s | 0.03% | `/opt/miniconda3/envs/testbed/lib/python3.10/typing.py:142` |
| 25 | `__new__` | 0.002s | 0.03% | `/opt/miniconda3/envs/testbed/lib/python3.10/enum.py:205` |
| 26 | `_check` | 0.002s | 0.03% | `/testbed/pandas/core/dtypes/generic.py:32` |
| 27 | `__new__` | 0.002s | 0.03% | `/opt/miniconda3/envs/testbed/lib/python3.10/abc.py:106` |
| 28 | `Union` | 0.002s | 0.03% | `/opt/miniconda3/envs/testbed/lib/python3.10/typing.py:512` |
| 29 | `view` | 0.002s | 0.03% | `/testbed/pandas/core/arrays/datetimelike.py:378` |
| 30 | `__next` | 0.002s | 0.03% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_parse.py:247` |
| 31 | `_compile` | 0.002s | 0.03% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_compile.py:90` |
| 32 | `_parse_sub` | 0.002s | 0.03% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_parse.py:439` |
| 33 | `add_newdoc` | 0.002s | 0.03% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/core/function_base.py:548` |
| 34 | `_generate_range_overflow_safe` | 0.002s | 0.03% | `/testbed/pandas/core/arrays/_ranges.py:108` |
| 35 | `CFUNCTYPE` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/ctypes/__init__.py:102` |
| 36 | `verify_matching_signatures` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/core/overrides.py:85` |
| 37 | `communicate` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/subprocess.py:1136` |
| 38 | `tz` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/datetimes.py:519` |
| 39 | `needs_i8_conversion` | 0.001s | 0.02% | `/testbed/pandas/core/dtypes/common.py:1226` |
| 40 | `__new__` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/lazy.py:110` |
| 41 | `_code` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_compile.py:600` |
| 42 | `_convert_` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/enum.py:547` |
| 43 | `indent` | 0.001s | 0.02% | `/testbed/pandas/util/_decorators.py:485` |
| 44 | `count_not_none` | 0.001s | 0.02% | `/testbed/pandas/core/common.py:195` |
| 45 | `_is_dunder` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/typing.py:918` |
| 46 | `__init__` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/importlib/metadata/__init__.py:790` |
| 47 | `spec_for_distutils` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/__init__.py:132` |
| 48 | `__init__` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/core/getlimits.py:692` |
| 49 | `repeat` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/timeit.py:207` |
| 50 | `add_delegate_accessors` | 0.001s | 0.02% | `/testbed/pandas/core/accessor.py:140` |
| 51 | `_class_escape` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_parse.py:340` |
| 52 | `children` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/importlib/metadata/__init__.py:751` |
| 53 | `_create_delegator_property` | 0.001s | 0.02% | `/testbed/pandas/core/accessor.py:80` |
| 54 | `_is_sunder` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/enum.py:40` |
| 55 | `_hasnans` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/datetimelike.py:773` |
| 56 | `_assert_tzawareness_compat` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/datetimes.py:641` |
| 57 | `__getitem__` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_parse.py:166` |
| 58 | `match` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_parse.py:250` |
| 59 | `ExtensionArray` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/base.py:213` |
| 60 | `__getitem__` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/typing.py:1207` |
| 61 | `isna` | 0.001s | 0.02% | `/testbed/pandas/core/dtypes/missing.py:127` |
| 62 | `shape` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/_mixins.py:105` |
| 63 | `get_dtype` | 0.001s | 0.02% | `/testbed/pandas/core/dtypes/common.py:1598` |
| 64 | `_type_check` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/typing.py:168` |
| 65 | `_try_wait` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/subprocess.py:1896` |
| 66 | `decorator` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/core/overrides.py:166` |
| 67 | `Thread` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/threading.py:820` |
| 68 | `_guarded_repr_or_str` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/core/arrayprint.py:1592` |
| 69 | `joinpath` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/importlib/metadata/__init__.py:747` |
| 70 | `_check_compatible_with` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/datetimes.py:472` |
| 71 | `is_datetime64tz_dtype` | 0.001s | 0.02% | `/testbed/pandas/core/dtypes/common.py:420` |
| 72 | `_collect_type_vars` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/typing.py:215` |
| 73 | `seterr` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/core/_ufunc_config.py:128` |
| 74 | `workload` | 0.001s | 0.02% | `/home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/workload.py:16` |

Self time and sampled percentage are per run, averaged over the repetitions.
