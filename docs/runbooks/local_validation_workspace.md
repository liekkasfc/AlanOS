# Local Validation Workspace Runbook

## Purpose
This runbook explains how Alan runs a real daily manual validation workflow using local files.

The workspace exists to support the revenue validation loop:

Signal -> InformationGap -> Opportunity -> Today's Bet -> ValidationPlan -> ValidationRecord -> RevenueSignal/RejectionSignal -> AlanMemory.

It does not collect data, browse the web, call external APIs, use a database, create a UI, or introduce SaaS assumptions.

## Daily Folder
Create one folder per day:

```text
data/daily/YYYY-MM-DD/
```

Each folder contains local manual records:

- `signal.json`
- `information_gap.json`
- `opportunity.json`
- `todays_bet.json`
- `validation_plan.json`
- `validation_record.json`
- `revenue_signal.json`
- `rejection_signal.json`
- `alan_memory.json`

## Step 1: Create a Date Folder
Create blank manual templates:

```bash
python3 scripts/init_daily_workspace.py --date 2026-06-29
```

Or create the folder from sample records as examples:

```bash
python3 scripts/init_daily_workspace.py --date 2026-06-29 --from-sample
```

The `--from-sample` option is for learning the shape only. It does not collect anything.

## Step 2: Prepare Local JSON Records Manually
Edit the files inside `data/daily/YYYY-MM-DD/`.

Start with:

1. `signal.json`
2. `information_gap.json`
3. `opportunity.json`
4. `todays_bet.json`
5. `validation_plan.json`

Keep the records small. Alan should write only enough to choose one executable Today's Bet.

## Step 3: Validate Records
Run local schema validation:

```bash
python3 scripts/validate_records.py --records-dir data/daily/2026-06-29
```

Validation checks local JSON files against local `schemas/*.schema.json` files. It does not use a database or external API.

If validation fails, fix the reported file and field before rendering the daily output.

## Step 4: Generate Daily Output
Render one daily action packet:

```bash
python3 scripts/generate_daily_output.py --records-dir data/daily/2026-06-29 --date 2026-06-29
```

The renderer prints Markdown to stdout. It fails if more than one `planned` or `active` Today's Bet exists for the same date.

## Step 5: Execute Today's Bet
Do the action in the real world:

- send the messages,
- make the offer,
- ask the buyer,
- request the call,
- test the paid manual service.

Do not keep researching once the action is clear.

## Step 6: Record Validation Result
After execution, update:

- `validation_record.json`
- `revenue_signal.json` when a buyer moves closer to payment
- `rejection_signal.json` when silence, objection, timing, budget, or wrong-buyer evidence appears

Silence is data. Rejection is data. Record it before changing the idea.

## Step 7: Update AlanMemory
Update `alan_memory.json` with:

- validated patterns,
- rejected patterns,
- strong segments,
- weak segments,
- MoneyDNA updates,
- weekly revenue signals,
- next biases.

The memory update should change the next Today's Bet.

## Make Commands
The Makefile wraps the same local commands:

```bash
make init-day DATE=2026-06-29
make validate-day DATE=2026-06-29
make render-day DATE=2026-06-29
make sample-output
make test
```

## What Not To Do
- Do not build collectors.
- Do not browse the web automatically.
- Do not call external APIs.
- Do not use a database.
- Do not build a UI.
- Do not create SaaS assumptions.
- Do not generate multiple Today's Bets.
- Do not turn Alan OS into a news dashboard.
