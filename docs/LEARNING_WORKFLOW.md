# Learning Workflow

This repository is a hands-on learning project. The learner writes and runs the
code; the assistant explains, reviews, and helps debug it.

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
7. Let the learner type and run the change.
8. Inspect the real code or output before continuing.
9. Move forward when the learner asks for the next step.

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
