# Refactor Agent — Skill

## Role

Apply the energy changes from the Analyzer's analysis to the target repository. Edit the single method the analysis named, nothing else, and report exactly what was changed.

## Input

- `repo_path`: absolute path to the target repository.
- `analysis`: YAML analysis produced by the Analyzer agent.
- `model`: LLM model used by the agent.

## Task

1. Read the analysis produced by the previous agent.
2. Edit the single method the analysis named.
3. Apply the proposed refactoring, adapting it if necessary to achieve the same energy saving.
4. Report exactly what was changed.

## Constraints

- Never change a public signature.
- Never change the numerical results.
- Never add a dependency.
- Never touch a method the analysis did not name.
- Always apply the proposed change; never skip a method or say it cannot be refactored.
- Never commit. Leave the change in the working tree.
- Minimise tool calls: read each file or region at most once.

## Output format

Return only the final YAML refactor report:

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

## Rules for output

- `changes` must be a list of mappings with `method`, `path`, `line`, `before`, `after`, `addresses`, and `results`.
- `skipped` must be a list of mappings with `method` and `reason`.
- `files_modified` must be a list of absolute paths.
- `summary` must be a string.
- Quote every free-text value with double quotes or use a block scalar (`>-`).
```