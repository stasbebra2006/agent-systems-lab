# Agent Entry Point

This repository uses `docs/memory/` as its canonical persistent memory.

At the start of a session, read `docs/memory/PROJECT.md` and
`docs/memory/COLLABORATION.md`.

Re-read `docs/memory/COLLABORATION.md` before a new substantial task,
architecture or framework decision, comparison of multiple system-level
approaches, or continuation after context compaction or a session handoff.
Re-read it as a corrective when the user says the reasoning has become too
local, linear, abstract, or disconnected from implementation. Do not reload it
for simple factual questions or mechanical one-step edits.

After meaningful work, update its current facts and next action, then append a
concise entry to `docs/memory/SESSION_LOG.md`.

Treat `README.md` as the public view of the project. In the same turn, update it
when meaningful work changes public capabilities, setup instructions,
architecture, repository structure, roadmap state, or the current next step.
Do not rewrite it for discussion-only turns or changes that affect only
internal collaboration memory.

If information conflicts, prefer working code and tests, then `PROJECT.md`, then
older session-log entries. Do not duplicate project facts here.
