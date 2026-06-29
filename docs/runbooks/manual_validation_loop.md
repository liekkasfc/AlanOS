# Manual Validation Loop Runbook

## Purpose
This runbook explains how Alan manually runs one 60-minute Alan OS validation loop:

Signal -> InformationGap -> Opportunity -> Today's Bet -> ValidationPlan -> ValidationRecord -> RevenueSignal/RejectionSignal -> AlanMemory.

The point is not to collect more information. The point is to move from an information gap to a validated revenue signal faster.

## Timebox
Default timebox: 60 minutes.

- 5 minutes: select Signals.
- 5 minutes: extract one InformationGap.
- 5 minutes: create one Opportunity.
- 10 minutes: choose Today's Bet and write the ValidationPlan.
- 30 minutes: execute the action.
- 5 minutes: record results and update AlanMemory.

If execution needs the full 60 minutes, record the setup work and schedule the next action. Do not convert the loop into open-ended research.

## Preparation Checklist
Before starting, Alan should have:

- one quiet 60-minute block,
- `configs/source_registry.yaml` open,
- `data/sample/` open as examples,
- the five Sprint 1 prompts available,
- a place to save manual JSON records,
- one reachable buyer path or audience surface,
- a clear rule that no product development happens during the loop.

## Step 1: Select Signals
Choose one to three manual Signals from the source registry.

Good Signals have:

- a named pain or workflow,
- a reachable customer segment,
- a timing clue,
- a possible paid action,
- enough specificity to message a real person.

Avoid Signals that are only:

- interesting links,
- broad trend claims,
- popularity metrics,
- tool launches without buyer pain,
- topics Alan cannot act on today.

Output: one `signal` record for each useful observation.

## Step 2: Extract an InformationGap
Ask what temporary mismatch the Signals reveal.

Use these questions:

- Who knows or feels the issue early?
- Who needs the gap closed?
- Why does the timing matter now?
- What will make the window close?
- What would prove this is not a real gap?

The InformationGap should not be a product idea. It should explain a temporary asymmetric advantage.

Output: one `information_gap` record.

## Step 3: Create One Opportunity
Turn the InformationGap into a monetizable interpretation for a reachable customer.

Define:

- customer segment,
- buyer,
- pain,
- manual offer,
- revenue hypothesis,
- distribution path,
- lifecycle stage,
- riskiest assumption.

Prefer a service, audit, teardown, consultation, review, script cleanup, buyer-language rewrite, or other manual offer before software.

Output: one `opportunity` record.

## Step 4: Choose Today's Bet
Today's Bet is the one action Alan will do now.

The bet must:

- fit today,
- name reachable people,
- be small enough to start immediately,
- produce a RevenueSignal or RejectionSignal,
- include a give-up rule,
- avoid building software.

If there are multiple possible bets, choose the one with the shortest path to a real buyer response.

Output: one `todays_bet` record.

## Step 5: Execute the ValidationPlan
Convert Today's Bet into a concrete plan.

Include:

- target count,
- channels,
- action steps,
- message or offer script,
- timebox,
- success threshold,
- give-up rule,
- risk notes.

Then execute the action. Send the messages, publish the offer, ask the buyer, request the call, or offer the paid manual service.

Do not polish. Do not build. Do not continue researching once the action is clear.

Output: one `validation_plan` record before execution.

## Step 6: Record Validation
Immediately after execution, record what happened.

Capture:

- actions taken,
- people contacted,
- responses,
- silence,
- objections,
- outcome,
- lesson,
- next action,
- time spent.

Silence is data. Rejection is data. A confused reply is data.

Output: one `validation_record` record.

## Step 7: Record RevenueSignals and RejectionSignals
Create RevenueSignals for evidence that a real person may pay, has paid, or moved closer to payment.

Examples:

- booked call,
- budget-confirming reply,
- paid pilot,
- deposit,
- referral to a buyer,
- direct request for a paid service.

Create RejectionSignals for evidence that the offer, segment, timing, price, buyer, or pain is wrong.

Examples:

- no response,
- not urgent,
- no budget,
- wrong buyer,
- already solved,
- price objection,
- timing objection,
- scope mismatch.

Output: one or more `revenue_signal` and `rejection_signal` records.

## Step 8: Update AlanMemory
Write down what should change next time.

Update:

- validated patterns,
- rejected patterns,
- strong segments,
- weak segments,
- MoneyDNA notes,
- weekly revenue signals,
- next biases.

The memory update should change future selection. If it does not change a future bet, it is probably too vague.

Output: one `alan_memory` update for the current week or review period.

## What Not To Do
- Do not build collectors.
- Do not build analyzers.
- Do not build automation.
- Do not create a database.
- Do not create a UI.
- Do not add external integrations.
- Do not turn the loop into a SaaS workflow.
- Do not chase a news digest.
- Do not select multiple Today's Bets.
- Do not build product artifacts before buyer validation.
- Do not ignore rejection or silence.

## Done Criteria
One manual loop is complete when Alan has:

- at least one Signal,
- one InformationGap,
- one Opportunity,
- one Today's Bet,
- one ValidationPlan,
- one ValidationRecord,
- at least one RevenueSignal or RejectionSignal,
- one AlanMemory update,
- one specific next bias for future selection.
