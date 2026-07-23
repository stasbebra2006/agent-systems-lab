# Learning and Portfolio Roadmap

Last reviewed: 2026-07-23

## Repository decision

Keep this as one Git repository, but do not force every system into one Python
package, virtual environment, container, or process.

The repository is the portfolio narrative and integration surface. Each
third-party system keeps the boundary appropriate to it:

- The low-level LangGraph exercises remain in the root `uv` project.
- The useful Deep Agents application can become its own package when its
  dependency set justifies that split.
- NeMo Agent Toolkit configuration and evaluation artifacts stay beside the
  application they measure.
- AI-Q is run from a pinned upstream release; this repository stores only our
  launch instructions, configuration overlays, extension, and comparison.
- OpenClaw, OpenShell, and NemoClaw keep their mutable state outside Git. This
  repository stores reviewed skills, manifests, policies, and reproducible
  setup notes.

In short: **one repository, several bounded applications and runtimes**.

Do not vendor complete upstream repositories or merge all dependencies into the
root `pyproject.toml`. Use separate `uv` projects, containers, or external
checkouts when dependency or lifecycle boundaries differ.

## Intended final system

```text
User or messaging channel
          |
          v
OpenClaw inside a NemoClaw-managed OpenShell sandbox
          |
          | skill, MCP, or HTTP delegation
          v
AI-Q or our smaller Deep Agents research service
          |
          +-- LangGraph durable runtime
          +-- NeMo Agent Toolkit configuration, traces, profiling, and evals
          +-- search, MCP, and optional enterprise/RAG sources
          +-- selected model providers
```

This is a final integration target, not the shape to build on day one.

## Target learning depth

| Technology | Why it is here | Target depth | Stop when |
| --- | --- | --- | --- |
| LangGraph | Explain and debug the mechanisms under higher layers | Deep foundation | State, reducers, loops, persistence, streaming, and interrupts are understandable and tested |
| Deep Agents | Build the main useful application without recreating a harness | Application-level | One bounded research workflow uses planning, artifacts, a subagent, memory, and approval |
| NeMo Agent Toolkit (NAT) | Add framework-neutral configuration, profiling, and evaluation | Integration-level | The existing workflow runs, traces, profiles, and evaluates through NAT |
| NVIDIA AI-Q Blueprint | Study and extend a production-scale research reference | Operator/extension-level | A pinned release runs and one meaningful component is customized or compared |
| OpenClaw | Explore an always-on, multi-channel assistant runtime | Operator/integration-level | One safe assistant persists sessions and invokes the research capability |
| OpenShell | Learn the underlying security and credential boundary | Security/operator-level | A policy denial, approved access, and credential-isolated inference are demonstrated |
| NemoClaw | Learn NVIDIA's managed OpenClaw/OpenShell lifecycle | Operator-level | Onboarding, inspection, rebuild, recovery, and policy tradeoffs are reproducible |
| Model providers/OpenRouter | Make models replaceable, affordable, and safely credentialed | Cross-cutting | Exact models can be switched without leaking keys or invalidating evaluations |

## Estimated effort

These are focused-hour timeboxes, not targets to fill. Move on early when the
exit criteria are satisfied.

| Phase | Focus | Timebox |
| --- | --- | ---: |
| 0 | Repository, secrets, and model-access baseline | 3–5 h |
| 1 | LangGraph literacy floor | 12–18 h |
| 2 | Useful Deep Agents research application | 12–18 h |
| 3 | NeMo Agent Toolkit integration and evaluation | 8–12 h |
| 4 | AI-Q Blueprint operation and extension | 12–20 h |
| 5 | OpenClaw as an always-on assistant | 8–12 h |
| 6 | OpenShell security runtime | 8–12 h |
| 7 | NemoClaw managed operation | 8–12 h |
| 8 | Integrated public showcase | 15–25 h |
| **Total** | Full exploration and portfolio pass | **86–134 h** |

The minimum useful portfolio is phases 0–4 plus a compact phase 8. OpenClaw,
OpenShell, and NemoClaw are a valuable second track, but they are not
prerequisites for understanding or running AI-Q.

## Phase 0 — Guardrails before model access

### Learn and build

- Define the boundary between committed configuration and local runtime state.
- Ignore `.env` files while allowing sanitized `.env.example` templates.
- Adopt the model and secret practices in
  [`MODEL_ACCESS.md`](MODEL_ACCESS.md).
- Choose a small project-specific spending limit and alert threshold.
- Prepare a dedicated development key instead of reusing a personal
  all-purpose key.
- Decide the first exact tool-capable model before installing its integration.

### Deliverables

- Secret-safe `.gitignore`.
- Written provider strategy and key-rotation procedure.
- Eventually, a sanitized environment example containing names only.
- A documented checklist for the first credentialed-provider smoke test.

### Exit criteria

- A clean clone works after the operator supplies credentials out of band.
- No key appears in Git, example configuration, logs, screenshots, or shell
  commands saved in documentation.
- The development key can be revoked without affecting another project.
- Missing credentials fail clearly rather than silently selecting a provider.

Do not collect keys for every provider now. Add one only when a phase needs it.

## Phase 1 — LangGraph literacy floor

### Learn and build

1. Introduce message state and reducer semantics.
2. Add one model call through a dedicated LangChain provider integration.
3. Add one deterministic tool and a visible model/tool loop.
4. Make termination and iteration limits explicit.
5. Add a request timeout, concurrency limit, and bounded rate-limit backoff.
6. Stream updates and inspect the real state after each step.
7. Add checkpointing and thread identifiers.
8. Implement one interrupt/resume approval.
9. Test the happy path, tool failure, loop limit, rate limit, separate threads,
   and resume.

Start with the NVIDIA hosted development endpoint through
`langchain-nvidia-ai-endpoints` if an exact tool-capable model is available.
Keep OpenRouter optional until broader model choice, fallback routing, or a
provider comparison answers a concrete need. In either case, use a concrete
model identifier rather than automatic routing for reproducible work, and keep
fake or deterministic models in most unit tests.

### Deliverables

- A small, typed graph with messages, one tool loop, persistence, and approval.
- Automated tests for state evolution and failure boundaries.
- A diagram and short explanation of reducers, checkpoints, and interrupts.
- One credentialed NVIDIA smoke test recording the exact model, displayed rate
  cap, tokens, latency, and approximate cost.

### Exit criteria

- The learner can predict each state update before running the graph.
- The graph cannot loop forever.
- Two thread IDs do not share short-term state.
- An interrupted run resumes without restarting completed work.
- Model replacement does not require changing graph topology.
- A rate-limit response is handled without unbounded retries or concurrency.

Do not add multi-agent planning or a large tool catalog in this phase.

## Phase 2 — Useful Deep Agents research application

### Learn and build

- Rebuild the useful behavior with Deep Agents instead of expanding the raw
  graph into a framework.
- Add one search source and require evidence-bearing output.
- Use planning only for tasks that benefit from decomposition.
- Store intermediate evidence and final reports as artifacts.
- Add exactly one focused research subagent.
- Add cross-thread memory only for an identified user need.
- Require human approval for one sensitive or costly operation.
- Start a small evaluation set of roughly 10–20 representative prompts.

### Deliverables

- A research agent that produces a cited Markdown report.
- A visible plan, evidence artifacts, and one subagent trace.
- A permission boundary and an approval example.
- The first repeatable behavior/evaluation dataset.

### Exit criteria

- A shallow question does not trigger unnecessary deep work.
- A research question produces inspectable evidence and citations.
- A subagent has a specific purpose that improves context isolation.
- Failure or refusal from a tool produces a controlled result.
- The same prompt set can be rerun against a second exact model.

Do not reproduce all of AI-Q. This phase creates enough firsthand experience to
understand why AI-Q makes its architectural choices.

## Phase 3 — NeMo Agent Toolkit measurement layer

### Learn and build

- Run the existing LangGraph or Deep Agents graph through NAT.
- Move model, tool, and workflow selection into a non-secret YAML
  configuration where useful.
- Capture traces down to model and tool calls.
- Profile latency, token use, tool counts, and approximate cost.
- Run the existing evaluation dataset through `nat eval`.
- Compare NAT's role with LangSmith instead of enabling multiple overlapping
  systems without a question to answer.

### Deliverables

- Reproducible `nat run` and `nat eval` commands.
- Sanitized NAT configuration using environment-variable substitution.
- A short baseline report covering quality, latency, tokens, and cost.
- A decision note describing NAT versus LangSmith for this project.

### Exit criteria

- NAT adds measurement or configuration value without owning application
  behavior.
- At least one bottleneck or quality failure is visible in a trace.
- An evaluation run is repeatable with the model and dataset versions recorded.
- Secrets remain external to YAML.

## Phase 4 — AI-Q Blueprint as reference and extension

### Learn and build

- Pin a released AI-Q version rather than depending on its moving development
  branch.
- Run both shallow and deep research paths.
- Map its intent classifier, clarifier, researchers, writer, state, and
  evaluation harness to the concepts learned in phases 1–3.
- Run a small subset of its built-in evaluations.
- Customize one meaningful seam: a data-source connector, an evaluation,
  citation policy, model profile, or portable research skill.
- Document what AI-Q solves that the smaller application should not rebuild.

### Deliverables

- Reproducible AI-Q launch notes and non-secret configuration overlay.
- An architecture comparison with the smaller Deep Agents application.
- One focused extension or integration.
- Evaluation results from an exact AI-Q release and exact model configuration.

### Exit criteria

- Both shallow and deep routes work and their cost/latency difference is known.
- The learner can locate LangGraph, Deep Agents, and NAT responsibilities in
  the AI-Q source.
- The extension survives a fresh setup without modifying untracked upstream
  files by hand.
- There is a written decision to reuse, extend, or call AI-Q as a service.

Do not fork AI-Q merely to rename it or copy its whole implementation.

## Phase 5 — OpenClaw runtime

### Learn and build

- Start with WebChat or the local control UI before adding a real messaging
  channel.
- Learn gateway, sessions, memory, tools, skills, plugins, and automation.
- Give the assistant a narrow tool policy and a dedicated workspace.
- Add one reviewed skill that invokes the smaller research service or AI-Q.
- Add one messaging channel only after local behavior is stable.
- Back up and restore its state once.

### Deliverables

- A sanitized OpenClaw configuration description.
- A project-owned research skill.
- One local interface and, optionally, one messaging channel.
- A session/memory and backup demonstration.

### Exit criteria

- The assistant survives restart with the expected state.
- It can invoke the research capability and return its artifact.
- Unapproved host files and tools are not available.
- Channel access is restricted to the intended user or test account.

OpenClaw is the always-on assistant experience; it is not a replacement for the
AI-Q research workflow.

## Phase 6 — OpenShell security runtime

### Learn and build

- Create a minimal sandbox independently of NemoClaw.
- Inspect the CLI, gateway, supervisor, and sandbox roles.
- Write a narrow filesystem and network policy.
- Demonstrate a denied network request and an explicitly allowed one.
- Register a low-scope provider credential and route inference through
  `inference.local`.
- Verify from inside the sandbox that the raw provider key is unavailable.
- Inspect security and lifecycle logs.

### Deliverables

- Reviewed, non-secret policy YAML.
- A deny/allow demonstration and short threat analysis.
- An inference-routing and credential-isolation demonstration.

### Exit criteria

- The learner can explain which controls are static and which can refresh.
- A simulated exfiltration destination is blocked.
- Removing a provider or route causes inference to fail closed.
- The sandbox receives only the files, endpoints, and credentials it needs.

## Phase 7 — NemoClaw managed operation

### Learn and build

- Onboard one OpenClaw sandbox through NemoClaw.
- Compare the generated setup with the manual OpenShell work from phase 6.
- Inspect the versioned blueprint, effective policies, providers, inference
  route, state directories, and logs.
- Exercise connect, status, snapshot, rebuild, and recovery.
- Optionally run Deep Agents Code as a second supported runtime, but do not
  repeat every exercise.
- Record where `nemoclaw` is the supported interface and where lower-level
  `openshell` inspection is appropriate.

### Deliverables

- Reproducible onboarding and recovery notes.
- A NemoClaw-versus-OpenShell decision table.
- A credential and state-flow diagram.
- A documented failure and successful recovery.

### Exit criteria

- A fresh sandbox can be recreated from reviewed, non-secret inputs.
- Provider credentials are not present in the sandbox or repository.
- The assistant recovers after a deliberate stop or rebuild.
- The security differences from unsandboxed OpenClaw are demonstrated.

## Phase 8 — Integrated public showcase

### Build

- Connect the NemoClaw-managed OpenClaw assistant to AI-Q or the smaller
  research service through a skill, MCP, or HTTP boundary.
- Preserve NAT traces and evaluation summaries without publishing sensitive
  prompts or credentials.
- Add architecture diagrams, setup instructions, version pins, and a threat
  model.
- Add CI for deterministic tests and a separately gated provider smoke test.
- Record a short demonstration covering a normal request, a research request,
  an approval, and a blocked security action.
- Verify setup from a clean clone or disposable machine.

### Exit criteria

- The README explains why every layer exists.
- A reviewer can run the deterministic core without paid credentials.
- Credentialed demos fail safely when keys are missing.
- Evaluation results include model, provider, date, dataset version, cost, and
  latency.
- The public repository contains no keys, private transcripts, databases, or
  mutable runtime state.

## Universal move-on rule

A phase is complete when all five statements are true:

1. One useful happy path works.
2. One important failure or denial path is demonstrated.
3. The mechanism can be explained without reading copied tutorial text.
4. A reproducible artifact or test records the result.
5. The next phase has a concrete reason to use what was learned.

If the timebox expires, record the unresolved question and move on unless it
blocks the next phase. Return only when a downstream task makes the missing
depth necessary.

Change one major variable at a time. Do not introduce a new framework, model,
tool source, persistence layer, and deployment environment in the same step.

## Planned repository shape

Create these directories only when their phase begins:

```text
src/langgraph_learning/       # low-level foundation
apps/research_assistant/      # Deep Agents application and its own package
integrations/nat/             # NAT configs, adapters, and evaluation launchers
labs/aiq/                     # pinned-version notes, overlays, and extensions
labs/openclaw/                # reviewed skills and sanitized configuration
labs/openshell/               # sandbox manifests and policies
labs/nemoclaw/                # blueprint inputs and lifecycle notes
evals/                        # datasets, evaluators, and sanitized results
docs/decisions/               # architecture decision records
docs/security/                # threat model and credential-flow diagrams
```

Third-party runtime state, checkpoints containing real conversations, provider
stores, databases, downloaded models, and upstream source checkouts remain
outside Git.

## Current position

The deterministic LangGraph foundation exists. The next implementation change
is message state and reducer semantics in phase 1. Provider installation and
credential registration wait until the first model call is the next single
change.
