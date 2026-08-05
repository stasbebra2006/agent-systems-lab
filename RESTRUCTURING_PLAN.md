# Codebase Restructuring & Organization Plan

Status: implemented on 2026-07-28.

## Objective

Organize `langgraph_learning` by responsibility while keeping the small package
easy to navigate. Reusable graphs, executable runners, shared model
construction, and focused tools have explicit ownership.

---

## Target Directory Structure

```text
agent-systems-lab/
├── src/
│   └── langgraph_learning/
│       ├── __init__.py             # Package marker
│       ├── models.py               # Primary model selection and construction
│       ├── tools/                  # Focused local tool modules
│       │   ├── __init__.py
│       │   ├── deliberate_failure.py
│       │   └── word_counter.py
│       ├── graphs/                 # Reusable LangGraph definitions
│       │   ├── __init__.py
│       │   ├── retry.py
│       │   ├── routing.py
│       │   ├── timeout.py
│       │   ├── tool_failure.py
│       │   └── tool_loop.py
│       └── runners/                # Executable inspection entry points
│           ├── __init__.py
│           ├── manual_tool_call.py
│           ├── model_call.py
│           ├── retry.py
│           ├── routing.py
│           ├── timeout.py
│           ├── tool_failure.py
│           └── tool_loop.py
├── docs/
├── README.md
└── pyproject.toml
```

---

## File Mapping Table

| Previous path | Implemented path | Rationale |
| :--- | :--- | :--- |
| `src/langgraph_learning/models.py` | unchanged | One focused shared module does not justify a generic `core/` package |
| `src/langgraph_learning/tools.py` | `src/langgraph_learning/tools/word_counter.py` | Convert single tools file into a modular tools directory |
| `src/langgraph_learning/demos/model_call.py` | `src/langgraph_learning/runners/model_call.py` | Distinguish executable adapters from reusable definitions |
| `src/langgraph_learning/demos/manual_tool_call.py` | `src/langgraph_learning/runners/manual_tool_call.py` | Distinguish executable adapters from reusable definitions |
| `src/langgraph_learning/demos/routing.py` | `src/langgraph_learning/runners/routing.py` | Distinguish executable adapters from reusable definitions |
| `src/langgraph_learning/demos/playground.py` | matching `graphs/` and `runners/` modules for retry, timeout, and tool failure | Preserve useful probes while separating topology from execution adapters |
| *(New)* | `src/langgraph_learning/tools/deliberate_failure.py` | Keep the probe tool under tool ownership |
| *(New)* | matching `graphs/tool_loop.py` and `runners/tool_loop.py` | Separate reusable topology from interactive streaming |

---

## Implemented Steps

1. Created `tools/` and `runners/` packages.
2. Moved and renamed existing files without changing their established runtime
   behavior.
3. Added stable graph/runner pairs for the tool loop and the credential-free
   tool-failure, retry, and timeout probes; focused tool definitions remain in
   `tools/`.
4. Updated imports, public commands, package metadata, and persistent memory.
5. Removed the unused placeholder console script; runners use explicit
   `python -m` module paths.

## Testing

Pytest is a locked development dependency. Deterministic graph tests use
controlled model behavior and make no provider requests. Pyright remains the
Mason-managed installation documented in project memory.
