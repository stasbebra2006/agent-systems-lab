# Model Access and Secret Practices

Last reviewed: 2026-07-23

This policy applies to local development, CI, demos, AI-Q, OpenClaw, OpenShell,
and NemoClaw work in this repository.

## Provider strategy

Use an aggregator where it improves exploration, but do not make one
credential or endpoint serve every purpose.

### Recommended progression

1. **Initial LangGraph and Deep Agents work:** use the NVIDIA API Catalog hosted
   development endpoint with the dedicated `langchain-nvidia-ai-endpoints`
   integration and one exact, tool-capable model.
2. **Portability or provider comparison:** add OpenRouter only when broader
   model choice, fallback routing, or centralized billing answers a concrete
   need, then repeat a small test through one exact model and upstream provider.
3. **NAT and AI-Q work:** use their documented provider configuration, starting
   with a dedicated NVIDIA development key when following NVIDIA examples.
4. **OpenClaw exploration:** use a project-specific provider profile; add an
   OpenRouter profile only if the runtime benefits from its model catalog or
   routing.
5. **OpenShell/NemoClaw:** register credentials with the OpenShell provider
   boundary and use routed inference rather than placing raw keys inside the
   sandbox.

OpenRouter is convenient because one API and credential can reach many models.
That convenience does not remove the need to control the exact model, upstream
provider, privacy policy, budget, and fallback behavior.

For evaluations:

- Pin a concrete model identifier; do not use `auto` or a moving “latest”
  alias.
- Record the resolved model, upstream provider, date, parameters, and
  integration version.
- Disable fallbacks unless fallback behavior is what the test measures.
- Use the same prompt dataset and tool versions when comparing models.

For interactive exploration, automatic routing and fallback are acceptable
when availability matters more than reproducibility.

## Model roles

Keep model identifiers in versioned, non-secret configuration. Assign models by
role instead of scattering provider names through application code:

| Role | Purpose |
| --- | --- |
| `fast` | Routing, classification, and small transformations |
| `primary` | Normal tool-calling conversation |
| `research` | Planning, evidence synthesis, and long reports |
| `evaluator` | Quality scoring, preferably from a different model family |
| `embedding` | Retrieval only, when that phase is introduced |

Do not add every role immediately. Start with `primary`; add a role only when
measurements show a reason.

## Key boundaries

Create a different key for each meaningful blast radius:

- Local development
- CI smoke tests
- Public or shared demo
- OpenClaw runtime
- AI-Q/NVIDIA experiments

Where supported, give each key:

- A descriptive name
- The lowest useful scope
- A small spending limit
- An expiration date
- Provider and model allowlists
- Zero-data-retention enforcement when the data requires it

An OpenRouter management key is administrative and must never be used as the
normal inference key.

## Local storage

Preferred order:

1. Inject a key for one command or shell session from an OS keychain or secret
   manager.
2. Use an ignored, permission-restricted local `.env` only when the tool
   requires or materially benefits from it.
3. Use a tool-owned credential store only after understanding its storage and
   access boundary.

Committed files may reference environment-variable names, but never values:

```yaml
api_key: ${NVIDIA_API_KEY}
```

Sanitized examples use empty values:

```dotenv
OPENROUTER_API_KEY=
NVIDIA_API_KEY=
```

Load only the variables required by the current component. A research service
does not need messaging credentials, and an OpenClaw sandbox does not need every
direct model-provider key.

## Never put a key in

- Python, JavaScript, YAML, TOML, notebooks, or test fixtures
- Git history, including a “temporary” private commit
- README files, issue reports, screenshots, or copied terminal output
- Frontend or mobile application code
- Container images or Dockerfiles
- URLs or command arguments that are stored in shell history
- Traces, evaluation datasets, prompts, exception messages, or debug logs

If a secret enters Git, deleting the line is not remediation. Revoke or rotate
the key first, then clean history if necessary.

## Registration by component

| Component | Non-secret model configuration | Credential boundary |
| --- | --- | --- |
| LangGraph/LangChain | Provider package plus exact `provider:model` identifier | Process environment or local secret injection |
| Deep Agents | Exact `provider:model` string or configured LangChain model | Provider-specific environment variable |
| NeMo Agent Toolkit | YAML LLM definition with `${VARIABLE}` substitution | Process environment or deployment secret manager |
| AI-Q | Pinned YAML overlay defining roles, models, and tools | Environment substitution; never commit populated config |
| OpenClaw | Provider auth profile and exact model reference | Dedicated OpenClaw credential/profile boundary |
| OpenShell | Provider record plus `inference.local` route | Gateway injects the credential at egress |
| NemoClaw | Onboarding choice and generated runtime configuration | Registers transient host input with OpenShell; sandbox sees no raw key |

Use each project's native provider integration when available. For the initial
LangChain work, use `ChatNVIDIA` from `langchain-nvidia-ai-endpoints`. If
OpenRouter is added later, prefer `ChatOpenRouter`/`langchain-openrouter` over
pretending it is the official OpenAI endpoint; dedicated integrations preserve
provider-specific metadata and controls.

## Cost and reliability controls

Every real model loop must have:

- A request timeout
- A bounded retry policy
- A maximum tool/agent iteration count
- A maximum output-token budget
- A concurrency limit for research workers
- Token and cost collection where the provider supplies usage
- A per-run or per-job budget for deep research

Use fake models or recorded deterministic responses for unit tests. Put real
provider tests behind an explicit marker or command so ordinary test runs do
not spend money.

Start with a cheap tool-capable model for graph mechanics. Upgrade only after an
evaluation demonstrates a capability gap. A model that cannot reliably call
tools or produce the required structured output is unsuitable even if its chat
quality is good.

## NVIDIA Build/NIM development-endpoint checks

Before using an NVIDIA development key:

1. Confirm the current account and model rate limits in NVIDIA Build; do not
   interpret “no daily limits” as the absence of per-minute or concurrency
   limits.
2. Pin one exact model and verify that it supports the tool-calling behavior the
   graph requires.
3. Bound graph and subagent concurrency, and handle HTTP `429` responses with a
   limited retry policy and backoff.
4. Estimate requests per complete agent run rather than treating one user task
   as one API request.
5. Record the endpoint, model, date, displayed rate cap, tokens, and latency in
   credentialed smoke tests and evaluations.
6. Treat the hosted serverless endpoint as development capacity. Revisit a paid
   endpoint, dedicated deployment, or self-hosted NIM before making
   production-reliability claims.

The provider cards on NVIDIA Build are optional external account integrations.
Do not assume that connecting one extends the NVIDIA key or quota; inspect the
provider's credentials, billing, data handling, and authorization flow first.

## OpenRouter-specific checks

Before using an OpenRouter key:

1. Set a small key-level spending limit and expiration.
2. Restrict model/provider access where practical.
3. Review prompt-logging and data-use settings.
4. Enable the appropriate zero-data-retention controls for sensitive work.
5. Keep prompt/response logging off unless a specific debugging task needs it.
6. Record the resolved provider and model in evaluation results.

Requests traverse OpenRouter and an upstream model provider. Evaluate both
parties' policies for sensitive data.

## OpenShell and NemoClaw checks

- Use `inference.local` rather than allowlisting the upstream inference host.
- Keep raw provider credentials in the OpenShell gateway provider store.
- Verify from inside the sandbox that the raw key is absent.
- Give search, GitHub, messaging, and MCP integrations separate low-scope
  credentials.
- Remove a provider when the integration no longer needs it.
- Exercise rotation and fail-closed behavior before treating the setup as
  production-like.

## Incident procedure

If a key may have been exposed:

1. Revoke or rotate it immediately.
2. Stop affected jobs or sandboxes.
3. Review provider usage and charges.
4. Search Git history, logs, traces, artifacts, and screenshots for the value.
5. Remove leaked material and rewrite Git history only after revocation.
6. Replace the key through the correct secret boundary.
7. Record the cause and add a preventive check.

## Initial project choice

When phase 1 reaches its first model-backed node, the default recommendation is:

- The NVIDIA API Catalog hosted development endpoint
- `ChatNVIDIA` from the dedicated `langchain-nvidia-ai-endpoints` package
- One exact, inexpensive model verified to support tool calling
- A development-only `NVIDIA_API_KEY`
- Concurrency below the currently displayed account limit, with bounded
  retries for rate limiting
- A fake model for deterministic tests

OpenRouter remains the first optional addition when model diversity, fallback
routing, or provider comparison becomes useful.

The exact model is selected at that time from current provider documentation
and measured behavior, not permanently hard-coded in this policy.

## Primary references

- [LangChain providers, models, and routers](https://docs.langchain.com/oss/python/concepts/providers-and-models)
- [LangChain ChatNVIDIA integration](https://docs.langchain.com/oss/python/integrations/chat/nvidia_ai_endpoints)
- [Deep Agents model configuration](https://docs.langchain.com/oss/python/deepagents/models)
- [NVIDIA Build API keys](https://build.nvidia.com/settings/api-keys)
- [OpenRouter quickstart](https://openrouter.ai/docs/quickstart)
- [OpenRouter guardrails](https://openrouter.ai/docs/guides/features/guardrails/overview)
- [OpenRouter data collection](https://openrouter.ai/docs/guides/privacy/data-collection)
- [OpenRouter zero-data-retention controls](https://openrouter.ai/docs/guides/features/zdr)
- [NAT quickstart and environment variables](https://docs.nvidia.com/nemo/agent-toolkit/latest/get-started/quick-start.html)
- [AI-Q configuration reference](https://docs.nvidia.com/aiq-blueprint/2.0.0/customization/configuration-reference.html)
- [OpenShell inference routing](https://docs.nvidia.com/openshell/latest/sandboxes/inference-routing)
- [NemoClaw credential storage](https://docs.nvidia.com/nemoclaw/user-guide/openclaw/security/credential-storage)
