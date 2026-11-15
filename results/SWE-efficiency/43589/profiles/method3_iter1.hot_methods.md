# Methods of the workload by self time (method3_iter1)

Mean of 10 repetitions of the same benchmark.
Each repetition got its own profile file.

Profiles: /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method3_iter1.run1.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method3_iter1.run2.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method3_iter1.run3.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method3_iter1.run4.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method3_iter1.run5.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method3_iter1.run6.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method3_iter1.run7.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method3_iter1.run8.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method3_iter1.run9.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method3_iter1.run10.speedscope.json
Sampled: 17.438s per run across 17.392999999999997s of code frames (0.045s of profiler overhead)
Ranking: all

Percentages are of the sampled time, not of the benchmark run: py-spy sampled 17.438s per run. The 62 methods below account for 17.25s, 98.89% of the profile.

| # | method | self time | sampled | where |
| - | ------ | --------- | ------- | ----- |
| 1 | `__array__` | 8.277s | 47.47% | `/testbed/pandas/core/arrays/datetimelike.py:316` |
| 2 | `__iter__` | 7.572s | 43.42% | `/testbed/pandas/core/arrays/datetimes.py:626` |
| 3 | `equals` | 0.68s | 3.9% | `/testbed/pandas/core/indexes/multi.py:3552` |
| 4 | `_array_equivalent_object` | 0.54s | 3.1% | `/testbed/pandas/core/dtypes/missing.py:484` |
| 5 | `take` | 0.048s | 0.28% | `/testbed/pandas/core/algorithms.py:1522` |
| 6 | `workload` | 0.017s | 0.1% | `/home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/workload.py:13` |
| 7 | `dedent` | 0.014s | 0.08% | `/opt/miniconda3/envs/testbed/lib/python3.8/textwrap.py:430` |
| 8 | `array_equal` | 0.011s | 0.06% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/numeric.py:2468` |
| 9 | `namedtuple` | 0.006s | 0.03% | `/opt/miniconda3/envs/testbed/lib/python3.8/collections/__init__.py:394` |
| 10 | `tz` | 0.005s | 0.03% | `/testbed/pandas/core/arrays/datetimes.py:563` |
| 11 | `_all` | 0.005s | 0.03% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/_methods.py:64` |
| 12 | `DataFrame` | 0.004s | 0.02% | `/testbed/pandas/core/frame.py:7169` |
| 13 | `_execute_child` | 0.004s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/subprocess.py:1655` |
| 14 | `array_equivalent` | 0.003s | 0.02% | `/testbed/pandas/core/dtypes/missing.py:418` |
| 15 | `addpackage` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/site.py:177` |
| 16 | `__get_openssl_constructor` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/hashlib.py:131` |
| 17 | `__setitem__` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:110` |
| 18 | `_optimize_charset` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:396` |
| 19 | `needs_i8_conversion` | 0.002s | 0.01% | `/testbed/pandas/core/dtypes/common.py:1177` |
| 20 | `sub` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/re.py:210` |
| 21 | `_parse` | 0.002s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/vendored/docscrape.py:392` |
| 22 | `update_wrapper` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/functools.py:55` |
| 23 | `asi8` | 0.002s | 0.01% | `/testbed/pandas/core/arrays/datetimelike.py:291` |
| 24 | `SelectionMixin` | 0.002s | 0.01% | `/testbed/pandas/core/base.py:198` |
| 25 | `nlevels` | 0.002s | 0.01% | `/testbed/pandas/core/indexes/multi.py:931` |
| 26 | `_collect_type_vars` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:183` |
| 27 | `tile` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/lib/shape_base.py:1278` |
| 28 | `is_array_like` | 0.001s | 0.01% | `/testbed/pandas/core/dtypes/inference.py:213` |
| 29 | `IndexOpsMixin` | 0.001s | 0.01% | `/testbed/pandas/core/base.py:992` |
| 30 | `_make_global_functions` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compute.py:321` |
| 31 | `__init__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/timeit.py:132` |
| 32 | `tz` | 0.001s | 0.01% | `/testbed/pandas/core/dtypes/dtypes.py:723` |
| 33 | `__call__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:339` |
| 34 | `__call__` | 0.001s | 0.01% | `/testbed/pandas/util/_decorators.py:489` |
| 35 | `get_dtype` | 0.001s | 0.01% | `/testbed/pandas/core/dtypes/common.py:1571` |
| 36 | `__new__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:265` |
| 37 | `_combine_flags` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:69` |
| 38 | `UInt64Index` | 0.001s | 0.01% | `/testbed/pandas/core/indexes/numeric.py:451` |
| 39 | `codes` | 0.001s | 0.01% | `/testbed/pandas/core/indexes/multi.py:954` |
| 40 | `__new__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/abc.py:86` |
| 41 | `_get_options_class` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compute.py:205` |
| 42 | `_parse_summary` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/vendored/docscrape.py:369` |
| 43 | `FrameRowApply` | 0.001s | 0.01% | `/testbed/pandas/core/apply.py:893` |
| 44 | `__init__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:669` |
| 45 | `_compile_charset` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:253` |
| 46 | `_process_class` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/dataclasses.py:863` |
| 47 | `_compile` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:145` |
| 48 | `getwidth` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:198` |
| 49 | `LocaleTextCalendar` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/calendar.py:581` |
| 50 | `__enter__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/warnings.py:466` |
| 51 | `freq` | 0.001s | 0.01% | `/testbed/pandas/core/arrays/datetimelike.py:905` |
| 52 | `inner` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:258` |
| 53 | `parse` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:940` |
| 54 | `pandas_dtype` | 0.001s | 0.01% | `/testbed/pandas/core/dtypes/common.py:1787` |
| 55 | `decorate` | 0.001s | 0.01% | `/testbed/pandas/util/_decorators.py:298` |
| 56 | `Index` | 0.001s | 0.01% | `/testbed/pandas/core/indexes/base.py:4876` |
| 57 | `eof` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/vendored/docscrape.py:72` |
| 58 | `BaseIndexer` | 0.001s | 0.01% | `/testbed/pandas/core/indexers/objects.py:59` |
| 59 | `is_float_dtype` | 0.001s | 0.01% | `/testbed/pandas/core/dtypes/common.py:1264` |
| 60 | `_fix_result_transcoding` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/urllib/parse.py:370` |
| 61 | `cleandoc` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:631` |
| 62 | `__init__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/subprocess.py:848` |

Self time and sampled percentage are per run, averaged over the repetitions.
