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

## 2026-07-24 — Message reducer checkpoint

- Added a typed `messages` state channel backed by LangGraph's `add_messages`
  reducer and declared LangChain Core as a direct dependency.
- Updated the demo to initialize a `HumanMessage` and stream complete state
  values, making state accumulation visible after each graph step.
- Updated both deterministic answer branches to append an `AIMessage`; runtime
  assertions verified both routes finish with the expected two-message history.
- Verified source compilation, Pyright checks, lock consistency, and whitespace.
  No model provider, credential, or real model call has been introduced yet.

## 2026-07-25 — NVIDIA model integration checkpoint

- Added and locked `langchain-nvidia-ai-endpoints` 1.4.3, selected the exact
  tool-capable `nvidia/nemotron-3-nano-30b-a3b` model, and added a lazy
  `ChatNVIDIA` factory without changing either graph answer node.
- Stored the development credential only in an ignored permission-`600`
  `.env`, loaded it explicitly through uv, and completed a successful isolated
  model smoke call with thinking disabled and response metadata visible.
- Simplified the deterministic graph demo output and added `model_demo.py` for
  provider-only inspection.
- Stopped before replacing `answer_directly()` with the model-backed update so
  the learner can implement that exact change at the start of the next session.
- Verified lock consistency, source compilation, whitespace, and the existing
  deterministic direct route without making another billed model request;
  Pyright was unavailable in the current shell.

## 2026-07-26 — Direct graph route backed by NVIDIA

- Replaced only `answer_directly()` with the pending model call: it invokes the
  primary model with accumulated messages and thinking disabled, exposes
  `response.text` as the answer, and returns the complete `AIMessage`.
- Ran the direct route end to end with a concise prompt and confirmed that
  `add_messages` retained the human and AI messages plus response and usage
  metadata.
- Observed 23 input tokens, 42 output tokens, and a normal `stop` finish from
  the pinned model.
- Located the existing Mason-managed Pyright 1.1.409 installation outside the
  normal shell `PATH`; a check explicitly targeting `.venv/bin/python` passed
  with zero errors or warnings.
- Added `count_words` as the first deterministic local `@tool`; inspection
  showed its `StructuredTool` type, inferred JSON input schema, docstring-based
  description, and the expected direct result. Pyright remained clean.
- Added an isolated tool-call demo and confirmed that the bound model emits a
  structured `count_words` request with the expected argument and a unique call
  ID. Extended it only through local execution, which returned `5`, and stopped
  before constructing a `ToolMessage` or making a second model call. Pyright
  remained clean.
- Left the research route deterministic. The next learning step is to construct
  a `ToolMessage` matching the completed request before building a bounded,
  observable model/tool loop.

## 2026-07-27 — Tool result message checkpoint

- Extended the isolated tool-call demo through construction of a `ToolMessage`
  whose `tool_call_id` matches the model's structured request.
- Inspected the difference between the provider's raw tool-call representation,
  LangChain's normalized `tool_calls`, the AI message ID, and the individual
  tool-call ID.
- Stopped before the second model invocation. The next step is to pass the
  ordered human, assistant-tool-call, and tool-result messages back to the
  tool-bound model and inspect its final response.
- Completed the second invocation with the ordered human, assistant tool-call,
  and matching tool-result messages. The model correctly reported five words
  and returned no further tool calls, verifying successful manual-loop
  termination.
- Local compilation, Pyright, and whitespace checks passed. The next step is to
  express this protocol as a visible bounded LangGraph loop with controlled
  tool-failure behavior.

## 2026-07-27 — Systems-thinking collaboration model persisted

- Added `docs/memory/COLLABORATION.md` as the canonical collaboration contract:
  begin complex work with a compact system map, reason through dependencies and
  second-order effects, distinguish facts from hypotheses, challenge weak
  models, and return analysis to implementation and measurement.
- Updated `AGENTS.md` to require loading the collaboration contract alongside
  project memory at the start of every session without duplicating the full
  instructions in the entry point.
- Added targeted refresh triggers for substantial tasks, system-level
  decisions, post-compaction continuation, and user-identified reasoning drift;
  simple factual questions and mechanical edits do not trigger redundant
  rereads.
- Refined the learning workflow from horizontal component buildup to vertical
  slices: each new construct should enter the smallest safe runnable path and
  produce immediate observable evidence before another mechanism is added.

## 2026-07-27 — Tool-loop foundation checkpoint

- Added an uncompiled `tool_graph.py` foundation with typed reducer-backed
  messages, explicit tool-round state, a tool-bound model node, model-output
  routing, a standard `ToolNode`, and deterministic round accounting.
- Verified the router locally with synthetic `AIMessage` values: a structured
  tool call routes to tools, while ordinary assistant content routes to
  termination. Compilation and Pyright remained clean.
- Identified delayed integration as a learning-process problem and changed the
  next step to a safe one-round vertical slice with streamed node updates,
  followed by finalization and then the bounded multi-round path.
