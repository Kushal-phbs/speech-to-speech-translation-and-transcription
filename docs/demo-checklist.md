# Demo checklist

Use this checklist for the S1 requirements review and later release demos.
Run the product on a clean local checkout and record only observable pass/fail
results. Mocked providers are valid for UI/API checks, but real-model outputs
must be labeled as such.

## Pre-demo setup

- [ ] Repository and environment setup instructions have been reviewed.
- [ ] The backend starts successfully and API documentation is reachable.
- [ ] The frontend loads on a supported desktop browser.
- [ ] Automated tests run without model downloads or GPU access.
- [ ] Browser is opened over `localhost` or HTTPS so microphone capture is
  available.
- [ ] Microphone permission is reset before testing the permission flow.

## Core text pipeline

- [ ] Select `en-to-hi` and submit non-empty English text.
- [ ] Verify the source text, Hindi translation, and success status are shown.
- [ ] Select `hi-to-en` and submit non-empty Hindi text.
- [ ] Verify the source text, English translation, and success status are shown.
- [ ] Submit empty or whitespace-only text and verify useful validation.
- [ ] Submit an invalid direction and verify useful API/UI feedback.

## Speech pipeline

- [ ] Grant microphone permission and record a short English utterance.
- [ ] Stop the recording and verify progress, English transcript, Hindi
  translation, and playable Hindi audio.
- [ ] Grant/reset permission and record a short Hindi utterance.
- [ ] Stop the recording and verify progress, Hindi transcript, English
  translation, and playable English audio.
- [ ] Deny microphone permission and verify clear recovery guidance.
- [ ] Reset while audio is active and verify playback stops and visible state
  clears.
- [ ] Retry after a recoverable failure and verify stale results are not
  retained.

## Error and accessibility checks

- [ ] STT, translation, and TTS failures show separate, recoverable messages
  in test configuration.
- [ ] Errors do not expose Python tracebacks or private local paths.
- [ ] All controls have visible labels and keyboard focus is usable.
- [ ] Loading, success, and error states are visually distinguishable.
- [ ] Fast repeated submissions do not overwrite an earlier or later result.

## Instructor-facing review

- [ ] Both supported directions are identified explicitly.
- [ ] Typed-text fallback is demonstrated.
- [ ] Speech, translation, and audio stages are explained as replaceable
  provider boundaries.
- [ ] The scope explicitly excludes unsupported languages and cloud features.
- [ ] Fake-provider tests are distinguished from real model demonstrations.
- [ ] Known limitations and setup steps are summarized.
- [ ] The presenter states that the demo does not claim perfect translation
  quality.

See [requirements.md](requirements.md) for the complete functional,
non-functional, journey, and acceptance criteria.
