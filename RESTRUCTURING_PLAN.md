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
│       │   └── word_counter.py
│       ├── graphs/                 # Reusable LangGraph definitions
│       │   ├── __init__.py
│       │   ├── routing.py
│       │   └── tool_loop.py
│       └── runners/                # Executable inspection entry points
│           ├── __init__.py
│           ├── manual_tool_call.py
│           ├── model_call.py
│           ├── playground.py
│           ├── routing.py
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
| `src/langgraph_learning/demos/playground.py` | `src/langgraph_learning/runners/playground.py` | Provide one editable inspection workbench |
| *(New)* | `src/langgraph_learning/runners/tool_loop.py` | Stream the current one-round graph |

---

## Implemented Steps

1. Created `tools/` and `runners/` packages.
2. Moved and renamed existing files without changing their established runtime
   behavior.
3. Added a stable tool-loop runner and an editable, credential-free playground.
4. Updated imports, public commands, package metadata, and persistent memory.
5. Removed the unused placeholder console script; runners use explicit
   `python -m` module paths.

## Deferred Testing Step

Automated tests will be introduced with the next behavior that needs them,
rather than creating empty test hierarchies and fixtures in advance. At that
point, add `pytest` as a locked development dependency, start with the
deterministic word-count tool, and add graph tests with controlled model
behavior. Pyright currently remains the Mason-managed installation documented
in project memory.
