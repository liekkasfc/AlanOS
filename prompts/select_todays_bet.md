# 选择 Today's Bet

当 Alan 已经有一个 Opportunity 后，使用这个 prompt。

## Prompt
你正在帮助 Alan OS 选择 Today's Bet（今日唯一验证动作）。

Today's Bet 是最重要的每日输出。它是 Alan 今天可以执行的一个动作，用来产生 RevenueSignal（收入信号）或 RejectionSignal（拒绝信号）。

Opportunity：

```text
[PASTE OPPORTUNITY RECORD]
```

Available Alan Context：

```text
[PASTE AVAILABLE TIME, REACHABLE PEOPLE, CHANNELS, AND CONSTRAINTS]
```

返回一个 Today's Bet，必须包含这些 English keys：

- `opportunity_id`
- `date`
- `action`
- `target_personas`
- `timebox_minutes`
- `expected_signal`
- `give_up_rule`
- `success_criteria`
- `script_id`
- `notes`
- `confidence`
- `status`

约束：

- 只选择一个 bet。
- action 必须能在 60 分钟内开始或完成。
- action 必须接触或观察真实 buyers 或 referrers。
- action 不能要求 product development。
- expected signal 必须比 attention 更接近 revenue。
- 写清楚 rejection 或 silence 会教 Alan 什么。

最后用一句话结束：`Do this before any further research: ...`
