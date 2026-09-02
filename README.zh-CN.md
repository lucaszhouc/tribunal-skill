# Tribunal Skill

> [English](README.md) · **中文**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Codex Skill](https://img.shields.io/badge/Codex-skill-111827)](SKILL.md)
[![Claude Code Compatible](https://img.shields.io/badge/Claude_Code-compatible-D97757)](SKILL.md)
[![Behavior Tested](https://img.shields.io/badge/behavior-tested-16A34A)](tests/EFFECT_TEST.md)

一个面向已成形产品、UI 改动和代码改动的证据驱动审查 Skill。Tribunal 只选择确实能增加独立信息的审查视角，先复现再接受发现，并严格区分“审查范围”和“修改、部署或发布授权”。

Tribunal 是原创 Skill，不是其他项目的 fork。

## 为什么需要 Tribunal

多代理审查很容易变成角色扮演：固定人数、重复截图、冗长评分，以及大量未经复现的观点。Tribunal 约束四件真正有价值的事：

- **发现必须有证据**：检查或复现真实产物。
- **视角按任务选择**：只在相关时使用产品、界面或工程审查线。
- **输出有预算**：优先少量、真正影响结果的问题。
- **授权不扩张**：只说审查，不会自动变成修改、部署或对外提交。

## 适用场景

- 已有可运行产物或可检查 diff 的主要功能、大改和重构。
- 发布候选、里程碑或高风险关键路径。
- 需要把真实用户、界面体验与可靠性放在同一组证据上裁决的产品审查。

不适用于一行文案、尚无产物的方向发散，或可以直接完成的窄范围检查。

## 安装

把仓库克隆到当前 Agent 能识别的 Skill 根目录。

### Codex

```powershell
git clone https://github.com/lucaszhouc/tribunal-skill.git "$HOME\.agents\skills\tribunal"
```

如果当前 Codex 使用 `$CODEX_HOME/skills`，则放到 `$CODEX_HOME/skills/tribunal`。

### Claude Code

```powershell
git clone https://github.com/lucaszhouc/tribunal-skill.git "$HOME\.claude\skills\tribunal"
```

安装后重新打开 Agent 会话，让 Skill catalog 重新加载。

## 使用

显式调用深审但不授权修改：

```text
用 $tribunal 审查这个发布候选，只审查，不修改也不部署。
```

需要审查并修复时，明确写出授权：

```text
用 $tribunal 审查这个功能，修复已接受且在范围内的问题，并重新验证。
```

Tribunal 可以使用运行时已有的协作代理，但不强制凑人数。主 Agent 始终负责共同物证、去重、裁决和最终验证。

## 行为效果测试

轻量 RED/GREEN 测试使用一个现有测试全绿、但仍存在嵌套配置丢失和非原子写入的设置功能。

| 轮次 | 是否加载 Tribunal | 通过门槛 |
|---|---:|---:|
| RED 基线 | 否 | 4/6 |
| GREEN | 是 | 6/6 |
| REFACTOR 复验 | 是 | 6/6 |

测试覆盖取证、发现预埋的数据丢失风险、review-only 边界、避免固定角色仪式、发现质量，以及基于证据的发布裁决。完整设计见 [tests/EFFECT_TEST.md](tests/EFFECT_TEST.md)。

RED 基线本身也找到了两处预埋缺陷，因此这个测试不夸大为“让模型从完全看不见问题变成看见问题”。实测提升更窄也更可信：GREEN 没有照搬四人面板，而是收敛为三条相关审查线和更一致的裁决记录，不过仍保留了就绪度评分；v2.0.1 的 REFACTOR 轮进一步拒绝了这项无关评分。

## 维护与联系

这是单人维护项目，GitHub 通知可能回复较慢；最快联系方式是 [lucaszhouc@gmail.com](mailto:lucaszhouc@gmail.com)。

安全问题请按 [SECURITY.md](SECURITY.md) 私下报告；参与方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

[MIT](LICENSE)
