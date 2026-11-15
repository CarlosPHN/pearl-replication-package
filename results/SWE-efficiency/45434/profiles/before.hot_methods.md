# Methods of the workload by self time (before)

Mean of 10 repetitions of the same benchmark.
Each repetition got its own profile file.

Profiles: /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.before.run1.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.before.run2.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.before.run3.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.before.run4.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.before.run5.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.before.run6.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.before.run7.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.before.run8.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.before.run9.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/pandas-dev__pandas-45434.before.run10.speedscope.json
Sampled: 6.216s per run across 6.175s of code frames (0.041s of profiler overhead)
Ranking: all

Percentages are of the sampled time, not of the benchmark run: py-spy sampled 6.216s per run. The 64 methods below account for 6.0s, 96.46% of the profile.

| # | method | self time | sampled | where |
| - | ------ | --------- | ------- | ----- |
| 1 | `coerce_to_array` | 4.5s | 72.39% | `/testbed/pandas/core/arrays/integer.py:182` |
| 2 | `setup` | 0.541s | 8.7% | `/home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-45434/workload.py:10` |
| 3 | `_values_for_argsort` | 0.434s | 6.98% | `/testbed/pandas/core/arrays/integer.py:318` |
| 4 | `_amin` | 0.395s | 6.35% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/core/_methods.py:45` |
| 5 | `_any` | 0.027s | 0.43% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/core/_methods.py:58` |
| 6 | `dedent` | 0.019s | 0.31% | `/opt/miniconda3/envs/testbed/lib/python3.8/textwrap.py:430` |
| 7 | `sub` | 0.006s | 0.1% | `/opt/miniconda3/envs/testbed/lib/python3.8/re.py:210` |
| 8 | `_execute_child` | 0.004s | 0.06% | `/opt/miniconda3/envs/testbed/lib/python3.8/subprocess.py:1655` |
| 9 | `construct_from_string` | 0.003s | 0.05% | `/testbed/pandas/core/dtypes/dtypes.py:755` |
| 10 | `namedtuple` | 0.003s | 0.05% | `/opt/miniconda3/envs/testbed/lib/python3.8/collections/__init__.py:454` |
| 11 | `getargs` | 0.002s | 0.03% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/compat/_inspect.py:92` |
| 12 | `__new__` | 0.002s | 0.03% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:193` |
| 13 | `find` | 0.002s | 0.03% | `/testbed/pandas/core/dtypes/base.py:492` |
| 14 | `_parse` | 0.002s | 0.03% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:506` |
| 15 | `_compile` | 0.002s | 0.03% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:209` |
| 16 | `array` | 0.002s | 0.03% | `/testbed/pandas/core/construction.py:309` |
| 17 | `_register_known_types` | 0.002s | 0.03% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/core/getlimits.py:275` |
| 18 | `StringMethods` | 0.002s | 0.03% | `/testbed/pandas/core/strings/accessor.py:2951` |
| 19 | `find_spec` | 0.002s | 0.03% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/__init__.py:109` |
| 20 | `__new__` | 0.002s | 0.03% | `/opt/miniconda3/envs/testbed/lib/python3.8/abc.py:86` |
| 21 | `compile` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:777` |
| 22 | `verify_matching_signatures` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/core/overrides.py:96` |
| 23 | `__get_openssl_constructor` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/hashlib.py:131` |
| 24 | `_set_tzdata` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/tz/tz.py:486` |
| 25 | `__call__` | 0.001s | 0.02% | `/testbed/pandas/util/_decorators.py:489` |
| 26 | `_communicate` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/subprocess.py:1907` |
| 27 | `__init__` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/masked.py:150` |
| 28 | `_compile` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/re.py:312` |
| 29 | `set_num_threads` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/utils.py:110` |
| 30 | `SparseDtype` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/sparse/dtype.py:174` |
| 31 | `_make_global_functions` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/compute.py:323` |
| 32 | `_signature_from_function` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:2184` |
| 33 | `addpackage` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/site.py:168` |
| 34 | `<setcomp>` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:203` |
| 35 | `validate` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/logging/__init__.py:432` |
| 36 | `_make_signature` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/compute.py:272` |
| 37 | `_deepcopy_dict` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/copy.py:230` |
| 38 | `from_callable` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:2854` |
| 39 | `__init__` | 0.001s | 0.02% | `/testbed/pandas/core/arrays/integer.py:296` |
| 40 | `timeit` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/timeit.py:175` |
| 41 | `_find_new_` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:606` |
| 42 | `decorator` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/core/overrides.py:177` |
| 43 | `__init__` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/ma/core.py:6835` |
| 44 | `getdoc` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/ma/extras.py:257` |
| 45 | `_split_chunks` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/textwrap.py:338` |
| 46 | `ismethod` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/compat/_inspect.py:24` |
| 47 | `split` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/re.py:231` |
| 48 | `get_object_signature` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/ma/core.py:137` |
| 49 | `getwidth` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:180` |
| 50 | `__next` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:248` |
| 51 | `_parse` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/vendored/docscrape.py:403` |
| 52 | `wrapper` | 0.001s | 0.02% | `/testbed/pandas/core/indexes/extension.py:128` |
| 53 | `update_wrapper` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/functools.py:57` |
| 54 | `_optimize_charset` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:302` |
| 55 | `_collect_type_vars` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:182` |
| 56 | `_parse_sub` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:445` |
| 57 | `decorator` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/util.py:76` |
| 58 | `Index` | 0.001s | 0.02% | `/testbed/pandas/core/indexes/base.py:5919` |
| 59 | `is_unindented` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/vendored/docscrape.py:94` |
| 60 | `_create_fn` | 0.001s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/dataclasses.py:398` |
| 61 | `_wrapreduction` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/core/fromnumeric.py:86` |
| 62 | `_is_dtype_type` | 0.001s | 0.02% | `/testbed/pandas/core/dtypes/common.py:1628` |
| 63 | `_decorate_compute_function` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/compute.py:124` |
| 64 | `dedent_lines` | 0.001s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-45434/testbed/vendored/docscrape.py:560` |

Self time and sampled percentage are per run, averaged over the repetitions.
