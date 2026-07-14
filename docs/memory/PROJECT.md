# Project Memory

Last updated: 2026-07-14

## Goal

Learn LangGraph deeply enough to design, implement, debug, and eventually deploy
reliable stateful agents—not merely reproduce tutorial code.

## Approach

- Use the LangChain Academy Python course as a coverage map, not a requirement
  to watch every video.
- Learn interactively by extending one coherent project.
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
- No language environment, dependencies, application code, or credentials are
  configured.
- Python is expected because the chosen Academy course is the Python edition,
  but this remains to be confirmed before setup.

## Next action

Confirm the project idea and Python choice, then create the development
environment and build the first deterministic graph without an LLM.
