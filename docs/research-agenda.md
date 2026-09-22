# Research agenda: from closed-loop execution to verifiable continual improvement

Updated: 2026-09-22. The directions below are **research hypotheses** proposed by the maintainers. They are not claims validated by existing papers, nor claims of exhaustive coverage or novelty. Check related work and read the full papers before starting a project.

## Three kinds of feedback loop

| Loop | Updated components | Persistence across episodes | What should be demonstrated |
|---|---|---|---|
| Execution | State estimates, current plan, current action | May not persist | Recovery and completion within the same task under perturbations |
| Learning | Memory, skills, harness, parameters | Requires an explicit persistence mechanism | Benefits on subsequent unseen instances without degrading existing capabilities |
| Fleet | Experience and deployable artifacts shared across robots | Across robots/deployment rounds | Lower learning costs for new robots, beyond simply increasing data volume |

Retry, Replan, Reflection, Memory Update, Skill Update, Policy Update, and Fleet Update can serve as seven capability labels. They are not established levels, and should not be forced into a ladder every system must climb in sequence.

## P0: State-verification-driven memory and recovery

**Question:** When an executable action finishes but the semantic goal remains unmet, what evidence should the reasoning model retain, which step should it blame, and how should it change the next action?

**Hypothesis:** Structured memory containing goal conditions, failure evidence, and attempt history avoids repeated failures more effectively than free-text summaries. The benefit may come from selecting the right information rather than increasing context length.

**Design:** For each subtask, store the goal, preconditions, expected outcome, timestamped observation evidence, judgment confidence, and failure cause. Retrieve records related to currently unmet conditions. The verifier outputs success / failure / uncertain, with uncertain triggering additional observation.

**Experiment:** Fix the backbone, executor, and observation budget. Compare no memory, full history, text summaries, fixed-field memory, and oracle memory under occlusion, failed contact, object movement, and sensor noise. Measure task success, false-success rate, repeated-failure rate, recovery cost, and accuracy of locating supporting memory evidence.

**Related:** [RoboMME](../papers/2603.04639.md), [PLanAR](../papers/2602.01662.md), [MaP-WAM](../papers/2609.11561.md), [PhyAgentOS](../papers/2607.16636.md).

## P0: Fair interface comparisons with the same reasoning model

**Question:** Do gains come from the model, the action representation, or human-provided perception, motion planning, and skill scaffolding?

**Hypothesis:** Discrete semantic actions, continuous EEF targets, analytical tools, and frozen VLAs each have advantages in different task regimes. A single aggregate score hides these dependencies.

**Design:** Fix the VLM, images, history, token budget, and interaction budget while comparing four interfaces. Also record access to depth, target poses, and oracle scene graphs, together with coordinate frames, units, action duration, IK, and obstacle-avoidance implementations.

**Experiment:** Group tasks into free-space transport, constrained placement, articulated objects, and contact-rich manipulation. Introduce calibration errors and layout drift. Report success rates, call counts, failure attribution, end-to-end duration, and time spent in each tool. Ablate additional priors supplied by analytical tools separately.

**Related:** [Show-Harness](../papers/2609.10522.md), [Harness VLA](../papers/2607.08448.md), [CaP-X](../papers/2603.22435.md), [GPT-Policy](../papers/2609.19138.md).

## P1: Boundaries between code critics and learned critics

**Hypothesis:** Code constraints are reliable for explicitly describable geometric conditions; learned state classifiers are better suited to visual ambiguity and contact states. Hybrid verification may improve coverage and real-time performance.

Fix the base policy and compare rules, VLMs, lightweight neural critics, and hybrids. Annotate the first observable failure time to evaluate detection latency, false negatives/positives, and the cost of unnecessary recovery. Stress-test inference and communication delays, reporting p50/p95/p99 rather than averages alone.

**Related:** [Zetta](../papers/2608.16590.md), [SafeHarness](../papers/2609.20822.md), [Physical AI harness proposal](../papers/2606.09416.md). [FARM](../papers/2609.11445.md) adds a reference for learned failure detection using frozen world-model features; separate detection gains from recovery gains.

## P1: Behavioral regressions as skill libraries grow

**Hypothesis:** Even locally useful new skills can interfere with retrieval, selection, and existing behavior. Update gates with applicability conditions, counterexamples, and regression sets may reduce this degradation.

Expand the skill library by task family in stages while keeping the model and evaluation set fixed. Compare full injection, retrieval-based injection, guarded retrieval, and dual validation gates. Measure forward transfer, backward transfer, retention on existing tasks, context cost, and the fraction of rejected updates.

**Related:** [ASPIRE](../papers/2607.00272.md), [SHAPER](../papers/2608.11350.md), [EvoHarnessBench](../papers/2609.04280.md), [HarnessEvolve](../papers/2609.00829.md). The last two provide methods from general-purpose agents.

## P1: Reset costs and data value in learning budgets

**Hypothesis:** Scheduling exploration using expected learning gains, reset costs, and human takeover costs saves more real time than sampling solely by policy uncertainty.

Define experiment cost as the total cost of rollouts, resets, verification, human intervention, twin reconstruction, and training. Compare random, uncertainty-based, and cost-aware sampling using paired tasks and matched human budgets. Measure wall-clock time and person-hours needed to reach a target success rate.

**Related:** [RoboClaw](../papers/2603.11558.md), [HALTER](../papers/2609.19413.md), [TwinRL](../papers/2602.09023.md).

## P2: When should memory be distilled into a policy?

**Hypothesis:** Frequent, unambiguous experiences with reliable verification labels are suitable for parameter updates; rare or changeable knowledge is better kept in external memory. The best boundary depends on latency, forgetting, and scene drift.

Compare memory alone, post-training alone, periodic distillation, and confidence-based selective distillation. Evaluate learning speed, retention on existing tasks, online overhead, and robustness to distribution shifts. Do not feed successful test trajectories back into training and then claim zero-shot testing.

**Related:** [ViReSkill](../papers/2509.24219.md), [HARBOR](../papers/2606.08610.md), [LWD](../papers/2605.00416.md).

## P2: Verifiable transfer of experience across embodiments

**Hypothesis:** Sharing failure conditions and skill applicability may reduce adaptation costs across embodiments, while sharing raw trajectories or coordinates is more constrained by embodiment differences.

Use leave-one-embodiment-out evaluation to compare independent learning, shared raw trajectories, shared abstract experience, and shared weights. Control total data volume and robot count separately. Measure time to first success on a new embodiment, calibration costs, negative transfer, and fleet benefit curves.

**Related:** [RoboOS](../papers/2505.03673.md), [RoCo](../papers/2307.04738.md), [LWD](../papers/2605.00416.md). These examples do not establish any one work as the field's only evidence.

## Suggested sequence

1. Establish consistent interface logs and verification labels, and reproduce a minimal execution loop.
2. Run the P0 comparisons with matched protocols to identify the main bottleneck.
3. Pursue one P1 direction around the measured bottleneck, adding a retention set across tasks.
4. Test parameter updates or collective learning after autonomous collection and resources are reliable.
