# PEARL: Profiling-guided Energy-Aware Refactoring with LLMs

This replication package contains the materials for reproducing the evaluation of PEARL, a multi-agent framework for profiling-guided, energy-aware refactoring.

## Abstract

Code optimization can reduce the energy consumption of existing information systems, yet energy efficiency remains difficult to integrate into software maintenance. Although LLMs enable automated refactoring, runtime energy measurements are rarely used systematically to guide and refine code transformations.

To address this gap, we propose PEARL (Profiling-guided Energy-Aware Refactoring with LLMs), a multi-agent framework for energy-aware, method-level refactoring. The Analyzer agent uses a taxonomy of energy smells to detect and classify optimization opportunities, while Retrieval-Augmented Generation (RAG) retrieves related refactoring examples to guide transformations. The Refactoring agent generates candidate changes, which are checked for functional correctness and evaluated through runtime energy measurements. These results guide iterative refinement toward refactorings that reduce energy consumption while preserving program behavior.

We evaluate PEARL on four selected Pandas instances from the SWE-fficiency benchmark, which comprises optimization tasks from real-world Python repositories. PEARL generates functionally correct refactorings for all four instances, with accepted energy reductions in three, ranging from 4.44% to 67.15%.

## Package structure

```text
PEARL-replication-package/
├── framework/
├── energy-smells/
└── results/
```

- **`framework/`** — Descriptions of the PEARL agents, including their inputs, outputs, and skills.

- **`energy-smells/`** — The language-agnostic energy-smell taxonomy and its associated dataset, introduced by Mehditabar et al. in [*Watts This Smell: A Comprehensive Taxonomy of Software Energy Smells*](https://arxiv.org/abs/2604.04809). Energy smells are code patterns that can lead to inefficient energy use. The taxonomy classifies them by their characteristics and underlying causes. The dataset contains Python functions annotated with the taxonomy and their corresponding mitigation strategies. PEARL uses the taxonomy to identify and classify potential energy smells, and queries the dataset through RAG to retrieve relevant examples that guide refactoring.

- **`results/`** — Contains the evaluation results for both the pilot case study and the four selected Pandas instances from SWE-fficiency.
