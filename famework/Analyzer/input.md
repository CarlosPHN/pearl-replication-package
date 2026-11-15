# Analyzer Agent — Input

## State fields

- `test_scope`: scope to analyze (e.g., `pandas-dev__pandas-43589`).
- `repo_path`: absolute path to the target repository.
- `profile_ranking`: profiler ranking of hot methods (YAML), with `self_seconds` and `percent`.
- `selected_method`: if set, restricts analysis to this single method.
- `discarded_methods`: methods already discarded in previous iterations.
- `tried_methods`: methods already attempted.
- `analysis`: previous analysis output (YAML), used to detect method changes.
- `model_pool`: available LLM models.

## Additional inputs loaded from disk

- `taxonomy.md`: catalog of energy smells used to classify the detected smell.
- `load_past_comparisons`: previous iteration results for the same repository and scope.

## Prompt input (constructed by `_analyzer_prompt`)

### Measured methods (from profile ranking)

```
A profiler measured this scope and produced the ranking of its hottest methods, already
filtered to this scope:

  1. `equals` at `/testbed/pandas/core/indexes/multi.py:3547`
     measured_self_seconds: 0.687
     measured_percent: 3.99

Choose exactly one method from the ranking above to analyse. Pick the one with the highest
measured self time that has not already been refactored in a previous iteration.
Report the two measured values as bare numbers, exactly as printed above.
Report one energy smell for this method, pointing at the line it was found in.
```

### Past section (if available)

```
Previous iterations in this repository and scope:

<past_comparisons>

Do not propose changes to methods that already did not improve in a previous iteration
unless you can justify why a different approach would succeed where the previous one
failed.

The following methods have already been attempted in previous passes and must NOT be
proposed again, even if they reappear in the profile ranking:

  - `<method>`
```

### Taxonomy section (if taxonomy.md exists)

```
Use the following energy smells taxonomy to classify each smell you find. Each smell must
match one of the categories and subcategories defined here:

<taxonomy content>
```

### Similar section

```
Before you propose a change, query the refactoring collection with the
`search_energy_refactorings` tool. Pass a short description of the inefficiency in the
method you are reading, not the method name and not the whole file. The tool returns the
most similar refactorings that measurably reduced energy, with their code before and after
and the energy they saved. Use them to see what kind of change has worked on similar code,
and let them inform your proposal.
```

### Constraints (always included)

```
Work only from the methods named above. Read the specific region of the file each one
points at, plus the few lines around it needed to understand it.

Minimise tool calls: read each file region at most once, never reopen a file you have
already read, never repeat a glob/grep or a search_energy_refactorings query, and batch
independent reads instead of issuing them one at a time.

Every proposal must preserve the public signature and the numerical results, must be
implementable in the file you point at, and must not need a new dependency.

Return only the final YAML analysis defined by the skill.
```

## Example input (profile ranking)

```yaml
profile_ranking:
  profile_usable: true
  repetitions_averaged: 10
  hot_functions:
    - method: equals
      file: /testbed/pandas/core/indexes/multi.py
      line: 3547
      self_seconds: 0.687
      percent: 3.99
```
