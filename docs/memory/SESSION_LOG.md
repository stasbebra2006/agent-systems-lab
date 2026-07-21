# Session Log

## 2026-07-13 — Project initialization

- Chose a hybrid learning approach: Academy structure plus interactive project
  implementation.
- Proposed a research assistant as the project spanning the curriculum.
- Created the working directory and canonical persistent-memory documents.
- Left language environment, dependencies, model provider, and credentials
  unconfigured pending the first implementation session.

## 2026-07-13 — Memory simplified

- Consolidated current state, roadmap, and decisions into `PROJECT.md`; retained
  this file only for chronological history.

## 2026-07-14 — Repository initialized

- Initialized the project as a Git repository on `main`.
- Created private GitHub repository `stasbebra2006/langgraph-learning` and
  configured it as `origin`.

## 2026-07-16 — Python environment and learning workflow

- Selected the deterministic research-query router as the first LangGraph
  exercise, with LLM and tool behavior deferred until graph mechanics are
  understood.
- Initialized a uv-managed package on Python 3.12 and added LangGraph 1.2.9 with
  a reproducible lockfile.
- Reviewed package structure, `pyproject.toml`, `uv.lock`, and the role of
  `TypedDict` as a LangGraph state schema.
- Established a learner-driven workflow: introduce one small change at a time,
  present all imports explicitly, explain requirements versus preferences, and
  inspect actual code or output before continuing.
- Left graph implementation for the next session; the next step is to define
  the first field of `ResearchState` in `graph.py`.

## 2026-07-21 — First deterministic graph compiled

- Defined typed graph state with required `question` and later-produced
  `route` and `answer` fields.
- Implemented deterministic routing plus direct and research placeholder nodes.
- Connected `START`, conditional branches, and `END`, then compiled the graph.
- Added an interactive `demo.py` runner, printed the compiled structure as
  Mermaid syntax, streamed per-node updates, and verified both branches through
  the package-module command.
- Confirmed experimentally that this LangGraph version filters unknown state
  keys but does not enforce `TypedDict` value types at runtime.
- Deferred automated tests for now; the next milestone is selecting a model
  provider and introducing one observable LLM-backed node.
