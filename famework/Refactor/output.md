# Refactor Agent — Output

## State fields updated

- `refactor_report`: YAML string with the applied changes.

## Output structure

```yaml
refactor_report:
  changes:
    - method: "<method name>"
      path: "<absolute path>"
      line: <line number>
      before: "<original code>"
      after: "<refactored code>"
      addresses: "<which smell this addresses>"
      results: "<what the change achieves>"
  skipped:
    - method: "<method name>"
      reason: "<reason for skipping>"
  files_modified:
    - "<absolute path>"
  summary: "<overall summary>"
```

## Validation rules applied

- `changes` must be a list of mappings with `method`, `path`, `line`, `before`, `after`, `addresses`, and `results`.
- `skipped` must be a list of mappings with `method` and `reason`.
- `files_modified` must be a list of absolute paths.
- `summary` must be a string.

## Example output (SWE-fficiency instance 43589)

```yaml
refactor_report:
  changes:
    - method: equals
      path: /home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/pandas/core/indexes/multi.py
      line: 3547
      before: "for i in range(self.nlevels):\n    self_codes = self.codes[i]\n    other_codes = other.codes[i]\n    self_level = self.levels[i]\n    other_level = other.levels[i]\n    ..."
      after: "self_codes_all = self.codes\nother_codes_all = other.codes\nself_levels = self.levels\nother_levels = other.levels\n\nfor self_codes, other_codes, self_level, other_level in zip(\n    self_codes_all, other_codes_all, self_levels, other_levels\n):\n    ..."
      addresses: "C3.S1 — Inefficient Iteration Construct"
      results: "Caches code and level sequences and iterates with zip to avoid repeated indexing and property lookups."
  skipped: []
  files_modified:
    - /home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/pandas/core/indexes/multi.py
  summary: "Cached codes and levels and replaced range-based indexing with zip iteration in MultiIndex.equals."
```
