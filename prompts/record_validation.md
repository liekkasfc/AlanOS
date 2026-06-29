# Record Validation

Use this prompt immediately after Alan executes a ValidationPlan.

## Prompt
You are helping Alan OS record what happened without narrative distortion.

ValidationPlan:

```text
[PASTE VALIDATION PLAN RECORD]
```

Raw execution notes:

```text
[PASTE ACTIONS TAKEN, PEOPLE CONTACTED, RESPONSES, SILENCE, OBJECTIONS, CALLS, PAYMENT SIGNALS]
```

Return:

1. One ValidationRecord.
2. Any RevenueSignals.
3. Any RejectionSignals.

For the ValidationRecord include:

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

For each RevenueSignal include:

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

For each RejectionSignal include:

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

Constraints:

- Record silence as evidence when relevant.
- Do not inflate weak replies into strong revenue signals.
- Separate facts from interpretation.
- Capture at least one lesson before moving to another idea.

End with one sentence: `The next action should be: ...`
