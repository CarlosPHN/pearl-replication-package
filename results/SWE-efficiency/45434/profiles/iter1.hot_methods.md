# Methods of the workload by self time (iter1)

Mean of 10 repetitions of the same benchmark.
Each repetition got its own profile file.

Profiles: /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.iter1.run1.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.iter1.run2.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.iter1.run3.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.iter1.run4.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.iter1.run5.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.iter1.run6.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.iter1.run7.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.iter1.run8.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.iter1.run9.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.iter1.run10.speedscope.json
Sampled: 1.841s per run across 1.804s of code frames (0.037s of profiler overhead)
Ranking: all

Percentages are of the sampled time, not of the benchmark run: py-spy sampled 1.841s per run. The 53 methods below account for 1.67s, 90.44% of the profile.

| # | method | self time | sampled | where |
| - | ------ | --------- | ------- | ----- |
| 1 | `setup` | 0.57s | 30.96% | `/home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/workload.py:10` |
| 2 | `_values_for_argsort` | 0.49s | 26.62% | `/testbed/pandas/core/arrays/integer.py:323` |
| 3 | `_amin` | 0.453s | 24.61% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/core/_methods.py:45` |
| 4 | `_any` | 0.044s | 2.39% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/core/_methods.py:58` |
| 5 | `coerce_to_array` | 0.034s | 1.85% | `/testbed/pandas/core/arrays/integer.py:163` |
| 6 | `dedent` | 0.011s | 0.6% | `/opt/miniconda3/envs/testbed/lib/python3.8/textwrap.py:431` |
| 7 | `namedtuple` | 0.004s | 0.22% | `/opt/miniconda3/envs/testbed/lib/python3.8/collections/__init__.py:456` |
| 8 | `sub` | 0.004s | 0.22% | `/opt/miniconda3/envs/testbed/lib/python3.8/re.py:210` |
| 9 | `_parse` | 0.004s | 0.22% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:495` |
| 10 | `array` | 0.003s | 0.16% | `/testbed/pandas/core/construction.py:298` |
| 11 | `_execute_child` | 0.002s | 0.11% | `/opt/miniconda3/envs/testbed/lib/python3.8/subprocess.py:1655` |
| 12 | `_parse_summary` | 0.002s | 0.11% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/vendored/docscrape.py:364` |
| 13 | `deepcopy` | 0.002s | 0.11% | `/opt/miniconda3/envs/testbed/lib/python3.8/copy.py:137` |
| 14 | `__init__` | 0.002s | 0.11% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/vendored/docscrape.py:157` |
| 15 | `__init__` | 0.002s | 0.11% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:2491` |
| 16 | `_is_sunder` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:39` |
| 17 | `_make_signature` | 0.001s | 0.05% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/compute.py:272` |
| 18 | `__init__` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/selectors.py:213` |
| 19 | `append` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:173` |
| 20 | `__get_openssl_constructor` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/hashlib.py:131` |
| 21 | `__init__` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:505` |
| 22 | `_is_at_section` | 0.001s | 0.05% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/vendored/docscrape.py:186` |
| 23 | `workload` | 0.001s | 0.05% | `/home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/workload.py:15` |
| 24 | `seterr` | 0.001s | 0.05% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/core/_ufunc_config.py:128` |
| 25 | `cleandoc` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:631` |
| 26 | `__init__` | 0.001s | 0.05% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/tz/tz.py:464` |
| 27 | `DataFrame` | 0.001s | 0.05% | `/testbed/pandas/core/frame.py:4636` |
| 28 | `__setitem__` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:169` |
| 29 | `__call__` | 0.001s | 0.05% | `/testbed/pandas/util/_decorators.py:489` |
| 30 | `_wrapreduction` | 0.001s | 0.05% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/core/fromnumeric.py:73` |
| 31 | `update_wrapper` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/functools.py:49` |
| 32 | `inner` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/contextlib.py:75` |
| 33 | `_make_global_functions` | 0.001s | 0.05% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/compute.py:323` |
| 34 | `timeit` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/timeit.py:174` |
| 35 | `_optimize_charset` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:300` |
| 36 | `_is_dunder` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:28` |
| 37 | `uname` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/platform.py:767` |
| 38 | `__new__` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:635` |
| 39 | `_exact_ratio` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/statistics.py:235` |
| 40 | `_register` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/importlib/abc.py:21` |
| 41 | `__delitem__` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/os.py:688` |
| 42 | `groups` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:83` |
| 43 | `seek_next_non_empty_line` | 0.001s | 0.05% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/vendored/docscrape.py:65` |
| 44 | `__call__` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:339` |
| 45 | `InfinityType` | 0.001s | 0.05% | `/testbed/pandas/util/version/__init__.py:39` |
| 46 | `_decorate_compute_function` | 0.001s | 0.05% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/compute.py:165` |
| 47 | `_compile` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:131` |
| 48 | `SparseDtype` | 0.001s | 0.05% | `/testbed/pandas/core/arrays/sparse/dtype.py:174` |
| 49 | `construct_from_string` | 0.001s | 0.05% | `/testbed/pandas/core/dtypes/dtypes.py:900` |
| 50 | `_display_as_base` | 0.001s | 0.05% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/core/_exceptions.py:27` |
| 51 | `__setitem__` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:110` |
| 52 | `__getitem__` | 0.001s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/calendar.py:82` |
| 53 | `PandasExtensionDtype` | 0.001s | 0.05% | `/testbed/pandas/core/dtypes/dtypes.py:106` |

Self time and sampled percentage are per run, averaged over the repetitions.
