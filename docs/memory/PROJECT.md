# Project Memory

Last updated: 2026-08-05

## Goal

Learn enough low-level LangGraph to understand, inspect, and debug reliable
stateful agents, then apply that foundation through Deep Agents, NeMo Agent
Toolkit, the NVIDIA AI-Q Blueprint, OpenClaw, OpenShell, and NemoClaw in a
project suitable for a public GitHub portfolio.

## Approach

- Use the LangChain Academy Python course as a coverage map, not a requirement
  to watch every video.
- Learn interactively by extending one coherent project.
- Follow the interactive, one-change-at-a-time process documented in
  `docs/LEARNING_WORKFLOW.md`: the assistant implements and verifies each step,
  then pauses for learner review and acknowledgment.
- Treat a dedicated interactive runner as part of completing each runnable
  graph or protocol slice; use `runners/playground.py` only for temporary
  inspection.
- Follow the persistent systems-thinking collaboration contract in
  `docs/memory/COLLABORATION.md`.
- Prefer current official documentation and installed-package behavior when
  older course examples differ.
- Build a small LangGraph literacy floor explicitly, but do not recreate a
  large agent framework when a higher-level abstraction already fits.
- Learn advanced low-level features just in time when Deep Agents, NeMo Agent
  Toolkit, AI-Q, OpenClaw, OpenShell, or NemoClaw exposes a concrete need for
  them.
- Treat reproducibility, observability, security boundaries, and public
  presentation as part of the project rather than end-of-project cleanup.
- Keep `README.md` synchronized after meaningful changes to public
  capabilities, setup, architecture, repository structure, roadmap state, or
  the current next step.
- Keep one portfolio repository but preserve separate package, environment,
  process, and runtime boundaries where the systems have different dependency
  or lifecycle needs.

## Project direction

The project will evolve into a safe, inspectable research agent that can plan,
delegate focused work, preserve evidence, produce useful artifacts, and request
approval for sensitive operations. The raw LangGraph implementation will remain
an explanatory foundation; the main showcase should use appropriate higher-level
frameworks instead of rebuilding their infrastructure.

The intended public narrative is a progression from graph primitives, through
a useful Deep Agents application, NeMo Agent Toolkit profiling and evaluation,
AI-Q operation and extension, OpenClaw usage, and OpenShell/NemoClaw operation
with explicit deployment and security tradeoffs.

## Roadmap

0. Establish repository boundaries, secret hygiene, provider policy, and cost
   controls before the first real model call.
1. Finish the LangGraph literacy floor: messages and reducers, one bounded
   model/tool loop, checkpoints and thread IDs, and interrupt/resume.
2. Build a deliberately small research assistant with Deep Agents.
3. Add NeMo Agent Toolkit as the configuration, profiling, and evaluation
   layer around the working application.
4. Run a pinned NVIDIA AI-Q release, map its architecture to the learned
   concepts, and implement one meaningful extension or comparison.
5. Explore OpenClaw as a separate always-on assistant and connect one reviewed
   research skill.
6. Learn OpenShell directly through explicit policy denial, credential-isolated
   inference, and sandbox inspection.
7. Operate OpenClaw through NemoClaw, then exercise inspection, rebuild, and
   recovery.
8. Integrate and prepare the public showcase with reproducible setup,
   architecture diagrams, evaluation results, a demo, and a threat model.

The detailed timeboxes, deliverables, and exit criteria are canonical in
`docs/ROADMAP.md`. Model-provider and credential practices are canonical in
`docs/MODEL_ACCESS.md`.

For each phase, the completion standard is to explain the mechanism, implement
it without blindly copying, inspect its runtime state, and identify common
failure modes.

## Current status

- The working directory and persistent memory are initialized.
- The project is the public GitHub repository
  `stasbebra2006/agent-systems-lab` on the `main` branch, configured as
  `origin`.
- `Agent Systems Lab` is the repository-level identity spanning the complete
  roadmap. The existing `langgraph_learning` Python package and
  `langgraph-learning` distribution/CLI retain their narrow names because they
  describe only the low-level LangGraph foundation.
- `README.md` is the public entry point and now distinguishes verified current
  behavior from the target architecture, provides credential-free and
  credentialed quick starts, and summarizes the roadmap and engineering
  constraints.
- The repository is a uv-managed Python package targeting Python 3.12, with a
  local virtual environment and committed lockfile.
- LangGraph 1.2.9, LangChain Core 1.4.9, and
  `langchain-nvidia-ai-endpoints` 1.4.3 are direct application dependencies.
  Pytest 9.1.1 is isolated in the uv `dev` dependency group.
- `src/langgraph_learning/models.py` owns the pinned primary model ID and model
  factory. Graphs and runners import this shared provider construction directly,
  so one graph module no longer supplies common infrastructure to another.
- `src/langgraph_learning/graphs/routing.py` defines and compiles a typed graph
  with `question`/`route`/`answer` state plus a `messages` channel using the
  `add_messages` reducer. The direct node now invokes the pinned
  `nvidia/nemotron-3-nano-30b-a3b` model with the accumulated messages and
  thinking disabled, stores the response's text as `answer`, and returns the
  complete `AIMessage` for reducer-backed history. The research node remains
  deterministic.
- `src/langgraph_learning/runners/routing.py` provides an interactive module
  runner that creates a typed initial state containing a `HumanMessage` and
  streams the complete accumulated state after each step. Its output preserves
  dictionary order and separates snapshots with blank lines. Both
  deterministic branches were verified to finish with one human and one AI
  message.
- `src/langgraph_learning/runners/model_call.py` performs one isolated
  `ChatNVIDIA.invoke()` with thinking disabled and prints response content,
  usage metadata, and response metadata. The learner ran this credentialed
  smoke test successfully against NVIDIA's hosted development endpoint.
- The credentialed direct graph route was verified end to end on 2026-07-26.
  Streaming showed the initial state, the router's `direct` decision, and the
  final accumulated human/AI message history. The test used 23 input and 42
  output tokens, and the returned `AIMessage` retained provider and usage
  metadata.
- Pyright 1.1.409 is installed through Neovim's Mason rather than on the normal
  shell `PATH`. Invoking its absolute path with `.venv/bin/python` selected via
  `--pythonpath` reports zero errors.
- `src/langgraph_learning/tools/word_counter.py` defines the first
  deterministic local tool, `count_words`, using LangChain's `@tool`
  decorator. Runtime inspection confirmed that it becomes a `StructuredTool`,
  its required string input and description are inferred correctly, and direct
  invocation returns the expected count.
- `src/langgraph_learning/runners/manual_tool_call.py` binds `count_words` to
  the primary model, inspects the response, then invokes the local tool with
  the returned arguments, prints its result, constructs a `ToolMessage` whose
  `tool_call_id` matches the model request, and sends the ordered message
  history back to the tool-bound model. A credentialed round trip on 2026-07-27
  produced one structured `count_words` request, returned `5` locally,
  generated a final natural-language answer confirming five words, and
  terminated with no further tool calls.
- `src/langgraph_learning/graphs/tool_loop.py` defines reducer-backed message
  state plus a `tool_rounds` counter, a tool-bound model node, deterministic
  routing from an `AIMessage` to tools or termination, a `ToolNode` for
  `count_words`, explicit round accounting, and an unbound final-response model
  node. Its compiled topology returns from round accounting to the tool-bound
  model while `tool_rounds < MAX_TOOL_ROUNDS`, naturally ends on a normal model
  answer, and routes to the unbound finalizer at the three-round limit. The
  finalizer prevents another tool request and guarantees bounded termination.
- `src/langgraph_learning/runners/tool_loop.py` creates the typed initial state,
  streams individual node updates, and separately renders only nonempty
  `AIMessage` values with no tool calls. Credential-free probes verified that a
  direct answer renders while a model tool request, `ToolMessage`, and
  counter-only update remain silent. A credentialed run on 2026-07-29 executed
  `count_words("Hello my friend.")`, returned `3`, incremented `tool_rounds` to
  `1`, and produced a final natural-language answer. NVIDIA accepted the
  accumulated historical tool protocol on the unbound finalization call, which
  used 73 input and 27 output tokens.
- Runtime inspection on 2026-07-29 established the exact update boundary:
  `CompiledStateGraph.stream(..., stream_mode="updates")` returns a generator
  that emits a node-name wrapper around that node's partial state update.
  `ToolNode` executes the structured request from the latest `AIMessage`,
  returns its ordinary result as a matching `ToolMessage` under `messages`,
  and `add_messages` merges that update into the graph's accumulated history.
  Even parallel nodes were observed as separate streamed dictionaries rather
  than one multi-node update.
- A thin credential-free controlled-failure graph inspected on 2026-08-05
  confirmed that the installed `ToolNode` converts malformed tool arguments to
  an error `ToolMessage` by default but re-raises exceptions from valid tool
  execution. The latter emits no completed `tools` update and escapes the graph
  boundary.
- `src/langgraph_learning/runners/playground.py` currently contains the next thin
  reliability probe: a node raises `ConnectionError` twice and succeeds on its
  third attempt under an explicit three-attempt `RetryPolicy`. Runtime inspection
  showed all three executions but only one streamed update, confirming that
  failed attempts did not commit graph state.
- The dedicated tool-loop response view is complete for the current protocol:
  it unwraps each single-node streamed update and renders only a completed,
  nonempty `AIMessage` with no tool calls. Raw streamed updates remain visible
  as the canonical inspection interface alongside the user-facing answer.
- The unused placeholder `langgraph-learning` console script was removed;
  runners are invoked explicitly as Python modules.
- `tests/test_tool_loop.py` provides the deterministic automated baseline:
  eleven pytest cases cover model and post-tool routing outcomes, immutable
  partial round accounting, completed-answer rendering, three filtered protocol
  updates, required bounded-cycle edges, and a full three-tool-round execution
  with a scripted model plus the real local `ToolNode`. The suite makes no
  provider requests.
- An NVIDIA Build account is available and displayed a development limit of up
  to 40 requests per minute on 2026-07-23. A dedicated local development
  credential is stored only in an ignored, permission-`600` `.env` and is
  loaded explicitly with `uv run --env-file .env`; no credential value is
  versioned.
- The learning scope now intentionally stops short of building a full framework
  in raw LangGraph. The repository is expected to become a public portfolio
  demonstration spanning foundations, Deep Agents, NeMo Agent Toolkit, AI-Q,
  OpenClaw, OpenShell, and NemoClaw.
- The project is intentionally one repository with multiple bounded packages
  and runtimes rather than one dependency environment or monolithic process.
- The accepted source restructuring is implemented: `graphs/` owns reusable
  graph definitions, `runners/` owns executable inspection entry points,
  `tools/` owns focused tool modules, and `models.py` remains at the package
  root rather than introducing a generic `core/` directory.

## Next action

Continue the remaining Phase 1 survey with thin vertical probes rather than
production-grade subsystems: finish timeout and local rate-limit behavior;
checkpointing with isolated thread IDs; then interrupt/resume. For each, frame
the problem and meaningful experiment choice with the learner, implement the
smallest runnable example, inspect its control/state behavior together, and stop
once the mechanism is predictable unless a concrete failure requires a focused
test.

Begin by choosing how to isolate and observe a credential-free timeout, then
inspect local request pacing without intentionally provoking provider 429s.
After the remaining mechanism groups, move to Deep Agents. Keep
`runners/playground.py` as the ad hoc inspection file rather than replacing
dedicated runners.
