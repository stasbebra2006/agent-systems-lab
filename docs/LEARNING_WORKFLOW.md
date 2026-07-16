# Learning Workflow

This repository is a hands-on learning project. The learner writes and runs the
code; the assistant explains, reviews, and helps debug it.

## Working cycle

1. Inspect the current repository state before suggesting the next action.
2. Introduce one small concept or code change at a time.
3. Show every required import, dependency, file, and command explicitly.
4. Explain what the new construct does, why it is needed, and what is merely a
   project preference rather than a requirement.
5. Let the learner type and run the change.
6. Inspect the real code or output before continuing.
7. Move forward when the learner asks for the next step.

The assistant should not silently build ahead unless the learner explicitly
asks for implementation. Commands that create or modify files, environments, or
dependencies should be identified as such before they run.

## Technical progression

Build the research assistant from visible, deterministic pieces before adding
model behavior:

1. Define graph state.
2. Implement ordinary Python nodes.
3. Connect nodes with edges and conditional routing.
4. Compile, invoke, inspect, and test the graph.
5. Replace selected deterministic behavior with an LLM and tools.

This sequence keeps LangGraph mechanics observable and makes failures easier to
attribute to graph orchestration, application code, or model behavior.
