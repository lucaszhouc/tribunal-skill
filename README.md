# Tribunal Skill

> **English** · [中文](README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Codex Skill](https://img.shields.io/badge/Codex-skill-111827)](SKILL.md)
[![Claude Code Compatible](https://img.shields.io/badge/Claude_Code-compatible-D97757)](SKILL.md)
[![Behavior Tested](https://img.shields.io/badge/behavior-tested-16A34A)](tests/EFFECT_TEST.md)

An evidence-driven review skill for finished products, UI changes, and code changes. Tribunal selects only the review perspectives that add independent information, reproduces findings before accepting them, and keeps review scope separate from permission to modify or publish.

Tribunal is an original skill, not a fork of another project.

## Why Tribunal

Multi-agent reviews often become role-play: fixed panels, repeated screenshots, long scorecards, and many unverified opinions. Tribunal instead enforces four useful properties:

- **Evidence before findings** — reproduce or inspect the actual artifact.
- **Adaptive review lanes** — select product, interface, or engineering perspectives only when relevant.
- **Bounded output** — prioritize a small number of consequential findings.
- **Permission safety** — review-only does not silently become editing, deployment, or submission.

## Use it for

- A major feature or refactor with a runnable artifact or inspectable diff.
- A release candidate, milestone, or high-risk workflow.
- A product review that needs user, interface, and reliability perspectives to meet on the same evidence.

Do not use it for a one-line copy change, early ideation without an artifact, or a narrow check that can be answered directly.

## Installation

Clone the repository into a skill directory recognized by your agent runtime.

### Codex

```powershell
git clone https://github.com/lucaszhouc/tribunal-skill.git "$HOME\.agents\skills\tribunal"
```

If your Codex setup uses `$CODEX_HOME/skills`, clone or copy the repository to `$CODEX_HOME/skills/tribunal` instead.

### Claude Code

```powershell
git clone https://github.com/lucaszhouc/tribunal-skill.git "$HOME\.claude\skills\tribunal"
```

Restart or open a new agent session after installation so the skill catalog is refreshed.

## Usage

Invoke it explicitly when you want a deep, bounded review:

```text
Use $tribunal to review this release candidate. Review only; do not modify or deploy it.
```

To authorize fixes, say so explicitly:

```text
Use $tribunal to review this feature, fix accepted in-scope issues, and rerun its checks.
```

Tribunal can use available delegation, but it does not require multiple agents. The primary agent remains responsible for evidence, deduplication, judgment, and verification.

## Behavioral test

The lightweight RED/GREEN test uses a small settings feature whose existing test passes while two contract violations remain: shallow nested merging and non-atomic persistence.

| Run | Candidate skill loaded | Gates passed |
|---|---:|---:|
| RED baseline | No | 4/6 |
| GREEN | Yes | 6/6 |
| REFACTOR verification | Yes | 6/6 |

The test checks evidence gathering, detection of a seeded data-loss risk, review-only behavior, avoidance of fixed-role theatre, finding quality, and an evidence-based release decision. See [tests/EFFECT_TEST.md](tests/EFFECT_TEST.md).

The baseline already found the two seeded defects. Tribunal's measured improvement was narrower and still useful: GREEN replaced the requested four-role panel with three relevant lanes and returned a smaller, consistently actionable decision record, although it still included a readiness score. The v2.0.1 regression run also rejected the unnecessary score.

## Maintenance and contact

This is a single-maintainer project. GitHub notifications may be reviewed slowly; email is the fastest contact method: [lucaszhouc@gmail.com](mailto:lucaszhouc@gmail.com).

Security reports should follow [SECURITY.md](SECURITY.md). Contributions are welcome under [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
