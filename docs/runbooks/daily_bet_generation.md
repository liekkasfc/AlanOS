# Daily Bet 生成 Runbook

## 目的
这个 runbook 说明如何从已准备好的本地 JSON records 生成一个以 Today's Bet（今日唯一验证动作）为中心的每日行动包。

生成器只用于减少 Alan 已经手动准备 records 之后的排版摩擦。它不收集数据、不浏览网页、不调用外部 API、不使用数据库、不创建 UI，也不会从新闻看板里替 Alan 做选择。

## 输入
使用 `data/sample/` 或 `data/daily/YYYY-MM-DD/` 中已准备好的 JSON records，record shapes 保持一致：

- Signal（信号 / 原始线索）
- InformationGap（信息差）
- Opportunity（可变现机会）
- Today's Bet（今日唯一验证动作）
- ValidationPlan（验证计划）
- ValidationRecord（验证记录）
- RevenueSignal（收入信号）
- RejectionSignal（拒绝信号）
- AlanMemory（Alan 机会记忆）
- Alan Context

Alan Context 会优先读取 records directory 中精确命名的 `alan_context.json`。如果不存在，renderer 会回退到 `memory/alan_context.json`。如果两个都不存在，输出会显示 `No Alan Context recorded.`

生成器要求选定日期只有一个 active daily bet。在本地 workspace 中，`planned` 和 `active` 状态的 Today's Bet 都算作仍可行动的候选。

## 输出结构
Markdown 输出遵循 `templates/daily_output_template.md` 和 RFC-0005：

1. 今日唯一验证动作
2. 为什么选它
3. 执行计划
4. 证据与疑点
5. 回填记录提示

Today's Bet 必须只出现一次。如果 Alan 在同一天有多个候选，停止并手动做选择。

## 命令
生成 sample daily packet：

```bash
python3 scripts/generate_daily_output.py --sample-dir data/sample --date 2026-06-29
```

从真实本地 workspace 生成 daily packet：

```bash
python3 scripts/generate_daily_output.py --records-dir data/daily/2026-06-29 --date 2026-06-29
```

命令会把 Markdown 打印到 stdout，默认不写文件。

## 手动检查步骤
1. 确认 prepared records 来自手动 review，而不是 automated collection。
2. 确认选定日期只有一个 `planned` 或 `active` Today's Bet。
3. 确认 bet 指向可触达 buyers 或 referrers。
4. 确认 ValidationPlan 能在产品开发前执行。
5. 确认 expected signal 比 attention 更接近 revenue。
6. 确认 give-up rule 和 recording prompts 存在。
7. 执行动作，再继续研究。

## 失败情况
生成器应该在以下情况清晰失败：

- 选定日期没有 active Today's Bet；
- 选定日期有多个 active Today's Bet；
- required linked records 缺失；
- prepared JSON 无效。

通过手动编辑本地 records 解决失败。不要添加 collectors 或 automated browsing 来补上下文。

## 不要做什么
- 不要构建 collectors。
- 不要调用 external APIs。
- 不要自动浏览。
- 不要使用 database。
- 不要创建 UI。
- 不要渲染多个 Today's Bets。
- 不要把它变成趋势或新闻看板。
- 不要因为 Markdown 看起来完整，就跳过 manual validation。
