# Methods of the workload by self time (iter1)

Mean of 10 repetitions of the same benchmark.
Each repetition got its own profile file.

Profiles: /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.iter1.run1.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.iter1.run2.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.iter1.run3.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.iter1.run4.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.iter1.run5.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.iter1.run6.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.iter1.run7.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.iter1.run8.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.iter1.run9.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.iter1.run10.speedscope.json
Sampled: 37.859s per run across 37.818000000000005s of code frames (0.041s of profiler overhead)
Ranking: all

Percentages are of the sampled time, not of the benchmark run: py-spy sampled 37.859s per run. The 81 methods below account for 37.7s, 99.59% of the profile.

| # | method | self time | sampled | where |
| - | ------ | --------- | ------- | ----- |
| 1 | `_box_func` | 29.332s | 77.48% | `/testbed/pandas/core/arrays/datetimes.py:518` |
| 2 | `_box_values` | 2.779s | 7.34% | `/testbed/pandas/core/arrays/datetimelike.py:272` |
| 3 | `tz` | 2.209s | 5.83% | `/testbed/pandas/core/arrays/datetimes.py:563` |
| 4 | `dtype` | 0.838s | 2.21% | `/testbed/pandas/core/arrays/datetimes.py:550` |
| 5 | `tz` | 0.74s | 1.95% | `/testbed/pandas/core/dtypes/dtypes.py:723` |
| 6 | `equals` | 0.685s | 1.81% | `/testbed/pandas/core/indexes/multi.py:3547` |
| 7 | `_array_equivalent_object` | 0.611s | 1.61% | `/testbed/pandas/core/dtypes/missing.py:484` |
| 8 | `freq` | 0.305s | 0.81% | `/testbed/pandas/core/arrays/datetimelike.py:905` |
| 9 | `take` | 0.044s | 0.12% | `/testbed/pandas/core/algorithms.py:1522` |
| 10 | `workload` | 0.029s | 0.08% | `/home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/workload.py:13` |
| 11 | `dedent` | 0.02s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/textwrap.py:431` |
| 12 | `DataFrame` | 0.009s | 0.02% | `/testbed/pandas/core/frame.py:7169` |
| 13 | `array_equal` | 0.008s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/numeric.py:2468` |
| 14 | `_all` | 0.005s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/_methods.py:64` |
| 15 | `sub` | 0.005s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/re.py:210` |
| 16 | `_execute_child` | 0.005s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/subprocess.py:1655` |
| 17 | `update_wrapper` | 0.003s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/functools.py:60` |
| 18 | `read_to_condition` | 0.003s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/vendored/docscrape.py:77` |
| 19 | `array_equivalent` | 0.003s | 0.01% | `/testbed/pandas/core/dtypes/missing.py:418` |
| 20 | `decorator` | 0.002s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/overrides.py:204` |
| 21 | `namedtuple` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/collections/__init__.py:456` |
| 22 | `getargs` | 0.002s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compat/_inspect.py:85` |
| 23 | `_optimize_charset` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:396` |
| 24 | `__new__` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/abc.py:85` |
| 25 | `__array__` | 0.002s | 0.01% | `/testbed/pandas/core/arrays/datetimelike.py:316` |
| 26 | `_parse` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:511` |
| 27 | `__init__` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:500` |
| 28 | `timeit` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/timeit.py:180` |
| 29 | `loads` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/json/__init__.py:335` |
| 30 | `_parse` | 0.001s | 0.0% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/vendored/docscrape.py:388` |
| 31 | `_make_global_functions` | 0.001s | 0.0% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compute.py:323` |
| 32 | `add_newdoc` | 0.001s | 0.0% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/function_base.py:529` |
| 33 | `Parameter` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:2539` |
| 34 | `_float_to_str` | 0.001s | 0.0% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/getlimits.py:119` |
| 35 | `_generate_range` | 0.001s | 0.0% | `/testbed/pandas/core/arrays/datetimes.py:409` |
| 36 | `iscode` | 0.001s | 0.0% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compat/_inspect.py:59` |
| 37 | `cleandoc` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:631` |
| 38 | `_uniq` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:433` |
| 39 | `__new__` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:256` |
| 40 | `partialmethod` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/functools.py:424` |
| 41 | `_timelex` | 0.001s | 0.0% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/parser/_parser.py:204` |
| 42 | `__next` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:240` |
| 43 | `ObjectStringArrayMixin` | 0.001s | 0.0% | `/testbed/pandas/core/strings/object_array.py:208` |
| 44 | `_joinrealpath` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/posixpath.py:411` |
| 45 | `_compile` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:82` |
| 46 | `_compile` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/re.py:294` |
| 47 | `__init__` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:2824` |
| 48 | `split` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/re.py:231` |
| 49 | `_is_sunder` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:39` |
| 50 | `_decorate_compute_function` | 0.001s | 0.0% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compute.py:150` |
| 51 | `asi8` | 0.001s | 0.0% | `/testbed/pandas/core/arrays/datetimelike.py:291` |
| 52 | `_convert` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/statistics.py:261` |
| 53 | `getargspec` | 0.001s | 0.0% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compat/_inspect.py:110` |
| 54 | `match` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:251` |
| 55 | `_remove_dups_flatten` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:231` |
| 56 | `__setattr__` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:764` |
| 57 | `_wrap_function` | 0.001s | 0.0% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compute.py:304` |
| 58 | `contextmanager` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/contextlib.py:239` |
| 59 | `__init__` | 0.001s | 0.0% | `/testbed/pandas/core/arrays/datetimes.py:255` |
| 60 | `maybe_convert_platform` | 0.001s | 0.0% | `/testbed/pandas/core/dtypes/cast.py:127` |
| 61 | `take` | 0.001s | 0.0% | `/testbed/pandas/core/arrays/_mixins.py:114` |
| 62 | `__call__` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:339` |
| 63 | `needs_i8_conversion` | 0.001s | 0.0% | `/testbed/pandas/core/dtypes/common.py:1177` |
| 64 | `__setattr__` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:428` |
| 65 | `__get_openssl_constructor` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/hashlib.py:131` |
| 66 | `_get_arg_names` | 0.001s | 0.0% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compute.py:108` |
| 67 | `deepcopy` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/copy.py:146` |
| 68 | `_missing_ctypes` | 0.001s | 0.0% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/_internal.py:243` |
| 69 | `escape` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/re.py:275` |
| 70 | `_get_options_class` | 0.001s | 0.0% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compute.py:205` |
| 71 | `get` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/_collections_abc.py:660` |
| 72 | `_strip` | 0.001s | 0.0% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/vendored/docscrape.py:200` |
| 73 | `_make_signature` | 0.001s | 0.0% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compute.py:277` |
| 74 | `_parse_summary` | 0.001s | 0.0% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/vendored/docscrape.py:372` |
| 75 | `_try_wait` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/subprocess.py:1780` |
| 76 | `date_range` | 0.001s | 0.0% | `/testbed/pandas/core/indexes/datetimes.py:1032` |
| 77 | `<setcomp>` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:202` |
| 78 | `__init__` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:225` |
| 79 | `__hash__` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:721` |
| 80 | `getwidth` | 0.001s | 0.0% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:220` |
| 81 | `make_flex_doc` | 0.001s | 0.0% | `/testbed/pandas/core/ops/docstrings.py:53` |

Self time and sampled percentage are per run, averaged over the repetitions.
