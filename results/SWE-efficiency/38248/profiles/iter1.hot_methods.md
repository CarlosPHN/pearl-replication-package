# Methods of the workload by self time (iter1)

Mean of 10 repetitions of the same benchmark.
Each repetition got its own profile file.

Profiles: /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.iter1.run1.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.iter1.run2.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.iter1.run3.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.iter1.run4.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.iter1.run5.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.iter1.run6.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.iter1.run7.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.iter1.run8.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.iter1.run9.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/pandas-dev__pandas-38248.iter1.run10.speedscope.json
Sampled: 6.429s per run across 6.346s of code frames (0.083s of profiler overhead)
Ranking: all

Percentages are of the sampled time, not of the benchmark run: py-spy sampled 6.429s per run. The 69 methods below account for 6.21s, 96.58% of the profile.

| # | method | self time | sampled | where |
| - | ------ | --------- | ------- | ----- |
| 1 | `_cmp_method` | 2.027s | 31.53% | `/testbed/pandas/core/arrays/datetimelike.py:939` |
| 2 | `_isnan` | 1.604s | 24.95% | `/testbed/pandas/core/arrays/datetimelike.py:766` |
| 3 | `_isna_ndarraylike` | 1.556s | 24.2% | `/testbed/pandas/core/dtypes/missing.py:230` |
| 4 | `generate_regular_range` | 0.587s | 9.13% | `/testbed/pandas/core/arrays/_ranges.py:62` |
| 5 | `_any` | 0.108s | 1.68% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/core/_methods.py:58` |
| 6 | `_wrapreduction` | 0.102s | 1.59% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/core/fromnumeric.py:88` |
| 7 | `__lt__` | 0.084s | 1.31% | `/testbed/pandas/core/arraylike.py:37` |
| 8 | `setup` | 0.023s | 0.36% | `/home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/workload.py:12` |
| 9 | `dedent` | 0.01s | 0.16% | `/opt/miniconda3/envs/testbed/lib/python3.10/textwrap.py:438` |
| 10 | `_parse` | 0.007s | 0.11% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_parse.py:854` |
| 11 | `_compile` | 0.005s | 0.08% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_compile.py:90` |
| 12 | `__init__` | 0.004s | 0.06% | `/opt/miniconda3/envs/testbed/lib/python3.10/typing.py:1004` |
| 13 | `_generate_range` | 0.004s | 0.06% | `/testbed/pandas/core/arrays/datetimes.py:376` |
| 14 | `_isna` | 0.004s | 0.06% | `/testbed/pandas/core/dtypes/missing.py:159` |
| 15 | `__setattr__` | 0.004s | 0.06% | `/opt/miniconda3/envs/testbed/lib/python3.10/typing.py:971` |
| 16 | `namedtuple` | 0.004s | 0.06% | `/opt/miniconda3/envs/testbed/lib/python3.10/collections/__init__.py:414` |
| 17 | `create_pandas_abc_type` | 0.003s | 0.05% | `/testbed/pandas/core/dtypes/generic.py:34` |
| 18 | `isna` | 0.003s | 0.05% | `/testbed/pandas/core/dtypes/missing.py:127` |
| 19 | `_validate_comparison_value` | 0.003s | 0.05% | `/testbed/pandas/core/arrays/datetimelike.py:454` |
| 20 | `__new__` | 0.003s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.10/abc.py:106` |
| 21 | `__next` | 0.003s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_parse.py:236` |
| 22 | `_type_check` | 0.003s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.10/typing.py:168` |
| 23 | `_optimize_charset` | 0.003s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_compile.py:396` |
| 24 | `__instancecheck__` | 0.003s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.10/abc.py:119` |
| 25 | `add_newdoc` | 0.002s | 0.03% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/core/function_base.py:543` |
| 26 | `seterr` | 0.002s | 0.03% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/core/_ufunc_config.py:122` |
| 27 | `__len__` | 0.002s | 0.03% | `/testbed/pandas/core/arrays/_mixins.py:108` |
| 28 | `new_method` | 0.002s | 0.03% | `/testbed/pandas/core/ops/common.py:63` |
| 29 | `asi8` | 0.002s | 0.03% | `/testbed/pandas/core/arrays/datetimelike.py:243` |
| 30 | `is_dtype` | 0.002s | 0.03% | `/testbed/pandas/core/dtypes/base.py:280` |
| 31 | `sub` | 0.002s | 0.03% | `/opt/miniconda3/envs/testbed/lib/python3.10/re.py:209` |
| 32 | `addpackage` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/site.py:186` |
| 33 | `_inplace_binary_method` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/lib/mixins.py:40` |
| 34 | `_mk_bitmap` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_compile.py:412` |
| 35 | `formatargspec` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/_utils/_inspect.py:160` |
| 36 | `Fixed` | 0.001s | 0.02% | `/testbed/pandas/io/pytables.py:2625` |
| 37 | `Table` | 0.001s | 0.02% | `/testbed/pandas/io/pytables.py:4067` |
| 38 | `is_object_dtype` | 0.001s | 0.02% | `/testbed/pandas/core/dtypes/common.py:228` |
| 39 | `_MergeOperation` | 0.001s | 0.02% | `/testbed/pandas/core/reshape/merge.py:581` |
| 40 | `_execute_child` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/subprocess.py:1775` |
| 41 | `_communicate` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/subprocess.py:1982` |
| 42 | `_maybe_normalize_endpoints` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/datetimes.py:2346` |
| 43 | `is_string_dtype` | 0.001s | 0.02% | `/testbed/pandas/core/dtypes/common.py:602` |
| 44 | `get` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_parse.py:256` |
| 45 | `__getitem__` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/typing.py:1119` |
| 46 | `any` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/core/fromnumeric.py:2412` |
| 47 | `tz` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/datetimes.py:519` |
| 48 | `_Unpickler` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/pickle.py:1539` |
| 49 | `copy_with` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/typing.py:1063` |
| 50 | `__init__` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_parse.py:116` |
| 51 | `_assert_tzawareness_compat` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/datetimes.py:643` |
| 52 | `needs_i8_conversion` | 0.001s | 0.02% | `/testbed/pandas/core/dtypes/common.py:1226` |
| 53 | `cleandoc` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/inspect.py:765` |
| 54 | `append` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_parse.py:173` |
| 55 | `dtype` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/datetimes.py:506` |
| 56 | `DynamicClassAttribute` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/types.py:185` |
| 57 | `_compile_info` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_compile.py:540` |
| 58 | `Optional` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/typing.py:526` |
| 59 | `view` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/datetimelike.py:378` |
| 60 | `_missing_ctypes` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/core/_internal.py:244` |
| 61 | `_is_dtype_type` | 0.001s | 0.02% | `/testbed/pandas/core/dtypes/common.py:1629` |
| 62 | `workload` | 0.001s | 0.02% | `/home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-38248/workload.py:16` |
| 63 | `tzinfo` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/datetimes.py:534` |
| 64 | `_parse_sub` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.10/sre_parse.py:461` |
| 65 | `_hasnans` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/datetimelike.py:773` |
| 66 | `shape` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/_mixins.py:105` |
| 67 | `decorator` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/core/overrides.py:145` |
| 68 | `find_spec` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-38248/testbed/__init__.py:107` |
| 69 | `DataFrameInfo` | 0.001s | 0.02% | `/testbed/pandas/io/formats/info.py:285` |

Self time and sampled percentage are per run, averaged over the repetitions.
