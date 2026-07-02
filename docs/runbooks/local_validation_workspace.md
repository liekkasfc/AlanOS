# 本地验证 Workspace Runbook

## 目的
这个 runbook 说明 Alan 如何用本地文件跑真实的每日手动验证工作流。

workspace 支持 revenue validation loop：

Signal（信号 / 原始线索） -> InformationGap（信息差） -> Opportunity（可变现机会） -> Today's Bet（今日唯一验证动作） -> ValidationPlan（验证计划） -> ValidationRecord（验证记录） -> RevenueSignal（收入信号）/RejectionSignal（拒绝信号） -> AlanMemory（Alan 机会记忆）。

它不收集数据、不浏览网页、不调用外部 API、不使用数据库、不创建 UI，也不引入 SaaS assumptions。

## Daily Folder
每天创建一个文件夹：

```text
data/daily/YYYY-MM-DD/
```

每个文件夹包含本地手动 records：

- `signal.json`
- `information_gap.json`
- `opportunity.json`
- `todays_bet.json`
- `validation_plan.json`
- `validation_record.json`
- `revenue_signal.json`
- `rejection_signal.json`
- `alan_memory.json`

`revenue_signal.json` 和 `rejection_signal.json` 是 post-execution records。initializer 为了兼容性会保留 placeholder files，但它们在真实执行产生证据前是可选的。

## Alan Context
Alan 的长期个人上下文位于：

```text
memory/alan_context.json
```

用它保存稳定约束，例如每日执行时间有限、现金流压力、偏好手动验证、buyer signal 前避免 heavy build，以及 Alan 最强的适配方向。

如果 daily folder 中存在 `alan_context.json`，daily renderer 会优先使用这个文件。否则回退到 `memory/alan_context.json`。如果两个都不存在，输出会显示 `No Alan Context recorded.`

## Step 1: 创建日期文件夹
创建空白手动 templates：

```bash
python3 scripts/init_daily_workspace.py --date 2026-06-29
```

或从 sample records 创建示例文件夹：

```bash
python3 scripts/init_daily_workspace.py --date 2026-06-29 --from-sample
```

`--from-sample` 只用于学习 record shape。它不会收集任何东西。

## Step 2: 手动准备本地 JSON Records
编辑 `data/daily/YYYY-MM-DD/` 中的文件。

先从这些文件开始：

1. `signal.json`
2. `information_gap.json`
3. `opportunity.json`
4. `todays_bet.json`
5. `validation_plan.json`

保持 records 简短。Alan 只需要写到足以选择一个可执行 Today's Bet。

## Step 3: 验证 Records
运行本地结构验证：

```bash
python3 scripts/validate_records.py --records-dir data/daily/2026-06-29
```

Structural validation 会用本地 `schemas/*.schema.json` 检查 required fields、简单类型、enums 和日期格式。它不使用 database 或 external API。

如果验证失败，先修复报错中的 file 和 field，再渲染 daily output。

然后运行关系验证：

```bash
python3 scripts/validate_records.py --records-dir data/daily/2026-06-29 --links
```

Relationship validation 检查本地 record IDs 是否连对：Signals 到 InformationGaps，InformationGaps 到 Opportunities，Opportunities 到 Today's Bet，Today's Bet 到 ValidationPlan，post-execution records 回连 ValidationRecord。

行动前运行 execution-readiness validation：

```bash
python3 scripts/validate_records.py --records-dir data/daily/2026-06-29 --ready
```

Readiness validation 只检查 pre-execution records：`signal.json`、`information_gap.json`、`opportunity.json`、`todays_bet.json`、`validation_plan.json`。它会在 TODO placeholders 或执行关键字段缺失时失败：Today's Bet action、target personas、expected signal、give-up rule、ValidationPlan target count、script 和 action steps。它会忽略 `validation_record.json`、`revenue_signal.json`、`rejection_signal.json` 和 `alan_memory.json` 中的 post-execution placeholders。

## Step 4: 生成 Daily Output
渲染一个 daily action packet：

```bash
python3 scripts/generate_daily_output.py --records-dir data/daily/2026-06-29 --date 2026-06-29
```

renderer 会把 Markdown 打印到 stdout。如果同一天存在多个 `planned` 或 `active` Today's Bet，它会失败。

## Step 5: 执行 Today's Bet
在真实世界执行动作：

- 发消息；
- 提出 offer；
- 询问买家；
- 请求 call；
- 测试付费手动服务。

动作清楚后，不要继续研究。

## Step 6: 记录 Validation Result
执行后更新：

- `validation_record.json`
- 有买家更接近付款时，更新 `revenue_signal.json`
- 出现沉默、异议、时机、预算或 wrong-buyer 证据时，更新 `rejection_signal.json`

沉默是数据。拒绝是数据。改变 idea 前先记录。

然后验证已记录的结果：

```bash
python3 scripts/validate_records.py --records-dir data/daily/2026-06-29 --result
```

Result validation 只检查 post-execution records：`validation_record.json`、`revenue_signal.json`、`rejection_signal.json`、`alan_memory.json`。如果 execution record 仍有 TODO、没有 actions taken、没有 outcome、没有 lesson、没有 time spent、没有 RevenueSignal 或 RejectionSignal reference，或 AlanMemory 没有 next bias，它会失败。

## Step 7: 更新 AlanMemory
更新 `alan_memory.json`：

- validated patterns；
- rejected patterns；
- strong segments；
- weak segments；
- MoneyDNA updates；
- weekly revenue signals；
- next biases。

Memory update 应该改变下一次 Today's Bet。

## Make Commands
Makefile 包装了同样的本地命令：

```bash
make init-day DATE=2026-06-29
make validate-day DATE=2026-06-29
make validate-links DATE=2026-06-29
make validate-ready DATE=2026-06-29
make validate-result DATE=2026-06-29
make render-day DATE=2026-06-29
make sample-output
make test
```

`make validate-day` 是结构验证。`make validate-links` 是关系验证。`make validate-ready` 是行动前执行准备验证。`make validate-result` 是行动后结果记录验证。

行动前运行 `validate-day`、`validate-links`、`validate-ready`。行动后更新结果文件并运行 `validate-result`。

## 不要做什么
- 不要构建 collectors。
- 不要自动浏览网页。
- 不要调用 external APIs。
- 不要使用 database。
- 不要构建 UI。
- 不要创建 SaaS assumptions。
- 不要生成多个 Today's Bets。
- 不要把 Alan OS 变成新闻看板。
