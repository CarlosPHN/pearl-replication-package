# Analyzer Agent — Output

## State fields updated

- `analysis`: YAML string with the detected energy smell and proposed refactoring.
- `tried_methods`: updated list of methods already attempted.

## Output structure

```yaml
analysis:
  scope: "<scope>"
  energy_smell:
    - method: "<method name>"
      path: "<absolute path>"
      measured_self_seconds: <number>
      measured_percent: <number>
      type: "<smell type>"
      problem: "<description>"
      energy_impact: "<impact>"
      refactoring: "<proposed change>"
```

## Validation rules applied

- Exactly one energy smell under `energy_smell`.
- `measured_self_seconds` and `measured_percent` must be bare numbers, no units, no percent sign.
- `path` must be an absolute path.
- `method` must belong to the profile ranking (if `allowed_methods` is set).
- Free-text values must be quoted or written as block scalars.
- `refactoring` code must be indented deeper than the key.

## Example output (SWE-fficiency instance 43589)

```yaml
analysis:
  scope: "pandas-dev__pandas-43589"
  energy_smell:
    - method: equals
      path: /home/carlos/.greenrefia/work/pandas-dev__pandas-43589/testbed/pandas/core/indexes/multi.py
      measured_self_seconds: 0.687
      measured_percent: 3.99
      type: "C3.S1 — Inefficient Iteration Construct"
      problem: "The loop uses range(self.nlevels) and re-indexes self.codes, other.codes, self.levels, and other.levels on every iteration, adding avoidable index and property-lookup overhead in a hot path."
      energy_impact: "Removes per-iteration index lookups and repeated property evaluations by iterating directly over the cached code and level sequences."
      refactoring: "self_codes_all = self.codes\nother_codes_all = other.codes\nself_levels = self.levels\nother_levels = other.levels\n\nfor self_codes, other_codes, self_level, other_level in zip(\n    self_codes_all, other_codes_all, self_levels, other_levels\n):\n    self_mask = self_codes == -1\n    other_mask = other_codes == -1\n    if not np.array_equal(self_mask, other_mask):\n        return False\n    self_codes = self_codes[~self_mask]\n    self_values = self_level._values.take(self_codes)\n\n    other_codes = other_codes[~other_mask]\n    other_values = other_level._values.take(other_codes)\n\n    if len(self_values) == 0 and len(other_values) == 0:\n        continue\n\n    if not array_equivalent(self_values, other_values):\n        return False"
```
