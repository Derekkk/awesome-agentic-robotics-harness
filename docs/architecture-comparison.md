# Architecture and interface comparison

This table summarizes mechanisms from the original abstracts and project pages checked during this review. It is not a complete implementation specification. Exact action dimensions, coordinate systems, network architectures, and execution frequencies require reading the full papers and code.

| Approach | Examples | Reasoning output / interface | Low-level execution | What persists across tasks | Key comparison factors |
|---|---|---|---|---|---|
| Code and analytical tools | CaP-X, ASPIRE | Programs calling perception and control primitives | Tools and control stack | Programs, skills, and experience; CaP-RL also trains parameters | Tool access and human-designed priors |
| Frozen VLA orchestration | Harness VLA | Analytical primitives and local VLA calls | Frozen VLA + analytical tools | Task trajectories, rules, and failure models | Frozen components and original VLA training distribution |
| Semantic action interpreter | Show-Harness | Discrete semantic action units | Embodiment-specific deterministic interpreter | Depends on the zero-shot / fine-tuned configuration | Action granularity, quantization, and interface priors |
| Deployment-time ICL | GPT-Policy | Context-conditioned robot tool actions | Constrained controller | Current context; the abstract does not claim parameter updates | Demonstration information, feedback, and budget |
| Explicit plan-driven execution | PLanAR | Symbolic plans with predicates and effects | Skill execution and stepwise checks | State and plan records | Symbol grounding and condition verification |
| End-to-end fast and slow systems | OneTwoVLA, FiS, LaST0, StreamVLA | Textual / latent reasoning conditions and actions | Trained action modules | Parameters; deployment state varies by method | Training cost, switching, and latency |
| Context-driven fast and slow systems | PonderPounce | Latest cognition token + age | Jointly trained Pounce | Native episode context | Information freshness and asynchronous latency |
| Memory compressed into plans | MaP-WAM | Segment-level language plans and visual guidance | WAP action and progress prediction | Episodic segment records | Separate accounting for planning and execution costs |
| Runtime governance | Zetta, PhyAgentOS | Critic/recovery or session scheduling | Policy/skills + verification layer | Validated experience and code | First-failure detection and update regressions |
| Fleet parameter updates | LWD | Deployment policy and training feedback loop | Generalist VLA | Shared policy parameters | Data volume, task count, and fleet heterogeneity |

## Design questions when keeping the VLA unchanged

- With reliable local contact skills, study Harness VLA-style orchestration, state acceptance checks, and memory.
- With reliable pose, grasp, and motion-planning tools, explore code-as-policy while recording the priors and errors these tools introduce.
- To test the physical decision-making ability of a general-purpose VLM directly, semantic action interpreters or constrained tool interfaces make interface effects easier to study. Do not attribute low-level controller contributions to the VLM.
- For long histories, compare explicit state/memory with full history before training a cognition interface; the latter changes more than the surrounding system.

These are mechanism-based research design suggestions, not performance rankings established by experiments.
