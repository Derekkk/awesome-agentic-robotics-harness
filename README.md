# Awesome Agentic Robotics & Embodied Harness

> From closed-loop execution to continual learning: a research index of papers, system mechanisms, evaluation, and open questions.

Latest manual review: **2026-09-22** · **36 indexed papers** · See the unverified list for pending entries.

This review primarily checked original abstracts and author project pages, rather than reproducing every paper in full. Each card states its verification scope; research questions and categories reflect maintainer analysis.

## Navigation

- [Research agenda and testable hypotheses](docs/research-agenda.md)
- [Architecture comparison](docs/architecture-comparison.md)
- [Initial review and corrections](reports/2026-09-22.md)
- [Evaluation protocol](docs/evaluation-protocol.md) · [Evidence policy](docs/evidence-policy.md)
- [Daily candidates](docs/inbox.md) · [Unverified leads](docs/unverified.md)
- [Automated updates and publishing](docs/maintenance.md) · [Contributing](CONTRIBUTING.md)
- [JSON data](data/papers.json) · [BibTeX](references.bib)

## Source reconciliation

Coverage of 26 arXiv entries was checked against the original Notion page; see the [source mapping](docs/source-reconciliation.md). The original page and the uploaded attachment contain the same set of paper IDs.

## Scope

This index focuses on how large models make reliable robot decisions through tool interfaces, execution feedback, memory, verification, and learning. It covers frozen VLA orchestration, analytical tools and code-based control, semantic action interpreters, and trained dual-system architectures. General VLA architectures are included only when directly relevant.

Execution, Learning, and Fleet are overlapping organizational perspectives. Multi-agent division of labor, multi-robot collaboration, and shared fleet learning are distinct concepts.

## Categories

| Area | Core question | Entries |
|---|---|---:|
| [Closed-loop execution and tool interfaces](#execution) | What does the reasoning model output, how do tools connect to controllers, and when should the system observe and replan? | 15 |
| [Long-term memory and context](#memory) | What history is stored, and how is it retrieved, compressed, and used to guide actions? | 10 |
| [State verification and failure monitoring](#verification) | How can action completion, task success, and the need for recovery be distinguished? | 10 |
| [Reflection, attribution, and recovery](#reflection) | How are failure causes identified and subsequent attempts changed? | 10 |
| [Skill and harness evolution](#skills) | How can experience become transferable, verifiable skills without degrading existing capabilities? | 6 |
| [Fast and slow systems and real-time execution](#dual-system) | At what frequencies do reasoning, action generation, playback, and feedback operate? | 6 |
| [Policy learning and autonomous data loops](#policy-learning) | How does environment feedback enter training, reset, and redeployment? | 8 |
| [Digital twins and simulation validation](#simulation) | How can physical exploration costs be reduced and transfer be tested? | 2 |
| [Multi-robot collaboration and collective learning](#fleet) | What evidence supports shared state, shared skills, and shared weights, respectively? | 4 |
| [Runtime constraints and safety](#safety) | How are task constraints enforced during routing, contact, resource use, and fallback? | 4 |
| [Evaluation and reproducibility](#evaluation) | Are interfaces, perception access, budgets, perturbations, and data splits matched? | 7 |
| [Methods from general-purpose agents](#transfer) | Which software-agent mechanisms are worth transferring to physical execution? | 3 |

## Suggested reading

Execution interfaces: Show-Harness → Harness VLA → CaP-X; accumulating experience: ViReSkill → ASPIRE → Zetta; memory: RoboMME → PonderPounce → MaP-WAM; data and training: RoboClaw → HALTER → TwinRL → LWD.

## Paper index

Papers may appear in multiple categories. Dates indicate initial submission; new versions of the same arXiv ID are not counted again.

<a id="execution"></a>
### Closed-loop execution and tool interfaces

What does the reasoning model output, how do tools connect to controllers, and when should the system observe and replan?

| Submitted | Work | Core mechanism |
|---|---|---|
| 2026-09-17 | [SafeHarness](papers/2609.20822.md) · [Paper](https://arxiv.org/abs/2609.20822) | Turns obstacle-avoidance requirements into action choices during routing and contact, combining waypoint validation with replanning. |
| 2026-09-16 | [GPT-Policy](papers/2609.19138.md) · [Paper](https://arxiv.org/abs/2609.19138) | A context compiler retains task-relevant visual transitions; a VLM proposes robot tool actions that a constrained controller checks and executes. |
| 2026-09-10 | [Harness Robotic OS](papers/2609.11225.md) · [Paper](https://arxiv.org/abs/2609.11225) | Organizes quadruped inspection skills, shared context, hierarchical memory, and controlled candidate updates into a unified runtime. |
| 2026-09-09 | [Show-Harness](papers/2609.10522.md) · [Paper](https://arxiv.org/abs/2609.10522) | A VLM emits discrete semantic action units that an embodiment-specific interpreter deterministically converts into local actions, with GUI support for collecting demonstrations. |
| 2026-07-18 | [PhyAgentOS](papers/2607.16636.md) · [Paper](https://arxiv.org/abs/2607.16636) | Uses sessions to organize scheduling, evidence, acceptance checks, and memory, decoupling cognition from physical execution through inspectable state records. |
| 2026-07-09 | [Harness VLA](papers/2607.08448.md) · [Paper](https://arxiv.org/abs/2607.08448) | Uses a frozen VLA as a retryable contact primitive, combining analytical tools with task and global memory to extend manipulation capabilities. |
| 2026-06-30 | [ASPIRE](papers/2607.00272.md) · [Paper](https://arxiv.org/abs/2607.00272) | Diagnoses failures using fine-grained multimodal execution records, searches for repair programs, and accumulates validated experience as skills. |
| 2026-06-08 | [Harness Engineering for Physical AI](papers/2606.09416.md) · [Paper](https://arxiv.org/abs/2606.09416) | Proposes output constraints, resource isolation, and fallback mechanisms across control, computation, and communication paths. |
| 2026-03-23 | [CaP-X](papers/2603.22435.md) · [Paper](https://arxiv.org/abs/2603.22435) | Provides environments and evaluation for robot coding agents, studying tool abstractions, test-time compute, and RL with verifiable rewards. |
| 2026-03-12 | [RoboClaw](papers/2603.11558.md) · [Paper](https://arxiv.org/abs/2603.11558) | Combines forward manipulation and reverse recovery into a self-resetting loop, using a unified VLM controller to organize collection, learning, and deployment. |
| 2026-02-02 | [PLanAR](papers/2602.01662.md) · [Paper](https://arxiv.org/abs/2602.01662) | Constrains reasoning with object predicates, action preconditions and postconditions, and symbolic plans, checking execution effects step by step and replanning. |
| 2025-05-17 | [OneTwoVLA](papers/2505.11917.md) · [Paper](https://arxiv.org/abs/2505.11917) | A unified model switches between reasoning and action as needed, co-trained on robot data and synthetic reasoning data. |
| 2025-05-06 | [RoboOS](papers/2505.03673.md) · [Paper](https://arxiv.org/abs/2505.03673) | Organizes tasks and error correction across embodiments using an embodied brain, a modular skill library, and real-time shared memory. |
| 2024-11-26 | [MALMM](papers/2411.17636.md) · [Paper](https://arxiv.org/abs/2411.17636) | Assigns task planning, control-code generation, and process supervision to separate agents, using stepwise feedback to handle failures. |
| 2023-07-10 | [RoCo](papers/2307.04738.md) · [Paper](https://arxiv.org/abs/2307.04738) | Multiple robots use dialogue to produce task decompositions and waypoints, then check feasibility using environment feedback and motion planning. |

<a id="memory"></a>
### Long-term memory and context

What history is stored, and how is it retrieved, compressed, and used to guide actions?

| Submitted | Work | Core mechanism |
|---|---|---|
| 2026-09-16 | [GPT-Policy](papers/2609.19138.md) · [Paper](https://arxiv.org/abs/2609.19138) | A context compiler retains task-relevant visual transitions; a VLM proposes robot tool actions that a constrained controller checks and executes. |
| 2026-09-10 | [MaP-WAM](papers/2609.11561.md) · [Paper](https://arxiv.org/abs/2609.11561) | Uses long histories for planning, compresses them into segment-level language and visual guidance, and predicts action chunks and execution progress with an action model. |
| 2026-09-10 | [Harness Robotic OS](papers/2609.11225.md) · [Paper](https://arxiv.org/abs/2609.11225) | Organizes quadruped inspection skills, shared context, hierarchical memory, and controlled candidate updates into a unified runtime. |
| 2026-08-25 | [PonderPounce](papers/2608.24115.md) · [Paper](https://arxiv.org/abs/2608.24115) | Maintains an episode in the native MLLM context and asynchronously guides an action model through cognition tokens and token age. |
| 2026-07-18 | [PhyAgentOS](papers/2607.16636.md) · [Paper](https://arxiv.org/abs/2607.16636) | Uses sessions to organize scheduling, evidence, acceptance checks, and memory, decoupling cognition from physical execution through inspectable state records. |
| 2026-07-15 | [Zero2Skill](papers/2607.14047.md) · [Paper](https://arxiv.org/abs/2607.14047) | Collects data, verifies outcomes, and resets autonomously; requests human help only after exhausting a retry budget, then parses language corrections into Corrective Memory for reuse across rounds. |
| 2026-07-09 | [Harness VLA](papers/2607.08448.md) · [Paper](https://arxiv.org/abs/2607.08448) | Uses a frozen VLA as a retryable contact primitive, combining analytical tools with task and global memory to extend manipulation capabilities. |
| 2026-05-18 | [Robo-Cortex](papers/2605.18729.md) · [Paper](https://arxiv.org/abs/2605.18729) | Distills navigation trajectories into reusable heuristics, combining short-term reflection, long-term principle memory, and Imagine-then-Verify planning. |
| 2026-03-04 | [RoboMME](papers/2603.04639.md) · [Paper](https://arxiv.org/abs/2603.04639) | Evaluates temporal, spatial, object, and procedural memory in robotics, comparing 14 memory-augmented configurations. |
| 2025-05-06 | [RoboOS](papers/2505.03673.md) · [Paper](https://arxiv.org/abs/2505.03673) | Organizes tasks and error correction across embodiments using an embodied brain, a modular skill library, and real-time shared memory. |

<a id="verification"></a>
### State verification and failure monitoring

How can action completion, task success, and the need for recovery be distinguished?

| Submitted | Work | Core mechanism |
|---|---|---|
| 2026-09-17 | [SafeHarness](papers/2609.20822.md) · [Paper](https://arxiv.org/abs/2609.20822) | Turns obstacle-avoidance requirements into action choices during routing and contact, combining waypoint validation with replanning. |
| 2026-09-16 | [HALTER](papers/2609.19413.md) · [Paper](https://arxiv.org/abs/2609.19413) | Builds scene graphs and composes atomic reset skills for automatic scoring, reset planning, and reset verification in long-horizon evaluation. |
| 2026-09-10 | [MaP-WAM](papers/2609.11561.md) · [Paper](https://arxiv.org/abs/2609.11561) | Uses long histories for planning, compresses them into segment-level language and visual guidance, and predicts action chunks and execution progress with an action model. |
| 2026-09-10 | [FARM](papers/2609.11445.md) · [Paper](https://arxiv.org/abs/2609.11445) | Freezes the VLA-JEPA predictive backbone and trains only a lightweight readout, producing failure scores from internal states and aggregating risk over observed history. |
| 2026-08-17 | [Zetta](papers/2608.16590.md) · [Paper](https://arxiv.org/abs/2608.16590) | Evolves code critics and recovery skills around a frozen base policy, separating the timescales of actions, rollouts, and update validation. |
| 2026-07-18 | [PhyAgentOS](papers/2607.16636.md) · [Paper](https://arxiv.org/abs/2607.16636) | Uses sessions to organize scheduling, evidence, acceptance checks, and memory, decoupling cognition from physical execution through inspectable state records. |
| 2026-05-18 | [Robo-Cortex](papers/2605.18729.md) · [Paper](https://arxiv.org/abs/2605.18729) | Distills navigation trajectories into reusable heuristics, combining short-term reflection, long-term principle memory, and Imagine-then-Verify planning. |
| 2026-02-02 | [PLanAR](papers/2602.01662.md) · [Paper](https://arxiv.org/abs/2602.01662) | Constrains reasoning with object predicates, action preconditions and postconditions, and symbolic plans, checking execution effects step by step and replanning. |
| 2026-02-01 | [StreamVLA](papers/2602.01100.md) · [Paper](https://arxiv.org/abs/2602.01100) | Generates textual and visual completion states at subtask transitions, while locking intent and continuously producing actions during stable execution. |
| 2025-03-28 | [REMAC](papers/2503.22122.md) · [Paper](https://arxiv.org/abs/2503.22122) | Combines precondition and postcondition checks, self-reflection, and dynamic planning for long-horizon multi-robot tasks. |

<a id="reflection"></a>
### Reflection, attribution, and recovery

How are failure causes identified and subsequent attempts changed?

| Submitted | Work | Core mechanism |
|---|---|---|
| 2026-09-01 | [HarnessEvolve](papers/2609.00829.md) · [Paper](https://arxiv.org/abs/2609.00829) | Uses reference trajectories for failure attribution and screens harness updates through quality and performance gates to reduce regressions. |
| 2026-08-17 | [Zetta](papers/2608.16590.md) · [Paper](https://arxiv.org/abs/2608.16590) | Evolves code critics and recovery skills around a frozen base policy, separating the timescales of actions, rollouts, and update validation. |
| 2026-08-11 | [SHAPER](papers/2608.11350.md) · [Paper](https://arxiv.org/abs/2608.11350) | Keeps parameters frozen and uses environment rollouts to jointly optimize reusable skills and a context-code harness. |
| 2026-07-15 | [Zero2Skill](papers/2607.14047.md) · [Paper](https://arxiv.org/abs/2607.14047) | Collects data, verifies outcomes, and resets autonomously; requests human help only after exhausting a retry budget, then parses language corrections into Corrective Memory for reuse across rounds. |
| 2026-07-09 | [Harness VLA](papers/2607.08448.md) · [Paper](https://arxiv.org/abs/2607.08448) | Uses a frozen VLA as a retryable contact primitive, combining analytical tools with task and global memory to extend manipulation capabilities. |
| 2026-06-30 | [ASPIRE](papers/2607.00272.md) · [Paper](https://arxiv.org/abs/2607.00272) | Diagnoses failures using fine-grained multimodal execution records, searches for repair programs, and accumulates validated experience as skills. |
| 2026-05-18 | [Robo-Cortex](papers/2605.18729.md) · [Paper](https://arxiv.org/abs/2605.18729) | Distills navigation trajectories into reusable heuristics, combining short-term reflection, long-term principle memory, and Imagine-then-Verify planning. |
| 2025-09-29 | [ViReSkill](papers/2509.24219.md) · [Paper](https://arxiv.org/abs/2509.24219) | Replans from visual observations after failures and stores successful plans in skill memory for later reuse. |
| 2025-03-28 | [REMAC](papers/2503.22122.md) · [Paper](https://arxiv.org/abs/2503.22122) | Combines precondition and postcondition checks, self-reflection, and dynamic planning for long-horizon multi-robot tasks. |
| 2024-11-26 | [MALMM](papers/2411.17636.md) · [Paper](https://arxiv.org/abs/2411.17636) | Assigns task planning, control-code generation, and process supervision to separate agents, using stepwise feedback to handle failures. |

<a id="skills"></a>
### Skill and harness evolution

How can experience become transferable, verifiable skills without degrading existing capabilities?

| Submitted | Work | Core mechanism |
|---|---|---|
| 2026-09-01 | [HarnessEvolve](papers/2609.00829.md) · [Paper](https://arxiv.org/abs/2609.00829) | Uses reference trajectories for failure attribution and screens harness updates through quality and performance gates to reduce regressions. |
| 2026-08-17 | [Zetta](papers/2608.16590.md) · [Paper](https://arxiv.org/abs/2608.16590) | Evolves code critics and recovery skills around a frozen base policy, separating the timescales of actions, rollouts, and update validation. |
| 2026-08-11 | [SHAPER](papers/2608.11350.md) · [Paper](https://arxiv.org/abs/2608.11350) | Keeps parameters frozen and uses environment rollouts to jointly optimize reusable skills and a context-code harness. |
| 2026-06-30 | [ASPIRE](papers/2607.00272.md) · [Paper](https://arxiv.org/abs/2607.00272) | Diagnoses failures using fine-grained multimodal execution records, searches for repair programs, and accumulates validated experience as skills. |
| 2026-06-07 | [HARBOR](papers/2606.08610.md) · [Paper](https://arxiv.org/abs/2606.08610) | Breaks simulation RL engineering into executable stages and automates training pipelines through persistent artifacts, checkpoints, and experience reuse. |
| 2025-09-29 | [ViReSkill](papers/2509.24219.md) · [Paper](https://arxiv.org/abs/2509.24219) | Replans from visual observations after failures and stores successful plans in skill memory for later reuse. |

<a id="dual-system"></a>
### Fast and slow systems and real-time execution

At what frequencies do reasoning, action generation, playback, and feedback operate?

| Submitted | Work | Core mechanism |
|---|---|---|
| 2026-09-10 | [MaP-WAM](papers/2609.11561.md) · [Paper](https://arxiv.org/abs/2609.11561) | Uses long histories for planning, compresses them into segment-level language and visual guidance, and predicts action chunks and execution progress with an action model. |
| 2026-08-25 | [PonderPounce](papers/2608.24115.md) · [Paper](https://arxiv.org/abs/2608.24115) | Maintains an episode in the native MLLM context and asynchronously guides an action model through cognition tokens and token age. |
| 2026-02-01 | [StreamVLA](papers/2602.01100.md) · [Paper](https://arxiv.org/abs/2602.01100) | Generates textual and visual completion states at subtask transitions, while locking intent and continuously producing actions during stable execution. |
| 2026-01-08 | [LaST0](papers/2601.05248.md) · [Paper](https://arxiv.org/abs/2601.05248) | Connects a low-frequency reasoning expert to a high-frequency action expert through latent reasoning that incorporates visual dynamics, 3D structure, and proprioception. |
| 2025-06-02 | [Fast-in-Slow](papers/2506.01953.md) · [Paper](https://arxiv.org/abs/2506.01953) | Embeds a fast execution module within a slow reasoning system through partially shared parameters, asynchronous frequencies, and heterogeneous inputs. |
| 2025-05-17 | [OneTwoVLA](papers/2505.11917.md) · [Paper](https://arxiv.org/abs/2505.11917) | A unified model switches between reasoning and action as needed, co-trained on robot data and synthetic reasoning data. |

<a id="policy-learning"></a>
### Policy learning and autonomous data loops

How does environment feedback enter training, reset, and redeployment?

| Submitted | Work | Core mechanism |
|---|---|---|
| 2026-09-16 | [HALTER](papers/2609.19413.md) · [Paper](https://arxiv.org/abs/2609.19413) | Builds scene graphs and composes atomic reset skills for automatic scoring, reset planning, and reset verification in long-horizon evaluation. |
| 2026-07-15 | [Zero2Skill](papers/2607.14047.md) · [Paper](https://arxiv.org/abs/2607.14047) | Collects data, verifies outcomes, and resets autonomously; requests human help only after exhausting a retry budget, then parses language corrections into Corrective Memory for reuse across rounds. |
| 2026-06-07 | [HARBOR](papers/2606.08610.md) · [Paper](https://arxiv.org/abs/2606.08610) | Breaks simulation RL engineering into executable stages and automates training pipelines through persistent artifacts, checkpoints, and experience reuse. |
| 2026-05-01 | [Learning While Deploying](papers/2605.00416.md) · [Paper](https://arxiv.org/abs/2605.00416) | Pools deployment experience from multiple robots, continually updates a generalist VLA using DIVL and QAM, and redeploys it. |
| 2026-03-23 | [CaP-X](papers/2603.22435.md) · [Paper](https://arxiv.org/abs/2603.22435) | Provides environments and evaluation for robot coding agents, studying tool abstractions, test-time compute, and RL with verifiable rewards. |
| 2026-03-12 | [RoboClaw](papers/2603.11558.md) · [Paper](https://arxiv.org/abs/2603.11558) | Combines forward manipulation and reverse recovery into a self-resetting loop, using a unified VLM controller to organize collection, learning, and deployment. |
| 2026-02-09 | [TwinRL](papers/2602.09023.md) · [Paper](https://arxiv.org/abs/2602.09023) | Reduces online learning cost through SFT support-set expansion, digital-twin RL warm-up, and targeted real-world exploration. |
| 2025-11-25 | [Arcadia](papers/2512.00076.md) · [Paper](https://arxiv.org/abs/2512.00076) | Connects autonomous exploration, scene reconstruction, shared embodied representations, and simulation updates driven by real-world feedback. |

<a id="simulation"></a>
### Digital twins and simulation validation

How can physical exploration costs be reduced and transfer be tested?

| Submitted | Work | Core mechanism |
|---|---|---|
| 2026-02-09 | [TwinRL](papers/2602.09023.md) · [Paper](https://arxiv.org/abs/2602.09023) | Reduces online learning cost through SFT support-set expansion, digital-twin RL warm-up, and targeted real-world exploration. |
| 2025-11-25 | [Arcadia](papers/2512.00076.md) · [Paper](https://arxiv.org/abs/2512.00076) | Connects autonomous exploration, scene reconstruction, shared embodied representations, and simulation updates driven by real-world feedback. |

<a id="fleet"></a>
### Multi-robot collaboration and collective learning

What evidence supports shared state, shared skills, and shared weights, respectively?

| Submitted | Work | Core mechanism |
|---|---|---|
| 2026-05-01 | [Learning While Deploying](papers/2605.00416.md) · [Paper](https://arxiv.org/abs/2605.00416) | Pools deployment experience from multiple robots, continually updates a generalist VLA using DIVL and QAM, and redeploys it. |
| 2025-05-06 | [RoboOS](papers/2505.03673.md) · [Paper](https://arxiv.org/abs/2505.03673) | Organizes tasks and error correction across embodiments using an embodied brain, a modular skill library, and real-time shared memory. |
| 2025-03-28 | [REMAC](papers/2503.22122.md) · [Paper](https://arxiv.org/abs/2503.22122) | Combines precondition and postcondition checks, self-reflection, and dynamic planning for long-horizon multi-robot tasks. |
| 2023-07-10 | [RoCo](papers/2307.04738.md) · [Paper](https://arxiv.org/abs/2307.04738) | Multiple robots use dialogue to produce task decompositions and waypoints, then check feasibility using environment feedback and motion planning. |

<a id="safety"></a>
### Runtime constraints and safety

How are task constraints enforced during routing, contact, resource use, and fallback?

| Submitted | Work | Core mechanism |
|---|---|---|
| 2026-09-17 | [SafeHarness](papers/2609.20822.md) · [Paper](https://arxiv.org/abs/2609.20822) | Turns obstacle-avoidance requirements into action choices during routing and contact, combining waypoint validation with replanning. |
| 2026-09-10 | [FARM](papers/2609.11445.md) · [Paper](https://arxiv.org/abs/2609.11445) | Freezes the VLA-JEPA predictive backbone and trains only a lightweight readout, producing failure scores from internal states and aggregating risk over observed history. |
| 2026-09-10 | [Harness Robotic OS](papers/2609.11225.md) · [Paper](https://arxiv.org/abs/2609.11225) | Organizes quadruped inspection skills, shared context, hierarchical memory, and controlled candidate updates into a unified runtime. |
| 2026-06-08 | [Harness Engineering for Physical AI](papers/2606.09416.md) · [Paper](https://arxiv.org/abs/2606.09416) | Proposes output constraints, resource isolation, and fallback mechanisms across control, computation, and communication paths. |

<a id="evaluation"></a>
### Evaluation and reproducibility

Are interfaces, perception access, budgets, perturbations, and data splits matched?

| Submitted | Work | Core mechanism |
|---|---|---|
| 2026-09-16 | [HALTER](papers/2609.19413.md) · [Paper](https://arxiv.org/abs/2609.19413) | Builds scene graphs and composes atomic reset skills for automatic scoring, reset planning, and reset verification in long-horizon evaluation. |
| 2026-09-09 | [Show-Harness](papers/2609.10522.md) · [Paper](https://arxiv.org/abs/2609.10522) | A VLM emits discrete semantic action units that an embodiment-specific interpreter deterministically converts into local actions, with GUI support for collecting demonstrations. |
| 2026-09-03 | [EvoHarnessBench](papers/2609.04280.md) · [Paper](https://arxiv.org/abs/2609.04280) | Expands an external harness in stages and separately evaluates retention of existing capabilities and adaptation to new ones. |
| 2026-09-01 | [HarnessDev](papers/2609.01437.md) · [Paper](https://arxiv.org/abs/2609.01437) | Evaluates the capability and cost of building and improving executable harnesses, including held-out tasks and transfer across models. |
| 2026-03-23 | [CaP-X](papers/2603.22435.md) · [Paper](https://arxiv.org/abs/2603.22435) | Provides environments and evaluation for robot coding agents, studying tool abstractions, test-time compute, and RL with verifiable rewards. |
| 2026-03-04 | [RoboMME](papers/2603.04639.md) · [Paper](https://arxiv.org/abs/2603.04639) | Evaluates temporal, spatial, object, and procedural memory in robotics, comparing 14 memory-augmented configurations. |
| 2026-02-02 | [PLanAR](papers/2602.01662.md) · [Paper](https://arxiv.org/abs/2602.01662) | Constrains reasoning with object predicates, action preconditions and postconditions, and symbolic plans, checking execution effects step by step and replanning. |

<a id="transfer"></a>
### Methods from general-purpose agents

Which software-agent mechanisms are worth transferring to physical execution?

| Submitted | Work | Core mechanism |
|---|---|---|
| 2026-09-03 | [EvoHarnessBench](papers/2609.04280.md) · [Paper](https://arxiv.org/abs/2609.04280) | Expands an external harness in stages and separately evaluates retention of existing capabilities and adaptation to new ones. |
| 2026-09-01 | [HarnessDev](papers/2609.01437.md) · [Paper](https://arxiv.org/abs/2609.01437) | Evaluates the capability and cost of building and improving executable harnesses, including held-out tasks and transfer across models. |
| 2026-09-01 | [HarnessEvolve](papers/2609.00829.md) · [Paper](https://arxiv.org/abs/2609.00829) | Uses reference trajectories for failure attribution and screens harness updates through quality and performance gates to reduce regressions. |

## Update status

The repository includes daily arXiv candidate discovery and version checks, scheduled to run once the workflows are on the GitHub default branch and Actions is enabled. Discovery does not replace manual review; curated entries require verification before updates. Scheduled GitHub Actions runs may be delayed, and disabled workflows need attention.

## Sources and licensing

The initial topic came from research material dated 2026-09-08 supplied by the user. This repository reorganizes, verifies, and rewrites that material without including private Notion pages, original reports, or full papers. Code and original annotations use the MIT license; papers, abstracts, and third-party projects retain their respective licenses.
