# 记录 Validation

Alan 执行完 ValidationPlan 后，立刻使用这个 prompt。

## Prompt
你正在帮助 Alan OS 如实记录执行结果，避免叙事扭曲。

ValidationPlan：

```text
[PASTE VALIDATION PLAN RECORD]
```

Raw execution notes：

```text
[PASTE ACTIONS TAKEN, PEOPLE CONTACTED, RESPONSES, SILENCE, OBJECTIONS, CALLS, PAYMENT SIGNALS]
```

返回：

1. 一个 ValidationRecord。
2. 任意 RevenueSignals。
3. 任意 RejectionSignals。

ValidationRecord 必须包含这些 English keys：

- `validation_plan_id`
- `executed_at`
- `actions_taken`
- `people_contacted`
- `responses`
- `outcome`
- `revenue_signal_ids`
- `rejection_signal_ids`
- `lesson`
- `next_action`
- `time_spent_minutes`
- `confidence`
- `status`

每个 RevenueSignal 必须包含：

- `validation_record_id`
- `signal_type`
- `strength`
- `evidence`
- `amount`
- `currency`
- `buyer`
- `next_step`
- `confidence`
- `status`

每个 RejectionSignal 必须包含：

- `validation_record_id`
- `rejection_type`
- `stated_reason`
- `implicit_reason`
- `segment`
- `objection`
- `lesson`
- `follow_up_date`
- `confidence`
- `status`

约束：

- 相关时，把 silence 记录为 evidence。
- 不要把 weak replies 夸大成 strong revenue signals。
- 区分事实和解释。
- 转向另一个 idea 前，至少捕捉一个 lesson。

最后用一句话结束：`The next action should be: ...`
