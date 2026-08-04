# Learning Workflow

This repository is an interactive learning project. The assistant explains and
implements one small step at a time; the learner reviews the concrete change and
observed result, asks questions, and acknowledges before the assistant proceeds.

## Working cycle

1. Inspect the current repository state before suggesting the next action.
2. Introduce one small concept or code change at a time.
3. Prefer a vertical slice: attach the change to the smallest safe runnable
   path rather than building disconnected components for later assembly.
4. State the output, state transition, or test result the learner should
   observe immediately after the change.
5. Show every required import, dependency, file, and command explicitly.
6. Explain what the new construct does, why it is needed, and what is merely a
   project preference rather than a requirement.
7. Have the assistant implement and run the change.
8. Inspect the real code or output together.
9. Pause for learner review, questions, and acknowledgment before continuing.
10. When surveying a low-level mechanism for intuition, stop after one thin
    runnable probe and observable result unless a concrete failure justifies
    deeper engineering or tests.

When an interactive graph or protocol reaches a working checkpoint, completing
that slice includes a dedicated module under `src/langgraph_learning/runners/`
so the learner can run and inspect it again. `runners/playground.py` is only a
temporary workbench for ad hoc probes; it does not replace the stable runner.

The assistant should not silently build ahead unless the learner explicitly
asks for implementation. Commands that create or modify files, environments, or
dependencies should be identified as such before they run.

## Technical progression

Establish the smallest safe end-to-end graph as early as possible, then replace
or extend one part at a time:

1. Define only enough state and deterministic behavior to compile and run one
   complete path.
2. Stream or test that path immediately.
3. Add one model, tool, router, persistence feature, or approval boundary
   directly to the executable path.
4. Re-run and inspect the resulting state transition before adding the next
   mechanism.

Never make a real model/tool graph temporarily unbounded merely to obtain an
early runnable slice. Use a one-round topology, hard stop, fake model, or other
safe temporary boundary and make that limitation explicit.
