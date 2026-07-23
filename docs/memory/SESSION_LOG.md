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

## 2026-07-21 — Scope aligned with higher-level agent systems

- Decided to learn only the low-level LangGraph mechanisms needed to understand
  and debug higher-level systems rather than build a large framework from
  scratch.
- Set the remaining foundation boundary at messages/reducers, one model/tool
  loop, checkpoints/threads, and interrupt/resume.
- Chose Deep Agents as the main application layer, with OpenClaw explored as a
  separate always-on assistant runtime and NemoClaw/OpenShell as an operations
  and security layer for supported agent runtimes.
- Reframed the repository as a future public portfolio project: a safe,
  inspectable research agent with reproducible setup, architecture decisions,
  security boundaries, a useful demo, and lightweight evaluation.

## 2026-07-23 — NeMo Agent Toolkit added to the roadmap

- Positioned NeMo Agent Toolkit after the working Deep Agents application as
  the framework-agnostic profiling, observability, and evaluation layer.
- Kept NemoClaw/OpenShell as the separate runtime operations and security layer.
- Deferred toolkit integration until the project has real model and tool
  behavior worth profiling; the immediate LangGraph learning step is unchanged.

## 2026-07-23 — Full ecosystem roadmap and credential policy

- Decided to keep LangGraph, Deep Agents, NAT, AI-Q, OpenClaw, OpenShell, and
  NemoClaw in one portfolio repository while preserving separate dependency,
  process, sandbox, and mutable-state boundaries.
- Added a time-boxed nine-phase roadmap with deliverables and explicit exit
  criteria; the complete exploration is estimated at 86–134 focused hours.
- Positioned AI-Q as a pinned reference application to operate and extend, not
  a stack to copy into the root package.
- Added model-provider and secret practices covering OpenRouter, direct
  providers, exact model pinning for evaluations, key isolation, budgets,
  rotation, and OpenShell credential routing.
- Added `.env` exclusions before introducing any provider credentials. The next
  implementation step remains LangGraph message state and reducers.

## 2026-07-23 — Initial provider sequence aligned

- Made the available NVIDIA hosted development endpoint the first provider for
  the model-backed LangGraph exercise and kept OpenRouter as an optional later
  portability or fallback layer.
- Recorded the account's displayed limit of up to 40 requests per minute and
  added explicit concurrency, rate-limit, and provider-integration checks.
- Confirmed that no provider package, API key, or credential has been added to
  the repository; the next implementation step remains message state and
  reducer semantics.
