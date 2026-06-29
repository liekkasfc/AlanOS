# RFC-0005: Daily Output

## Status
Draft

## Date
2026-06-29

## Summary
This RFC defines the expected daily output of Alan OS.

Alan OS is a personal revenue operating system, not a news aggregator. The most important output is Today's Bet: one concrete validation action that helps Alan move from an information gap to a validated revenue signal.

The daily output should make Alan faster, not more informed in a passive way. If the output does not help Alan act today, it is probably too broad.

## Daily Output Principle
The daily output exists to answer one question:

What should Alan do today to reduce the most valuable uncertainty?

Everything else in the output is supporting evidence for that decision.

## Required Output Order
The output should appear in this order:

1. Today's Bet
2. Why this bet
3. Validation plan
4. Evidence and doubts
5. Recording prompts

Today's Bet comes first because Alan OS should create action pressure before research appetite.

## Section: Today's Bet

### Purpose
Today's Bet is the single validation action Alan should execute today.

### Required Content
- `opportunity_id`
- `date`
- `action`
- `target_personas`
- `timebox_minutes`
- `expected_signal`
- `give_up_rule`
- `success_criteria`

### Quality Bar
A good Today's Bet:

- can be completed today,
- names a reachable customer or buyer,
- can produce a revenue or rejection signal,
- does not require product development,
- is small enough to start within 60 minutes,
- records what Alan should learn even if nobody responds.

### Bad Today's Bet Examples
- Research ten AI trends.
- Build a prototype before speaking to buyers.
- Read more about the market.
- Collect a list of interesting links.
- Explore Product Hunt for inspiration.

## Section: Why This Bet

### Purpose
This section explains why the bet is worth Alan's limited execution energy.

### Required Content
- linked InformationGap,
- linked Opportunity,
- customer segment,
- buyer or decision maker,
- pain,
- revenue hypothesis,
- why now,
- riskiest assumption.

### Quality Bar
The explanation should make the money hypothesis visible. It should not merely say that a topic is trending.

## Section: Validation Plan

### Purpose
The ValidationPlan turns Today's Bet into an executable sequence.

### Required Content
- target count,
- channels or surfaces,
- action steps,
- short script or offer language,
- timebox,
- success threshold,
- give-up rule.

### Quality Bar
The plan should be service-first and sell-before-build whenever possible. It should prefer outreach, conversations, offers, interviews, pilots, and pre-sales over product work.

## Section: Evidence and Doubts

### Purpose
This section keeps Alan honest about uncertainty.

### Required Content
- strongest supporting Signals,
- contradicting Signals or missing facts,
- lifecycle stage,
- crowding risk,
- confidence level,
- what would change the decision.

### Quality Bar
Evidence should support action. Doubts should sharpen the validation plan, not reopen endless browsing.

## Section: Recording Prompts

### Purpose
Recording prompts make sure execution becomes learning.

### Required Content
- what action was taken,
- who was contacted,
- what response or silence occurred,
- whether any RevenueSignal appeared,
- whether any RejectionSignal appeared,
- what lesson updates AlanMemory,
- what next action is implied.

### Quality Bar
The prompts should make rejection easy to record without emotional distortion.

## Output Non-Goals
The daily output is not:

- a news digest,
- a list of links,
- a trend report,
- a dashboard of everything changing,
- a project roadmap,
- a prompt to build software,
- a replacement for talking to customers.

## Acceptance Criteria
The daily output is successful when:

- exactly one Today's Bet is selected,
- the first screen tells Alan what to do,
- the action can produce a revenue or rejection signal,
- the plan can run before product development,
- evidence supports the action without becoming a research rabbit hole,
- the result can update AlanMemory the same day.
