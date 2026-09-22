# Evaluation reporting protocol

Before making a cross-paper comparison, check the conditions below. Present mismatched conditions side by side without directly ranking results.

| Field | Required information |
|---|---|
| Version | arXiv version, code commit, and exact model version |
| Execution interface | Textual skills, semantic actions, EEF pose/delta, joint actions, code, or VLA primitives |
| Observations | RGB/RGB-D, multiple views, proprioception, force sensing, oracle/estimated scene graphs |
| Geometry conventions | Coordinate frames, units, absolute/relative values, rotation representation, calibration, and normalization |
| Execution stack | IK, planners, collision checks, gripper control, and their human-designed priors |
| Data access | Demonstration count, video/action labels, target-environment interaction, and privileged state |
| Updated components | Context, memory, code, harness, or model weights |
| Data splits | Separation of training, adaptation, validation, and testing by scene, task, or embodiment |
| Budget | Tokens, tool calls, rollouts, retries, candidate programs, and training compute |
| Frequency | VLM inference, action generation, chunk length, action playback, and closed-loop feedback |
| Cost | End-to-end elapsed time, human interventions/resets, person-hours, and twin construction time |
| Statistics | Sample counts, seeds, success criteria, confidence intervals, and failure categories |
| Continual learning | Initial adaptation, retained tasks, cross-task/embodiment generalization, and negative transfer |
| Safety | Collisions, constraint violations, emergency stops, detection latency, false positives, and false negatives |

## Minimum ablations

Fix the model and executor, then separately remove history, verification, recovery, persistent skills, and parameter updates. Match additional observation and compute budgets. A verifier must not silently benefit from oracle states unavailable at deployment during final testing.

## Recording numbers

Structured `metrics` records must include at least `value`, `unit`, `benchmark`, `split`, `backbone`, `budget`, `source_url`, `paper_version`, `table_or_section`, and `verification_scope`. Use `null` for missing fields and explain why the result cannot support cross-paper rankings. The initial release is a mechanism index; entries without sufficient numerical verification leave `metrics` empty.
