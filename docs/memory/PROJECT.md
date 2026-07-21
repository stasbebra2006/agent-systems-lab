# Project Memory

Last updated: 2026-07-21

## Goal

Learn enough low-level LangGraph to understand, inspect, and debug reliable
stateful agents, then apply that foundation through Deep Agents, OpenClaw, and
NemoClaw in a project suitable for a public GitHub portfolio.

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
- Learn advanced low-level features just in time when Deep Agents, OpenClaw, or
  NemoClaw exposes a concrete need for them.
- Treat reproducibility, observability, security boundaries, and public
  presentation as part of the project rather than end-of-project cleanup.

## Project direction

The project will evolve into a safe, inspectable research agent that can plan,
delegate focused work, preserve evidence, produce useful artifacts, and request
approval for sensitive operations. The raw LangGraph implementation will remain
an explanatory foundation; the main showcase should use appropriate higher-level
frameworks instead of rebuilding their infrastructure.

The intended public narrative is a progression from graph primitives, through
a useful Deep Agents application, to OpenClaw usage and NemoClaw/OpenShell
operation with explicit deployment and security tradeoffs.

## Roadmap

1. Complete the deterministic foundation: state, nodes, edges, conditional
   routing, visualization, and streamed updates.
2. Finish the LangGraph literacy floor: messages and reducers, one model/tool
   loop with termination, checkpoints and thread IDs, and interrupt/resume.
3. Build the useful research assistant with Deep Agents, using planning,
   filesystem context, focused subagents, memory, and human approval where each
   capability has a clear purpose.
4. Explore OpenClaw as a separate always-on assistant runtime and create a
   relevant skill or configuration around the same research workflow.
5. Operate supported Deep Agents Code and OpenClaw variants through
   NemoClaw/OpenShell, documenting inference routing, credentials, sandbox
   policy, and reproducible lifecycle management.
6. Prepare the repository for public release with a strong README, architecture
   diagrams, a demo, safe configuration examples, a threat model, and a small
   behavior/evaluation suite.

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
- The learning scope now intentionally stops short of building a full framework
  in raw LangGraph. The repository is expected to become a public portfolio
  demonstration spanning foundations, Deep Agents, OpenClaw, and NemoClaw.

## Next action

Introduce message state and reducer semantics with the smallest useful change.
Then choose a model provider and implement one observable model/tool loop before
moving on to checkpoints and interrupt/resume. Do not expand the raw LangGraph
layer into a full research-agent framework.
