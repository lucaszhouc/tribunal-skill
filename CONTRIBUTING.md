# Contributing

Thanks for helping improve Tribunal.

## Maintenance model

This is a single-maintainer project, and GitHub notifications are not monitored continuously. Pull-request review can be delayed; email [lucaszhouc@gmail.com](mailto:lucaszhouc@gmail.com) for the fastest response. If a change is time-sensitive, please fork the repository and continue independently rather than waiting on a review.

## Before opening a change

Use an issue to describe substantial behavior changes. Small documentation corrections can go directly to a pull request.

Keep the skill focused on evidence-driven review. New rules should remove a demonstrated failure mode rather than add ceremony, fixed personas, or unconditional tooling.

AI-assisted contributions are welcome, but the contributor must understand and be able to explain every submitted change.

## Pull-request checklist

1. Explain the behavior problem with a concrete example.
2. Make the smallest change that addresses it.
3. Run the metadata validator described below.
4. For instruction changes, run a RED/GREEN or regression scenario and report the rubric, prompt, and observed result.
5. Update `CHANGELOG.md` when behavior changes.

## Validation

From the repository root, run the official skill metadata validator if it is available in your Codex installation:

```powershell
python -X utf8 "$HOME\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .
```

The public behavioral fixture is deliberately small:

```powershell
python -m unittest discover -s tests/fixture -v
```

The fixture's existing test is expected to pass even though the implementation contains two seeded contract violations. It tests reviewer behavior, not a production implementation. See [tests/EFFECT_TEST.md](tests/EFFECT_TEST.md).

## Style and commits

- Keep `SKILL.md` concise and runtime-agnostic where possible.
- Do not include credentials, private paths, transcripts, or proprietary fixtures.
- Use clear, ASCII commit messages.
- Do not add AI co-author trailers. Describe material AI assistance in `AUTHORS.md` instead.

By contributing, you agree that your contribution is licensed under the MIT License.
