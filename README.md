# PEARL: Profiling-guided Energy-Aware Refactoring with LLMs

## Abstract

Code optimization can reduce the energy consumption of existing information systems, yet energy efficiency remains difficult to integrate into software maintenance. Although LLMs enable automated refactoring, runtime energy measurements are rarely used systematically to guide and refine code transformations.

To address this gap, we propose PEARL (Profiling-guided Energy-Aware Refactoring with LLMs), a multi-agent framework for energy-aware, method-level refactoring. The Analyzer agent uses a taxonomy of energy smells to detect and classify optimization opportunities, while Retrieval-Augmented Generation (RAG) retrieves related refactoring examples to guide transformations. The Refactoring agent generates candidate changes, which are checked for functional correctness and evaluated through runtime energy measurements. These results guide iterative refinement toward refactorings that reduce energy consumption while preserving program behavior.

We evaluate PEARL on four selected Pandas instances from the SWE-fficiency benchmark, which comprises optimization tasks from real-world Python repositories. PEARL produces accepted, functionally correct refactorings in three of the four instances, reducing measured workload energy by 4.44% to 67.15%.
