# Agent Entry Point

This repository uses `docs/memory/` as its canonical persistent memory.

At the start of a session, read `docs/memory/PROJECT.md`.

After meaningful work, update its current facts and next action, then append a
concise entry to `docs/memory/SESSION_LOG.md`.

If information conflicts, prefer working code and tests, then `PROJECT.md`, then
older session-log entries. Do not duplicate project facts here.
