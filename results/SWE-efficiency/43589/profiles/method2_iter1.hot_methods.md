# Methods of the workload by self time (method2_iter1)

Mean of 10 repetitions of the same benchmark.
Each repetition got its own profile file.

Profiles: /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method2_iter1.run1.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method2_iter1.run2.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method2_iter1.run3.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method2_iter1.run4.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method2_iter1.run5.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method2_iter1.run6.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method2_iter1.run7.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method2_iter1.run8.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method2_iter1.run9.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.method2_iter1.run10.speedscope.json
Sampled: 17.969s per run across 17.933s of code frames (0.036s of profiler overhead)
Ranking: all

Percentages are of the sampled time, not of the benchmark run: py-spy sampled 17.969s per run. The 69 methods below account for 17.8s, 99.04% of the profile.

| # | method | self time | sampled | where |
| - | ------ | --------- | ------- | ----- |
| 1 | `__array__` | 8.437s | 46.95% | `/testbed/pandas/core/arrays/datetimelike.py:316` |
| 2 | `__iter__` | 7.854s | 43.71% | `/testbed/pandas/core/arrays/datetimes.py:625` |
| 3 | `equals` | 0.751s | 4.18% | `/testbed/pandas/core/indexes/multi.py:3547` |
| 4 | `_array_equivalent_object` | 0.579s | 3.22% | `/testbed/pandas/core/dtypes/missing.py:484` |
| 5 | `take` | 0.038s | 0.21% | `/testbed/pandas/core/algorithms.py:1522` |
| 6 | `workload` | 0.028s | 0.16% | `/home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/workload.py:13` |
| 7 | `dedent` | 0.015s | 0.08% | `/opt/miniconda3/envs/testbed/lib/python3.8/textwrap.py:430` |
| 8 | `DataFrame` | 0.005s | 0.03% | `/testbed/pandas/core/frame.py:7169` |
| 9 | `update_wrapper` | 0.004s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/functools.py:57` |
| 10 | `sub` | 0.004s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/re.py:210` |
| 11 | `__init__` | 0.003s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:2824` |
| 12 | `__new__` | 0.003s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/abc.py:85` |
| 13 | `__new__` | 0.003s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:193` |
| 14 | `classes` | 0.003s | 0.02% | `/testbed/pandas/core/dtypes/common.py:147` |
| 15 | `array_equal` | 0.003s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/numeric.py:2468` |
| 16 | `_parse_param_list` | 0.002s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/vendored/docscrape.py:247` |
| 17 | `asi8` | 0.002s | 0.01% | `/testbed/pandas/core/arrays/datetimelike.py:291` |
| 18 | `__getitem__` | 0.002s | 0.01% | `/testbed/pandas/core/indexes/frozen.py:70` |
| 19 | `_make_signature` | 0.002s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compute.py:279` |
| 20 | `getargs` | 0.002s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compat/_inspect.py:79` |
| 21 | `_execute_child` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/subprocess.py:1655` |
| 22 | `deepcopy` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/copy.py:138` |
| 23 | `array_equivalent` | 0.002s | 0.01% | `/testbed/pandas/core/dtypes/missing.py:418` |
| 24 | `_add_filter` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/warnings.py:186` |
| 25 | `_create_fn` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/dataclasses.py:398` |
| 26 | `take` | 0.002s | 0.01% | `/testbed/pandas/core/arrays/_mixins.py:113` |
| 27 | `__get_openssl_constructor` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/hashlib.py:131` |
| 28 | `_all` | 0.002s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/_methods.py:64` |
| 29 | `getwidth` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:220` |
| 30 | `create_pandas_abc_type` | 0.001s | 0.01% | `/testbed/pandas/core/dtypes/generic.py:48` |
| 31 | `_signature_from_function` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:2154` |
| 32 | `__class_getitem__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:892` |
| 33 | `_optimize_charset` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:298` |
| 34 | `seek_next_non_empty_line` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/vendored/docscrape.py:67` |
| 35 | `extend_all` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/numeric.py:2539` |
| 36 | `_compile` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:148` |
| 37 | `_signature_get_user_defined_method` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:1726` |
| 38 | `_wrap_function` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compute.py:302` |
| 39 | `_name_get` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/_dtype.py:355` |
| 40 | `_with_infer` | 0.001s | 0.01% | `/testbed/pandas/core/indexes/base.py:658` |
| 41 | `_reset_identity` | 0.001s | 0.01% | `/testbed/pandas/core/indexes/base.py:810` |
| 42 | `communicate` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/subprocess.py:1015` |
| 43 | `_parse` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/vendored/docscrape.py:388` |
| 44 | `_read_sections` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/vendored/docscrape.py:219` |
| 45 | `_decorate_compute_function` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compute.py:124` |
| 46 | `needs_i8_conversion` | 0.001s | 0.01% | `/testbed/pandas/core/dtypes/common.py:1187` |
| 47 | `_uniq` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:433` |
| 48 | `inner` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/contextlib.py:75` |
| 49 | `__init__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:500` |
| 50 | `__delitem__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/os.py:685` |
| 51 | `get` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:254` |
| 52 | `eof` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/vendored/docscrape.py:72` |
| 53 | `__array__` | 0.001s | 0.01% | `/testbed/pandas/core/arrays/datetimes.py:599` |
| 54 | `__hash__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:722` |
| 55 | `_compile` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/re.py:304` |
| 56 | `LocaleTextCalendar` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/calendar.py:581` |
| 57 | `unwrap` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:515` |
| 58 | `__enter__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/warnings.py:459` |
| 59 | `__new__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/fractions.py:182` |
| 60 | `_ss` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/statistics.py:694` |
| 61 | `isstring` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:596` |
| 62 | `_parse` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:855` |
| 63 | `compile` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:770` |
| 64 | `__getitem__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/calendar.py:63` |
| 65 | `_parse_summary` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/vendored/docscrape.py:371` |
| 66 | `DatetimeIndex` | 0.001s | 0.01% | `/testbed/pandas/core/indexes/datetimes.py:291` |
| 67 | `cartesian_product` | 0.001s | 0.01% | `/testbed/pandas/core/reshape/util.py:39` |
| 68 | `is_` | 0.001s | 0.01% | `/testbed/pandas/core/indexes/base.py:796` |
| 69 | `tz` | 0.001s | 0.01% | `/testbed/pandas/core/arrays/datetimes.py:563` |

Self time and sampled percentage are per run, averaged over the repetitions.
