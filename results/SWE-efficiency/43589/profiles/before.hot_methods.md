# Methods of the workload by self time (before)

Mean of 10 repetitions of the same benchmark.
Each repetition got its own profile file.

Profiles: /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.before.run1.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.before.run2.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.before.run3.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.before.run4.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.before.run5.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.before.run6.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.before.run7.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.before.run8.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.before.run9.speedscope.json, /home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/pandas-dev__pandas-43589.before.run10.speedscope.json
Sampled: 17.239s per run across 17.177s of code frames (0.062s of profiler overhead)
Ranking: all

Percentages are of the sampled time, not of the benchmark run: py-spy sampled 17.239s per run. The 69 methods below account for 17.0s, 98.6% of the profile.

| # | method | self time | sampled | where |
| - | ------ | --------- | ------- | ----- |
| 1 | `__array__` | 8.168s | 47.38% | `/testbed/pandas/core/arrays/datetimelike.py:316` |
| 2 | `__iter__` | 7.375s | 42.78% | `/testbed/pandas/core/arrays/datetimes.py:626` |
| 3 | `equals` | 0.687s | 3.99% | `/testbed/pandas/core/indexes/multi.py:3547` |
| 4 | `_array_equivalent_object` | 0.575s | 3.34% | `/testbed/pandas/core/dtypes/missing.py:484` |
| 5 | `take` | 0.053s | 0.31% | `/testbed/pandas/core/algorithms.py:1522` |
| 6 | `workload` | 0.02s | 0.12% | `/home/carlos/Escritorio/greenrefia/profiles/pandas-dev__pandas-43589/workload.py:13` |
| 7 | `array_equal` | 0.016s | 0.09% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/numeric.py:2468` |
| 8 | `dedent` | 0.011s | 0.06% | `/opt/miniconda3/envs/testbed/lib/python3.8/textwrap.py:431` |
| 9 | `tz` | 0.004s | 0.02% | `/testbed/pandas/core/arrays/datetimes.py:563` |
| 10 | `_execute_child` | 0.003s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/subprocess.py:1655` |
| 11 | `sub` | 0.003s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/re.py:210` |
| 12 | `_all` | 0.003s | 0.02% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/_methods.py:64` |
| 13 | `__exit__` | 0.003s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/warnings.py:483` |
| 14 | `namedtuple` | 0.003s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/collections/__init__.py:456` |
| 15 | `_add_filter` | 0.003s | 0.02% | `/opt/miniconda3/envs/testbed/lib/python3.8/warnings.py:189` |
| 16 | `DataFrame` | 0.003s | 0.02% | `/testbed/pandas/core/frame.py:7169` |
| 17 | `array_equivalent` | 0.003s | 0.02% | `/testbed/pandas/core/dtypes/missing.py:418` |
| 18 | `_optimize_charset` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:395` |
| 19 | `__get_openssl_constructor` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/hashlib.py:131` |
| 20 | `__new__` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/abc.py:86` |
| 21 | `__next` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:240` |
| 22 | `__call__` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:339` |
| 23 | `__init__` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:2788` |
| 24 | `verify_matching_signatures` | 0.002s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/overrides.py:97` |
| 25 | `__init__` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:80` |
| 26 | `_compile` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:90` |
| 27 | `__init__` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:500` |
| 28 | `_push_exit_callback` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/contextlib.py:464` |
| 29 | `_parse` | 0.002s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:535` |
| 30 | `__array__` | 0.002s | 0.01% | `/testbed/pandas/core/arrays/datetimes.py:599` |
| 31 | `formatargspec` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compat/_inspect.py:160` |
| 32 | `__init__` | 0.001s | 0.01% | `/testbed/pandas/util/version/__init__.py:339` |
| 33 | `Index` | 0.001s | 0.01% | `/testbed/pandas/core/indexes/base.py:4010` |
| 34 | `asi8` | 0.001s | 0.01% | `/testbed/pandas/core/arrays/datetimelike.py:291` |
| 35 | `take` | 0.001s | 0.01% | `/testbed/pandas/core/arrays/_mixins.py:122` |
| 36 | `_type_check` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:146` |
| 37 | `SelectionMixin` | 0.001s | 0.01% | `/testbed/pandas/core/base.py:198` |
| 38 | `unwrap` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:520` |
| 39 | `add_newdoc` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/function_base.py:532` |
| 40 | `__new__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/enum.py:283` |
| 41 | `_scrape_options_class_doc` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compute.py:118` |
| 42 | `contextmanager` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/contextlib.py:239` |
| 43 | `is_dtype` | 0.001s | 0.01% | `/testbed/pandas/core/dtypes/base.py:292` |
| 44 | `freq` | 0.001s | 0.01% | `/testbed/pandas/core/arrays/datetimelike.py:905` |
| 45 | `dtype` | 0.001s | 0.01% | `/testbed/pandas/core/arrays/datetimes.py:550` |
| 46 | `_strip` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/vendored/docscrape.py:199` |
| 47 | `_is_at_section` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/vendored/docscrape.py:182` |
| 48 | `_generate_range` | 0.001s | 0.01% | `/testbed/pandas/core/arrays/datetimes.py:409` |
| 49 | `is_` | 0.001s | 0.01% | `/testbed/pandas/core/indexes/base.py:798` |
| 50 | `_mk_bitmap` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:413` |
| 51 | `_is_dunder` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:647` |
| 52 | `_wrapfunc` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/core/fromnumeric.py:57` |
| 53 | `tile` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/lib/shape_base.py:1278` |
| 54 | `compile` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_compile.py:783` |
| 55 | `__hash__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:722` |
| 56 | `create_pandas_abc_type` | 0.001s | 0.01% | `/testbed/pandas/core/dtypes/generic.py:49` |
| 57 | `_uniq` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/sre_parse.py:433` |
| 58 | `_cmpkey` | 0.001s | 0.01% | `/testbed/pandas/util/version/__init__.py:546` |
| 59 | `_collect_type_vars` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/typing.py:182` |
| 60 | `__enter__` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/warnings.py:463` |
| 61 | `isfunction` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:169` |
| 62 | `codes` | 0.001s | 0.01% | `/testbed/pandas/core/indexes/multi.py:954` |
| 63 | `filterwarnings` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/warnings.py:142` |
| 64 | `forbid_nonstring_types` | 0.001s | 0.01% | `/testbed/pandas/core/strings/accessor.py:107` |
| 65 | `ismethod` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/compat/_inspect.py:13` |
| 66 | `cleandoc` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:631` |
| 67 | `_sanity_check` | 0.001s | 0.01% | `/home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/__init__.py:348` |
| 68 | `BaseStringArrayMethods` | 0.001s | 0.01% | `/testbed/pandas/core/strings/base.py:123` |
| 69 | `_signature_is_functionlike` | 0.001s | 0.01% | `/opt/miniconda3/envs/testbed/lib/python3.8/inspect.py:1862` |

Self time and sampled percentage are per run, averaged over the repetitions.
