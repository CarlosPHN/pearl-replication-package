# Refactor Agent — Input

## State fields

- `repo_path`: absolute path to the target repository.
- `analysis`: YAML analysis produced by the Analyzer agent.
- `model`: LLM model used by the agent.

## Prompt input (constructed by `_refactor_prompt`)

```
Apply the energy changes from this analysis to the target repository, using the refactor skill.

Target repository:
<repo_path>

Scope:
<test_scope>

Analysis produced by the previous agent:
<analysis YAML>

Do only what the skill tells you: edit the single method the analysis named, nothing else,
and report exactly what you changed.

Minimise tool calls: read each file or region at most once, never reopen something you
have already read, never repeat a search, and only call a tool when the information is not
already in the analysis or in code you have read.

Never change a public signature, never change the numerical results, never add a
dependency, and never touch a method the analysis did not name. Always apply the proposed
change: never skip a method or say it cannot be refactored. If the exact proposal is not
applicable, adapt it to an equivalent change that achieves the same energy saving.

Never commit. Leave the change in the working tree.

Return only the final YAML refactor report defined by the skill.
```
