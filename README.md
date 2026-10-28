# AI-Mediated English ↔ Hindi Speech Translation

A browser-based, local-first speech translation application that accepts
microphone audio or typed text and translates in two directions: English
→ Hindi and Hindi → English. The browser displays the source transcript
and translated text and can play generated target-language audio.

## Scope

This project intentionally supports English and Hindi only. It does not
include other languages, multi-party calls, user accounts, cloud
deployment, or voice cloning. Audio and text are intended to stay local;
do not send them to external services unless the team explicitly documents
and approves that integration.

## Repository layout

- `backend/` — FastAPI application, provider boundaries, service logic,
  schemas, and backend tests.
- `frontend/` — browser UI, styles, and client-side interaction code.
- `docs/` — requirements, architecture, API, testing, and demonstration
  guidance. See [Requirements and acceptance tests](docs/requirements.md)
  for functional/non-functional requirements and user journeys.
- `scripts/` — local development and Windows setup helpers.
- `IMPLEMENTATION.md` — the Scrum implementation contract and backlog
  for the full project.

## Getting started

The repository is designed to work on Windows with Python 3.11.

```powershell
git clone https://github.com/VaaniPlus/speech-to-speech-translation-and-transcription.git
cd speech-to-speech-translation-and-transcription
./scripts/setup_windows.ps1
```

At later setup stages, the Windows setup script will create the local
Python environment and install project dependencies. Copy `.env.example`
to `.env` only when local configuration is needed; `.env` and other
environment-specific files are ignored by Git.

## Project workflow

Contributors should work from `main` in short-lived feature branches,
follow the items in `IMPLEMENTATION.md` in order, and open a pull request
for each completed Scrum item. Team members can review the repository
through GitHub after cloning with the command above.

## Current status

- [x] AMTT-1 — Repository and project baseline completed.
- [x] AMTT-2 — Jira backlog, sprint structure, and export completed.
- [x] AMTT-3 — Requirements and acceptance tests.
- [ ] AMTT-4 — Architecture and provider boundaries.
- [ ] AMTT-5 — Python environment and dependencies.
- [ ] AMTT-6 — Environment configuration.
- [ ] AMTT-7 — FastAPI application entry point.
- [ ] AMTT-8 — Health endpoint and API tests.
- [ ] AMTT-9 — Initial browser UI shell.
- [ ] AMTT-10 — Git branching, PR, and review rules.

Sprint 1 remains in progress until all ten items and the release
checkpoint are completed. The detailed plan is maintained in
`IMPLEMENTATION.md`.
