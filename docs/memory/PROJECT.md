# Project Memory

Last updated: 2026-07-21

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
- `src/langgraph_learning/graph.py` defines and compiles the first deterministic
  graph: a typed `question`/`route`/`answer` state, a word-count router, direct
  and research placeholder nodes, conditional routing, and terminal edges.
- `src/langgraph_learning/demo.py` provides an interactive module runner that
  prints the compiled graph as Mermaid syntax before prompting, then streams
  each node's partial state update. Both the direct and research branches were
  invoked successfully with
  `uv run python -m langgraph_learning.demo` from the repository root.
- The generated `langgraph-learning` command still runs its placeholder entry
  point, and automated graph tests have not been added yet.
- No model provider or credentials are configured, which is intentional for the
  first deterministic graph.

## Next action

Begin phase 2 by choosing a model provider, adding its integration dependency,
and replacing one placeholder answer node with a single model call while
keeping the deterministic router observable. Automated tests are intentionally
deferred while the graph remains small and both branches are manually verified.
