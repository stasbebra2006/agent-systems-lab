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

## 2026-07-28 — Repository renamed Agent Systems Lab

- Renamed the public GitHub repository from `langgraph-learning` to
  `agent-systems-lab` and verified that the local `origin` uses the new SSH URL.
- Renamed the local checkout directory to `agent-systems-lab` as well.
- Updated the public README identity to `Agent Systems Lab`.
- Kept the `langgraph_learning` Python package and `langgraph-learning`
  distribution/CLI names because they remain the bounded low-level foundation,
  not the identity of the wider multi-framework repository.

## 2026-07-28 — Public README established

- Reworked the README into the public project entry point with an honest
  implemented-versus-planned boundary, current capabilities, target
  architecture, phase status, quick starts, repository structure, engineering
  principles, documentation map, and maturity warning.
- Added a credential-free command that exercises the deterministic research
  branch and separate commands for the credentialed model and tool-call demos.
- Persisted a repository instruction to update the README whenever meaningful
  work changes public behavior, setup, architecture, structure, roadmap status,
  or the next implementation step; discussion-only turns do not create README
  churn.

## 2026-07-28 — Shared model construction extracted

- Added `models.py` as the explicit owner of the pinned model ID and primary
  model factory.
- Updated both graph modules and both credentialed demos to depend on the model
  module instead of importing shared infrastructure from `graph.py`.
- Verified all affected imports, source compilation, Pyright, and whitespace
  without making a provider request.
- Inspection also found that the learner-added provisional builder registers
  both the tool and counter node names with `call_model`. Static checks pass
  despite that semantic wiring error, so the graph code was left untouched for
  the next learner correction.
- Set the next step to correct those registrations, inspect the topology, and
  then finish the narrow graph/demo layout separation before adding the
  executable one-round tool-loop runner.

## 2026-07-28 — Source package grouped by responsibility

- Added `graphs/` for reusable graph definitions and `demos/` for executable
  learning entry points, each with an explicit package initializer.
- Moved and descriptively renamed the routing graph, tool-loop graph, routing
  runner, model-call demo, and manual tool-call demo.
- Kept `models.py` and `tools.py` at the package root as narrow shared
  infrastructure rather than introducing a generic global utility module.
- Updated internal imports, public quick-start commands, the repository tree,
  and canonical memory. The pending tool-node registration correction remains
  intentionally separate from this behavior-preserving layout change.
- Verified the new module paths through compilation, import checks, the
  credential-free streamed routing demo, Pyright, and whitespace checks.

## 2026-07-28 — One-round tool topology corrected

- Corrected the provisional graph registrations so the `tools` node executes
  the `ToolNode` and `increment_tool_round` executes the counter update.
- Rendered the compiled graph without a provider request and verified the safe
  topology: model output either terminates or takes one
  `tools -> increment_tool_round -> END` path.
- Pyright and whitespace checks passed. The next step is to add the executable
  demo runner and stream real node updates through this temporary hard stop.

## 2026-07-28 — Directory restructuring plan created

- Analyzed existing codebase layout and proposed a clean, layered architectural structure.
- Created `RESTRUCTURING_PLAN.md` in the project root to document target directory paths (`core/`, `tools/`, `graphs/`, `runners/`, `tests/`), file mappings, and step-by-step migration tasks.
- Updated project memory to reflect the new plan.

## 2026-07-28 — Accepted source restructuring implemented

- Replaced `demos/` with `runners/`, moved `count_words` into the focused
  `tools/word_counter.py` module, and retained the single shared `models.py` at
  the package root instead of adding a generic `core/` package.
- Added a stable interactive tool-loop runner plus an editable playground that
  currently renders the graph topology without a provider request.
- Removed the unused placeholder console script and standardized execution on
  explicit `python -m langgraph_learning.runners.<name>` module paths.
- Updated imports, public commands, repository structure documentation,
  restructuring status, and canonical project memory.
- Verified lock consistency, package imports, direct tool behavior, the
  credential-free playground and routing stream, source compilation, Pyright,
  and whitespace.

## 2026-07-28 — Runner completion rule clarified

- Clarified that a working interactive graph or protocol is not a completed
  learning slice until it has a dedicated runner the learner can execute and
  inspect repeatedly.
- Recorded `runners/playground.py` as a temporary ad hoc workbench rather than
  a substitute for a stable runner.

## 2026-07-28 — Credentialed one-round tool graph observed

- Ran the dedicated tool-loop runner with `Hello world` and streamed the
  `model`, `tools`, and `increment_tool_round` node updates.
- The model requested `count_words` with the original text, the local tool
  returned `2`, the matching `ToolMessage` preserved the tool-call ID, and
  round accounting advanced from zero to one.
- The request used 271 input and 26 output tokens and ended at the intentional
  hard stop, confirming that final natural-language synthesis is the next
  missing transition rather than a tool-execution failure.

## 2026-07-28 — Session handoff at observed tool-loop state

- Stopped immediately after explaining the credentialed
  `model -> tools -> increment_tool_round -> END` output.
- The learner has an unresolved question about this exact execution and wants
  the next session to reopen `graphs/tool_loop.py` and its dedicated
  `runners/tool_loop.py` without making another code change first.
- Preserve `runners/playground.py` as the editable ad hoc inspection file; it
  complements but never replaces dedicated runners for completed slices.
- Only after resolving the question should work proceed to the separate,
  bounded finalization node.

## 2026-07-29 — Stream-update mechanics and response-view checkpoint

- Revisited the one-round runner after the learner confirmed that a general
  greeting produced a direct model answer rather than another tool request.
- Traced the installed `ToolNode` inside graph-supplied runtime: it reads the
  latest `AIMessage.tool_calls`, executes the registered local tool, returns a
  matching `ToolMessage` in a partial `messages` update, and relies on
  `add_messages` to merge that result into accumulated graph history.
- Verified with a temporary parallel graph that
  `stream_mode="updates"` returns a generator and emits separate node-name
  wrappers around partial state dictionaries, including for nodes in the same
  parallel step.
- Preserved the learner's work-in-progress `print_response()` formatter and
  commented final-response scaffold. Lock consistency, source compilation,
  Pyright, and whitespace checks passed. A credential-free synthetic probe
  showed that the formatter correctly prints a direct answer but also emits an
  empty answer block for a tool request and labels a `ToolMessage("2")` as an
  AI response.
- Next session should first add the `AIMessage`/no-tool-call/content filter and
  repeat the four-case synthetic probe. Only then should the graph gain a
  bounded final-response node and credentialed provider-compatibility test.

## 2026-07-29 — Interactive learning roles changed

- Changed the working mode from learner-typed implementation to assistant-led
  implementation in small, visible checkpoints.
- The assistant now explains each step and its expected evidence, edits and
  verifies it, then pauses for learner review, questions, and acknowledgment.
- The learner remains the reviewer and decision-maker; advancing without an
  acknowledgment is outside the agreed cadence.

## 2026-07-29 — One-round tool path finalized

- Completed the runner's response filter: only nonempty `AIMessage` answers
  without tool calls render; deterministic probes confirmed tool requests,
  tool results, and counter-only updates remain silent.
- Added and wired an unbound `final_response` model node after round accounting,
  yielding `model -> tools -> increment_tool_round -> final_response -> END`.
- Verified the complete credentialed path with `count_words("Hello my friend.")`:
  the tool returned `3`, and NVIDIA accepted the historical assistant tool call
  plus matching `ToolMessage` without tools rebound on the final request.
- Lock consistency, source compilation, whitespace, and the focused diff passed.
  The next checkpoint is deterministic automated coverage before implementing
  the bounded multi-round path.

## 2026-07-29 — First deterministic pytest baseline

- Added pytest 9.1.1 to uv's development dependency group without changing
  application runtime dependencies.
- Added eight credential-free cases covering both model-routing outcomes,
  immutable partial round accounting, completed-answer rendering, silent tool
  request/result/counter updates, and required compiled topology edges.
- Explicitly annotated synthetic states as `ToolLoopState`; Mason Pyright then
  reported zero errors. Confirmed that a stale running Pyright client can retain
  a pre-install package index and should be restarted after dependency changes.
- Final verification passed: lock consistency, source/test compilation, eight
  tests, zero Pyright errors, and whitespace. The next step is designing and
  testing post-tool routing for the bounded multi-round loop.

## 2026-07-29 — Bounded multi-round loop verified

- Added a post-tool router that returns to the tool-bound model while fewer than
  three rounds have completed and forces the unbound finalizer at the limit.
- Replaced the fixed one-round edge with the tested conditional cycle and added
  topology coverage for both post-tool destinations.
- Added a scripted model and deterministic full-graph test using the real local
  `ToolNode`; it executed results `1`, `2`, and `3`, reached exactly three tool
  rounds, then made one forced finalization call.
- A credentialed NVIDIA run exercised the natural early-exit branch:
  `model -> tools -> increment_tool_round -> model -> END`, producing a normal
  answer after one tool result without invoking `final_response`.
- Final checks passed with eleven tests and zero Pyright errors. The next
  reliability boundary is controlled tool failure.

## 2026-07-29 — Remaining LangGraph depth recalibrated

- Chose to survey all remaining Phase 1 mechanisms rather than either skipping
  them or engineering each to production depth.
- The remaining sequence is controlled tool failure; timeout/retry/rate-limit
  intuition; checkpoint and thread isolation; then interrupt/resume.
- Each topic should use one thin runnable probe with visible evidence and stop
  once its behavior is predictable. Broad tests and infrastructure are deferred
  until a concrete failure or the higher-level application requires them.
- Deep Agents follows this compact mechanism survey.
