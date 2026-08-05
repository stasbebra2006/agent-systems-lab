# Learning Workflow

This repository is an interactive learning project. The learner is the active
architect and problem-solving partner: they help frame problems, develop
hypotheses, choose experiments and trade-offs, and interpret evidence. The
assistant handles repetitive inspection, translates decisions into code, runs
verification, and explains implementation details as needed.

## Working cycle

1. Inspect the current repository state before suggesting the next action.
2. Frame the current problem: why it matters, concrete objects, ownership,
   constraints, known facts, and the unresolved question.
3. Reconstruct rather than merely state the design: traverse from the problem and
   constraints through plausible mechanisms and trade-offs to the selected
   behavior and its consequences. Separate what is logically necessary from what
   is a framework-specific choice so the learner can derive and predict behavior
   instead of memorizing conventions.
4. At genuine design boundaries, ask the learner to propose a hypothesis,
   choose an experiment or trade-off, or predict the outcome. Offer compact
   options only when they clarify a real choice; do not turn mechanics into a
   quiz.
5. Introduce one small concept or code change at a time.
6. Prefer a vertical slice: attach the change to the smallest safe runnable
   path rather than building disconnected components for later assembly.
7. Agree on the output, state transition, or test result that would distinguish
   the competing hypotheses or demonstrate success.
8. Have the assistant handle repetitive inspection, implement the chosen change,
   and run it while making required imports, dependencies, files, and commands
   visible.
9. Inspect the real code or output together; ask the learner to interpret what
   it establishes before supplying the missing explanation.
10. Pause at the next meaningful decision or evidence boundary, not merely for a
   ceremonial acknowledgment.
11. When surveying a low-level mechanism for intuition, stop after one thin
    runnable probe and observable result unless a concrete failure justifies
    deeper engineering or tests.

When an interactive graph or protocol reaches a working checkpoint, completing
that slice includes a descriptively named module under
`src/langgraph_learning/runners/` so the learner can run and inspect it again.
Temporary probes are still learner-facing code: explain and introduce them
incrementally rather than silently treating them as disposable internal
diagnostics, and preserve useful probes under descriptive names.

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
