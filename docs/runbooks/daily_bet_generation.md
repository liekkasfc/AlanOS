# Daily Bet Generation Runbook

## Purpose
This runbook explains how to generate one daily action packet centered on Today's Bet from prepared local JSON records.

The generator exists only to reduce formatting friction after Alan has already prepared the records manually. It does not collect data, browse the web, call external APIs, use a database, create a UI, or choose from a news dashboard.

## Inputs
Use prepared JSON records in `data/sample/` or another local directory with the same record shapes:

- Signal
- InformationGap
- Opportunity
- Today's Bet
- ValidationPlan
- ValidationRecord
- RevenueSignal
- RejectionSignal
- AlanMemory
- Alan Context

The generator expects exactly one active daily bet for the selected date. In Sprint 2, `planned` and `active` Today's Bet records count as active candidates because they are still open for action.

## Output Shape
The Markdown output follows `templates/daily_output_template.md` and RFC-0005:

1. Today's Bet
2. Why this bet
3. Validation Plan
4. Evidence and Doubts
5. Recording Prompts

Today's Bet must appear once. If Alan has more than one candidate for the date, stop and resolve the decision manually.

## Command
Generate the sample daily packet:

```bash
rtk python3 scripts/generate_daily_output.py --sample-dir data/sample --date 2026-06-29
```

The command prints Markdown to stdout. It does not write files by default.

## Manual Review Steps
1. Confirm the prepared records came from manual review, not automated collection.
2. Confirm the selected date has exactly one `planned` or `active` Today's Bet.
3. Confirm the bet names reachable buyers or referrers.
4. Confirm the ValidationPlan can be executed before product development.
5. Confirm expected signal is closer to revenue than attention.
6. Confirm give-up rule and recording prompts are present.
7. Execute the action before doing more research.

## Failure Cases
The generator should fail clearly when:

- no active Today's Bet exists for the date,
- more than one active Today's Bet exists for the date,
- required linked records are missing,
- prepared JSON is invalid.

Resolve failures by editing the prepared local records manually. Do not add collectors or automated browsing to fill missing context.

## What Not To Do
- Do not build collectors.
- Do not call external APIs.
- Do not browse automatically.
- Do not use a database.
- Do not create a UI.
- Do not render multiple Today's Bets.
- Do not convert this into a trend or news dashboard.
- Do not skip manual validation because the Markdown looks polished.
