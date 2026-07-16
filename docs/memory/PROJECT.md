# Project Memory

Last updated: 2026-07-16

## Goal

Learn LangGraph deeply enough to design, implement, debug, and eventually deploy
reliable stateful agents—not merely reproduce tutorial code.

## Approach

- Use the LangChain Academy Python course as a coverage map, not a requirement
  to watch every video.
- Learn interactively by extending one coherent project.
- Follow the learner-driven, one-change-at-a-time process documented in
  `docs/LEARNING_WORKFLOW.md`.
- Prefer current official documentation and installed-package behavior when
  older course examples differ.
- Build low-level concepts explicitly before adopting higher-level shortcuts.
- Defer long-term memory and deployment until the project needs them.

## Project direction

The provisional project is a research assistant that can route work, call
tools, research in parallel, persist conversation state, request human approval,
and later retain long-term preferences.

## Roadmap

1. Build a deterministic graph: state, nodes, edges, and conditional routing.
2. Add an LLM and tools: agent loops, tool calls, and termination.
3. Add state management: reducers, messages, checkpoints, and threads.
4. Add user control: streaming, interrupts, state edits, and replay.
5. Add composition: parallel work, subgraphs, and map-reduce.
6. Add long-term memory and production infrastructure only when useful.

For each phase, the completion standard is to explain the mechanism, implement
it without blindly copying, inspect its runtime state, and identify common
failure modes.

## Current status

- The working directory and persistent memory are initialized.
- The project is a Git repository on the `main` branch, with private GitHub
  remote `stasbebra2006/langgraph-learning` configured as `origin`.
- The repository is a uv-managed Python package targeting Python 3.12, with a
  local virtual environment and committed lockfile.
- LangGraph 1.2.9 is installed as the first application dependency.
- The generated `langgraph-learning` command runs a placeholder entry point;
  graph state, nodes, edges, and tests have not been implemented yet.
- No model provider or credentials are configured, which is intentional for the
  first deterministic graph.

## Next action

Create `src/langgraph_learning/graph.py`, beginning with the `TypedDict` import
and then adding the first `ResearchState` field (`question: str`). Continue one
small addition at a time before implementing the deterministic router.
