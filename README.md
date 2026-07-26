# LangGraph Learning Lab

A project-driven environment for learning LangGraph by building a useful,
stateful agent rather than only completing disconnected tutorials.

The project intentionally implements only enough raw LangGraph to make state,
routing, tool loops, persistence, and interrupts understandable. It will then
evolve into a public-facing research-agent demonstration built with Deep Agents,
informed by NVIDIA AI-Q and measured with NeMo Agent Toolkit, with separate
OpenClaw experiments and NemoClaw/OpenShell deployment and security work.

The goal is not framework reimplementation. The goal is to show how agent
primitives, higher-level harnesses, and constrained runtime operation fit
together in one inspectable and reproducible project.

The [LangChain Academy Introduction to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph)
provides the curriculum map. We will implement its important concepts in one
evolving project and check examples against the current official documentation.

Project context and progress are recorded in
[`docs/memory/PROJECT.md`](docs/memory/PROJECT.md).

The time-boxed learning sequence and completion criteria are in
[`docs/ROADMAP.md`](docs/ROADMAP.md). Model-provider and credential rules are in
[`docs/MODEL_ACCESS.md`](docs/MODEL_ACCESS.md).

## Local environment

Recreate the locked Python environment and copy the credential template:

```sh
uv sync --locked
cp .env.example .env
chmod 600 .env
```

Add the local `NVIDIA_API_KEY` to `.env`. Never commit the populated file.
