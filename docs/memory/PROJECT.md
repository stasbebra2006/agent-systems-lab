# Project Memory

Last updated: 2026-07-26

## Goal

Learn enough low-level LangGraph to understand, inspect, and debug reliable
stateful agents, then apply that foundation through Deep Agents, NeMo Agent
Toolkit, the NVIDIA AI-Q Blueprint, OpenClaw, OpenShell, and NemoClaw in a
project suitable for a public GitHub portfolio.

## Approach

- Use the LangChain Academy Python course as a coverage map, not a requirement
  to watch every video.
- Learn interactively by extending one coherent project.
- Follow the learner-driven, one-change-at-a-time process documented in
  `docs/LEARNING_WORKFLOW.md`.
- Prefer current official documentation and installed-package behavior when
  older course examples differ.
- Build a small LangGraph literacy floor explicitly, but do not recreate a
  large agent framework when a higher-level abstraction already fits.
- Learn advanced low-level features just in time when Deep Agents, NeMo Agent
  Toolkit, AI-Q, OpenClaw, OpenShell, or NemoClaw exposes a concrete need for
  them.
- Treat reproducibility, observability, security boundaries, and public
  presentation as part of the project rather than end-of-project cleanup.
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
- The project is a Git repository on the `main` branch, with private GitHub
  remote `stasbebra2006/langgraph-learning` configured as `origin`.
- The repository is a uv-managed Python package targeting Python 3.12, with a
  local virtual environment and committed lockfile.
- LangGraph 1.2.9, LangChain Core 1.4.9, and
  `langchain-nvidia-ai-endpoints` 1.4.3 are direct application dependencies.
- `src/langgraph_learning/graph.py` defines and compiles a typed graph with
  `question`/`route`/`answer` state plus a `messages` channel using the
  `add_messages` reducer. The direct node now invokes the pinned
  `nvidia/nemotron-3-nano-30b-a3b` model with the accumulated messages and
  thinking disabled, stores the response's text as `answer`, and returns the
  complete `AIMessage` for reducer-backed history. The research node remains
  deterministic.
- `src/langgraph_learning/demo.py` provides an interactive module runner that
  creates a typed initial state containing a `HumanMessage` and streams the
  complete accumulated state after each step. Its output preserves dictionary
  order and separates snapshots with blank lines. Both deterministic branches
  were verified to finish with one human and one AI message.
- `src/langgraph_learning/model_demo.py` performs one isolated
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
- `src/langgraph_learning/tools.py` defines the first deterministic local tool,
  `count_words`, using LangChain's `@tool` decorator. Runtime inspection
  confirmed that it becomes a `StructuredTool`, its required string input and
  description are inferred correctly, and direct invocation returns the
  expected count.
- `src/langgraph_learning/tool_call_demo.py` binds `count_words` to the primary
  model, inspects the response, then invokes the local tool with the returned
  arguments and prints its result. A credentialed run produced one structured
  `count_words` request containing the expected text argument, a unique call
  ID, and no substantive assistant content; direct local execution returned
  `5`. The demo intentionally stops before constructing a `ToolMessage` or
  sending the result back to the model.
- The generated `langgraph-learning` command still runs its placeholder entry
  point, and automated graph tests have not been added yet.
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
- A time-boxed 86–134 focused-hour roadmap and a cross-cutting model/secret
  policy are documented. The initial provider preference is NVIDIA's hosted
  development endpoint, with OpenRouter retained as an optional later
  portability layer. `.env` variants are ignored before any credentials are
  introduced.

## Next action

Extend the isolated demo by constructing a `ToolMessage` from the local result
whose `tool_call_id` matches the model's request. Inspect that message before
sending anything back to the model. Then complete the response round trip and
build the visible graph loop with an explicit iteration bound and controlled
tool-failure behavior. Keep concurrency below the account limit, add OpenRouter
only for a concrete portability or comparison need, and do not expand the raw
LangGraph layer into a full research-agent framework.
