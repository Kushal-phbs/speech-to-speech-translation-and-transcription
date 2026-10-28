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
  guidance. See [requirements and acceptance tests](docs/requirements.md)
  and [architecture and provider boundaries](docs/architecture.md).
- `scripts/` — local development and Windows setup helpers.
- `IMPLEMENTATION.md` — the Scrum implementation contract and backlog
  for the full project.

## Getting started

The repository is designed to work on Windows with Python 3.11.

```powershell
git clone https://github.com/VaaniPlus/speech-to-speech-translation-and-transcription.git
cd speech-to-speech-translation-and-transcription
./scripts/setup_windows.ps1
.\.venv\Scripts\Activate.ps1
python -m pytest
```

The setup script requires Python 3.11, creates `.venv`, and installs the
runtime and test dependencies. Heavy STT, translation, and TTS packages are
not included in the default setup; they are listed separately in
`requirements-ml.txt` and must only be installed when an actual model adapter
is implemented. The application uses local defaults; copy `.env.example` to
`.env` to override the host, port, log level, model IDs/cache path, device, or
maximum upload size. Invalid values are reported with the setting name when the
application starts. `.env` and other environment-specific files are ignored by
Git.

Start the API from the repository root with:

```powershell
python -m uvicorn app.main:app --app-dir backend --host 127.0.0.1 --port 8000
```

Interactive API documentation is available at `http://127.0.0.1:8000/docs`.
Application startup initializes only configuration and logging; speech models
are not loaded or downloaded.
The `GET /api/health` endpoint returns `{"status": "ok"}`. Run its API tests
from the repository root with `python -m pytest`.

The UI scaffold can be previewed by opening `frontend/index.html` in a desktop
browser. Direction selection and text character count work locally; microphone,
translation, and audio controls remain disabled until those features are wired
to the API.

## Project workflow

Contributors should work from `main` in short-lived feature branches,
follow the items in `IMPLEMENTATION.md` in order, and open a pull request
for each completed Scrum item. Team members can review the repository
through GitHub after cloning with the command above.

## Current status

- [x] AMTT-1 — Repository and project baseline completed.
- [x] AMTT-2 — Jira backlog, sprint structure, and export completed.
- [x] AMTT-3 — Requirements and acceptance tests.
- [x] AMTT-4 — Architecture and provider boundaries.
- [x] AMTT-5 — Python environment and dependencies.
- [x] AMTT-6 — Environment configuration.
- [x] AMTT-7 — FastAPI application entry point.
- [x] AMTT-8 — Health endpoint and API tests.
- [x] AMTT-9 — Initial browser UI shell.
- [ ] AMTT-10 — Git branching, PR, and review rules.

Sprint 1 remains in progress until all ten items and the release
checkpoint are completed. The detailed plan is maintained in
`IMPLEMENTATION.md`.
