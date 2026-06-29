# RFC-0004: Schema

## Status
Draft

## Date
2026-06-29

## Summary
This RFC defines the initial schema contract for Alan OS records. It is documentation only for Sprint 0. No implementation code is introduced here.

Alan OS is a personal revenue operating system. These schemas exist to help Alan move from an information gap to one validated revenue signal faster. They are not collector specifications and should not create pressure to build automation before the manual loop proves useful.

All records share a common metadata shape so they can later be stored as JSON files, SQLite rows, Obsidian notes, Feishu Bitable records, or another operational surface.

## Common Fields
Every schema must include:

- `id`: stable unique identifier.
- `created_at`: ISO 8601 creation timestamp.
- `updated_at`: ISO 8601 update timestamp.
- `source`: origin of the record or derivation.
- `confidence`: number from 0 to 1.
- `status`: lifecycle state such as `draft`, `active`, `validated`, `rejected`, `archived`.

The shared metadata contract is extracted to [`common_fields.schema.json`](../../schemas/common_fields.schema.json).

## Schema Files
The JSON Schemas from this RFC are extracted into `schemas/`. The schema files are the source of truth for field contracts.

| Entity | Schema File | Purpose |
| --- | --- | --- |
| Common Fields | [`common_fields.schema.json`](../../schemas/common_fields.schema.json) | Shared metadata contract used by every record. |
| Signal | [`signal.schema.json`](../../schemas/signal.schema.json) | Raw or normalized outside-world observation. |
| InformationGap | [`information_gap.schema.json`](../../schemas/information_gap.schema.json) | Temporary asymmetric advantage extracted from Signals. |
| Opportunity | [`opportunity.schema.json`](../../schemas/opportunity.schema.json) | Monetizable interpretation of an InformationGap. |
| Today's Bet | [`todays_bet.schema.json`](../../schemas/todays_bet.schema.json) | The one validation action Alan should execute today. |
| ValidationPlan | [`validation_plan.schema.json`](../../schemas/validation_plan.schema.json) | Concrete plan for testing a Today's Bet before building. |
| ValidationRecord | [`validation_record.schema.json`](../../schemas/validation_record.schema.json) | What happened when Alan executed a ValidationPlan. |
| RevenueSignal | [`revenue_signal.schema.json`](../../schemas/revenue_signal.schema.json) | Evidence that a real person may pay, has paid, or is moving toward payment. |
| RejectionSignal | [`rejection_signal.schema.json`](../../schemas/rejection_signal.schema.json) | Structured evidence from silence, objection, delay, or rejection. |
| OpportunityGenome | [`opportunity_genome.schema.json`](../../schemas/opportunity_genome.schema.json) | Why an Opportunity can make money. |
| MoneyDNA | [`money_dna.schema.json`](../../schemas/money_dna.schema.json) | Why an Opportunity fits or does not fit Alan. |
| AlanMemory | [`alan_memory.schema.json`](../../schemas/alan_memory.schema.json) | Accumulated patterns from bets, outcomes, lessons, and fit updates. |

## Contract Priorities
The schema set should preserve the Alan OS operating bias:

1. Today's Bet is the most important daily output.
2. RevenueSignals and RejectionSignals matter more than attention metrics.
3. Every Opportunity must name a reachable customer segment and buyer.
4. Every ValidationPlan must be executable before product development.
5. AlanMemory must improve from both wins and losses.

## Storage Mapping

### JSON Files
JSON files are the portable source of truth for early development and manual review.

| Schema | Suggested Path |
| --- | --- |
| `signal.schema.json` | `data/signals/{id}.json` |
| `information_gap.schema.json` | `data/information_gaps/{id}.json` |
| `opportunity.schema.json` | `data/opportunities/{id}.json` |
| `todays_bet.schema.json` | `data/todays_bets/{date}-{id}.json` |
| `validation_plan.schema.json` | `data/validation_plans/{id}.json` |
| `validation_record.schema.json` | `data/validation_records/{id}.json` |
| `revenue_signal.schema.json` | `data/revenue_signals/{id}.json` |
| `rejection_signal.schema.json` | `data/rejection_signals/{id}.json` |
| `opportunity_genome.schema.json` | `data/opportunity_genomes/{id}.json` |
| `money_dna.schema.json` | `data/money_dna/{id}.json` |
| `alan_memory.schema.json` | `data/alan_memory/{period}.json` |

### SQLite Tables
SQLite is appropriate once the manual loop needs filtering, joins, and history queries.

| Schema | Table | Primary Relationships |
| --- | --- | --- |
| `signal.schema.json` | `signals` | feeds `information_gap_signals` |
| `information_gap.schema.json` | `information_gaps` | has many `opportunities` |
| `opportunity.schema.json` | `opportunities` | belongs to `information_gaps` |
| `todays_bet.schema.json` | `todays_bets` | belongs to `opportunities` |
| `validation_plan.schema.json` | `validation_plans` | belongs to `todays_bets` |
| `validation_record.schema.json` | `validation_records` | belongs to `validation_plans` |
| `revenue_signal.schema.json` | `revenue_signals` | belongs to `validation_records` |
| `rejection_signal.schema.json` | `rejection_signals` | belongs to `validation_records` |
| `opportunity_genome.schema.json` | `opportunity_genomes` | belongs to `opportunities` |
| `money_dna.schema.json` | `money_dna` | belongs to `opportunities` |
| `alan_memory.schema.json` | `alan_memory` | aggregates validation outcomes |

### Obsidian Frontmatter
Obsidian notes are useful for human review and weekly synthesis.

```yaml
id: opp_001
type: opportunity
created_at: 2026-06-29T00:00:00Z
updated_at: 2026-06-29T00:00:00Z
source: gap_001
confidence: 0.64
status: active
customer_segment: Small B2B AI vendors selling to enterprise
buyer: Founder or head of sales
lifecycle_stage: Early
```

Recommended note layout:

- frontmatter for structured fields,
- body for reasoning, examples, scripts, and lessons,
- backlinks between Signals, InformationGaps, Opportunities, Bets, and Records.

### Feishu Bitable Fields
Feishu Bitable is useful for operational tracking and daily execution.

| Entity | Core Fields |
| --- | --- |
| Signal | ID, Created At, Source, Title, Summary, Tags, Confidence, Status |
| InformationGap | ID, Name, Evidence Signals, Who Has Gap, Who Needs Gap Closed, Why Now, Confidence, Status |
| Opportunity | ID, Gap, Customer Segment, Buyer, Pain, Offer, Revenue Hypothesis, Lifecycle Stage, Confidence, Status |
| Today's Bet | ID, Date, Opportunity, Action, Timebox, Expected Signal, Give-Up Rule, Status |
| ValidationPlan | ID, Bet, Hypothesis, Action Steps, Target Count, Timebox, Success Threshold, Status |
| ValidationRecord | ID, Plan, Executed At, Actions Taken, Outcome, Lesson, Next Action, Status |
| RevenueSignal | ID, Record, Type, Strength, Amount, Buyer, Evidence, Next Step, Status |
| RejectionSignal | ID, Record, Type, Reason, Objection, Lesson, Segment, Status |
| OpportunityGenome | ID, Opportunity, Pain Intensity, Buyer Urgency, Budget Access, Timing Window, Serviceability, Status |
| MoneyDNA | ID, Opportunity, Skill Fit, Network Fit, Speed, Personal Edge, Anti-Patterns, Status |
| AlanMemory | ID, Period, Validated Patterns, Rejected Patterns, Strong Segments, Weak Segments, Lessons, Next Biases |

## Schema Evolution Rules
1. Additive changes are preferred.
2. Renames require migration notes in a future RFC.
3. Fields that affect scoring or selection must explain how they help Alan reach validated revenue signals faster.
4. Schema changes must not create product-building pressure before validation.
