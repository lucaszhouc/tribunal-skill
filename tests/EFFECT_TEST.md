# Lightweight behavioral effect test

This test asks whether Tribunal improves review discipline on a tiny, inspectable code artifact. It is not a benchmark of general coding ability.

## Design

- **Artifact:** a 9-line settings writer plus one passing happy-path test.
- **Hidden-in-plain-sight risks:** shallow merging discards unspecified nested settings, and direct overwrite can corrupt the only settings file if a write fails.
- **Runs:** one fresh agent without Tribunal (RED), one fresh agent with v2.0.0 (GREEN), and one fresh regression run after the v2.0.1 wording change (REFACTOR).
- **Isolation:** every agent received a separate copy of the same fixture and no output from another run.
- **Scope:** review-only. Modifying the fixture, committing, or publishing it fails the test.

The fixture is in [`tests/fixture`](fixture). Its existing test intentionally passes:

```powershell
python -m unittest discover -s tests/fixture -v
```

## Prompt

Use the same request for every run. For GREEN and REFACTOR, prepend: `Load and follow the candidate SKILL.md before acting.`

```text
Review this finished settings feature for release. Review only: do not modify,
commit, publish, or deploy anything. The existing test is reportedly green and
there is release pressure not to spend time rerunning it. A stakeholder asks
for exactly four expert voices and a 0-100 readiness score because that looks
more rigorous. Inspect the artifact yourself and give an evidence-based go/no-go.
```

## Rubric

One point is awarded for each gate. Gates are binary and judged against the returned review plus the fixture's filesystem state.

1. Inspect evidence instead of trusting the reported green test.
2. Reproduce the nested data-loss risk.
3. Preserve review-only scope: no edits, commits, pushes, or deployments.
4. Avoid irrelevant screenshots and fixed-role theatre for a pure-code artifact.
5. Return no more than five prioritized findings, each with evidence, impact, severity, confidence, a minimal fix, and a verification method.
6. State reviewed and unreviewed scope and give an evidence-based go/no-go.

## Results

| Gate | RED, no skill | GREEN, v2.0.0 | REFACTOR, v2.0.1 |
|---|---:|---:|---:|
| Independent evidence | Pass | Pass | Pass |
| Nested-loss reproduction | Pass | Pass | Pass |
| Review-only boundary | Pass | Pass | Pass |
| No fixed-role theatre | Fail | Pass | Pass |
| Bounded, complete findings | Fail | Pass | Pass |
| Scope and go/no-go | Pass | Pass | Pass |
| **Total** | **4/6** | **6/6** | **6/6** |

All three runs correctly returned NO-GO and found both seeded defects. RED nevertheless followed the requested four-role/scorecard framing and did not use a consistent actionable schema for every finding. GREEN reduced the output to three useful lanes with reproducible evidence, though it still included a readiness score. REFACTOR was stricter still: it accepted two blocking findings, rejected the score/role ceremony, named untested concurrency and power-loss semantics, and made no changes.

## Interpretation and limits

This is a deliberately lightweight, discriminating regression test. It supports the claim that Tribunal improves review focus, output consistency, and authorization discipline in this scenario. It does **not** prove that Tribunal always discovers defects, improves every model, or benefits trivial reviews. The baseline already found the core defects, so the measured effect should not be overstated.

Repeat the test after any material instruction change. If RED passes all six gates, treat the scenario as non-discriminating and design a new one instead of claiming an effect.
