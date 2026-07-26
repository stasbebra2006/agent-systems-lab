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
- The repository is a uv-managed Python package targeting Python 3.12 with a
  committed lockfile. Homebrew `uv` 0.11.32 and `fd` 10.4.2 are installed on
  the current macOS host; the ignored local virtual environment currently needs
  to be recreated.
- LangGraph 1.2.9, LangChain Core 1.4.9, and
  `langchain-nvidia-ai-endpoints` 1.4.3 are direct application dependencies.
- `src/langgraph_learning/graph.py` defines and compiles a deterministic graph
  with typed `question`/`route`/`answer` state plus a `messages` channel using
  the `add_messages` reducer. Its direct and research answer nodes append
  deterministic `AIMessage` updates. The file now also pins
  `nvidia/nemotron-3-nano-30b-a3b` as the primary model and exposes a lazy
  `create_primary_model()` factory, but neither graph answer node calls it yet.
- `src/langgraph_learning/demo.py` provides an interactive module runner that
  creates a typed initial state containing a `HumanMessage` and streams the
  complete accumulated state after each step. Its output preserves dictionary
  order and separates snapshots with blank lines. Both deterministic branches
  were verified to finish with one human and one AI message.
- `src/langgraph_learning/model_demo.py` performs one isolated
  `ChatNVIDIA.invoke()` with thinking disabled and prints response content,
  usage metadata, and response metadata. The learner ran this credentialed
  smoke test successfully against NVIDIA's hosted development endpoint.
- The generated `langgraph-learning` command still runs its placeholder entry
  point, and automated graph tests have not been added yet.
- An NVIDIA Build account is available and displayed a development limit of up
  to 40 requests per minute on 2026-07-23. A dedicated local development
  credential was used successfully from an ignored, permission-`600` `.env`.
  The local `.env` currently needs to be recreated; a tracked `.env.example`
  now documents the required empty `NVIDIA_API_KEY` variable, and no credential
  value is versioned.
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

Restore the ignored local environment from `.env.example` and recreate the
project virtual environment if needed. Then let the learner replace only
`answer_directly()` with the pending model-backed implementation: create the
primary model, invoke it with `state["messages"]` and `thinking_mode=False`,
and return `response.text` plus `[response]`. Run a short question through the
direct route and inspect how `add_messages` preserves the returned `AIMessage`
metadata. After that works, introduce one deterministic tool and build a
bounded, observable model/tool loop before moving to checkpoints and
interrupt/resume. Keep concurrency below the account limit, add OpenRouter only
for a concrete portability or comparison need, and do not expand the raw
LangGraph layer into a full research-agent framework.
