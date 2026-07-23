# Project Memory

Last updated: 2026-07-23

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
- An NVIDIA Build account is available and displayed a development limit of up
  to 40 requests per minute on 2026-07-23. No model-provider package, API key,
  or credential is configured in the project, which remains intentional for
  the first deterministic graph.
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

Introduce message state and reducer semantics with the smallest useful change.
Then choose a model provider and implement one observable model/tool loop before
moving on to checkpoints and interrupt/resume. Do not expand the raw LangGraph
layer into a full research-agent framework, and defer NeMo Agent Toolkit until
the application has real model and tool behavior worth measuring. When the
first model call becomes the next change, start with the NVIDIA hosted
development endpoint, select one exact tool-capable model, create only its
dedicated development credential, and bound concurrency below the account's
current limit. Add OpenRouter only when portability, fallback, or model
comparison provides a concrete benefit.
