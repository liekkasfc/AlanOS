# RFC-0002: Domain Model

## Status
Draft

## Date
2026-06-29

## Summary
This RFC defines the core Alan OS domain model. These entities describe how raw market observations become InformationGaps, how gaps become Opportunities, how Alan selects one Today's Bet, and how validation results update AlanMemory.

## Concept Boundaries
An InformationGap is not a tool, project, startup idea, article, repository, or news item.

An InformationGap is a temporary asymmetric advantage: Alan notices a mismatch, need, constraint, new capability, or market confusion before the relevant buyers and builders have fully adapted.

An Opportunity is a monetizable interpretation of an InformationGap.

Today's Bet is the one action Alan should do today to reduce uncertainty or produce a revenue signal.

OpportunityGenome explains why an opportunity can make money.

MoneyDNA explains why an opportunity fits or does not fit Alan.

OpportunityLifecycle describes where the opportunity is in its market window:

- Birth
- Early
- Growth
- Peak
- Crowded
- Commodity
- Dead

## Entity: Signal

### Definition
A Signal is a raw observation from the outside world that may indicate change, pain, confusion, demand, or opportunity.

### Purpose
Signals provide evidence for discovering InformationGaps. A single Signal is rarely enough; multiple Signals become useful when they point to the same underlying gap.

### Key Fields
- `id`
- `source`
- `source_url`
- `captured_at`
- `title`
- `raw_content`
- `summary`
- `tags`
- `confidence`
- `status`

### Example
A founder posts that small teams are struggling to comply with a new AI procurement questionnaire from enterprise customers.

### Relationship to Other Entities
Signals are normalized and merged to support InformationGap extraction. Many Signals can support one InformationGap.

## Entity: InformationGap

### Definition
An InformationGap is a temporary asymmetric advantage created when some people know, need, or understand something earlier than others.

### Purpose
InformationGaps are the core discovery unit of Alan OS. They explain what changed and why acting now may matter.

### Key Fields
- `id`
- `name`
- `description`
- `evidence_signal_ids`
- `who_has_the_gap`
- `who_needs_the_gap_closed`
- `why_now`
- `window_start`
- `window_risk`
- `confidence`
- `status`

### Example
Small B2B AI vendors are being asked for security and compliance answers they do not know how to prepare, while enterprise buyers are moving faster than vendor documentation.

### Relationship to Other Entities
InformationGaps are extracted from Signals. One InformationGap can generate multiple Opportunities.

## Entity: Opportunity

### Definition
An Opportunity is a monetizable interpretation of an InformationGap for a reachable customer segment.

### Purpose
Opportunities turn gaps into concrete ways Alan might create value and receive money.

### Key Fields
- `id`
- `information_gap_id`
- `customer_segment`
- `buyer`
- `pain`
- `offer`
- `revenue_hypothesis`
- `distribution_path`
- `lifecycle_stage`
- `confidence`
- `status`

### Example
Offer a fixed-price "AI vendor security questionnaire readiness review" for small AI startups selling to enterprise customers.

### Relationship to Other Entities
Opportunities depend on InformationGaps, are explained by OpportunityGenome, scored against MoneyDNA, and can produce Today's Bets.

## Entity: Today's Bet

### Definition
Today's Bet is the one validation action Alan should execute today.

### Purpose
Today's Bet converts opportunity thinking into action. It prevents endless browsing and forces a small test.

### Key Fields
- `id`
- `opportunity_id`
- `date`
- `action`
- `target_personas`
- `timebox_minutes`
- `expected_signal`
- `give_up_rule`
- `success_criteria`
- `status`

### Example
Send five targeted messages to founders of AI tools asking whether enterprise security questionnaires have blocked a deal and offering a 30-minute paid review.

### Relationship to Other Entities
Today's Bet is selected from an Opportunity and usually creates a ValidationPlan. Its execution creates a ValidationRecord.

## Entity: ValidationPlan

### Definition
A ValidationPlan describes how Alan will test an Opportunity through real-world action before building.

### Purpose
ValidationPlans make execution specific enough to run and evaluate.

### Key Fields
- `id`
- `todays_bet_id`
- `opportunity_id`
- `hypothesis`
- `action_steps`
- `script`
- `target_count`
- `timebox_minutes`
- `success_threshold`
- `give_up_rule`
- `status`

### Example
Contact five founders with a short message, ask one budget-confirming question, and count a serious reply or paid review request as a positive signal.

### Relationship to Other Entities
ValidationPlans operationalize Today's Bet and define how ValidationRecords should be interpreted.

## Entity: ValidationRecord

### Definition
A ValidationRecord captures what happened when Alan executed a ValidationPlan.

### Purpose
ValidationRecords preserve facts, outcomes, and lessons so Alan OS can learn from execution.

### Key Fields
- `id`
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
- `status`

### Example
Alan messaged five founders. Two replied, one asked for pricing, one said their buyer already provides templates, and one booked a call.

### Relationship to Other Entities
ValidationRecords produce RevenueSignals and RejectionSignals. They update AlanMemory and MoneyDNA.

## Entity: RevenueSignal

### Definition
A RevenueSignal is evidence that a real person may pay, has paid, or is moving toward a paid action.

### Purpose
RevenueSignals are the core metric for Alan OS. They distinguish money evidence from attention.

### Key Fields
- `id`
- `validation_record_id`
- `signal_type`
- `amount`
- `currency`
- `buyer`
- `strength`
- `evidence`
- `next_step`
- `confidence`
- `status`

### Example
A founder agrees to pay 200 USD for a same-day questionnaire readiness review.

### Relationship to Other Entities
RevenueSignals come from ValidationRecords and contribute to weekly validated revenue signal. They update Opportunity scoring and AlanMemory.

## Entity: RejectionSignal

### Definition
A RejectionSignal is structured evidence that a target customer ignored, declined, delayed, objected to, or reframed the offer.

### Purpose
RejectionSignals prevent wasted repetition and turn failure into learning.

### Key Fields
- `id`
- `validation_record_id`
- `rejection_type`
- `stated_reason`
- `implicit_reason`
- `segment`
- `objection`
- `lesson`
- `confidence`
- `status`

### Example
Three founders say security questionnaires are painful but not urgent until a deal is already in procurement.

### Relationship to Other Entities
RejectionSignals come from ValidationRecords and update OpportunityGenome, MoneyDNA, and AlanMemory.

## Entity: OpportunityGenome

### Definition
OpportunityGenome explains why an Opportunity can make money.

### Purpose
It decomposes monetizability into reusable traits so Alan OS can recognize similar patterns later.

### Key Fields
- `id`
- `opportunity_id`
- `pain_intensity`
- `buyer_urgency`
- `budget_access`
- `solution_substitutability`
- `distribution_advantage`
- `timing_window`
- `trust_requirement`
- `serviceability`
- `confidence`
- `status`

### Example
The AI questionnaire readiness offer has high urgency near enterprise procurement, clear buyer value, low initial software need, and strong serviceability.

### Relationship to Other Entities
OpportunityGenome is derived from an Opportunity and updated by ValidationRecords, RevenueSignals, and RejectionSignals.

## Entity: MoneyDNA

### Definition
MoneyDNA explains why an Opportunity fits or does not fit Alan.

### Purpose
It models Alan's personal fit: skills, network, credibility, energy, language, speed, and execution constraints.

### Key Fields
- `id`
- `opportunity_id`
- `skill_fit`
- `network_fit`
- `credibility_fit`
- `interest_fit`
- `speed_to_execute`
- `delivery_risk`
- `personal_edge`
- `anti_patterns`
- `confidence`
- `status`

### Example
Alan may have strong fit if he understands AI tools, can write clearly in English and Chinese, and can reach founders quickly.

### Relationship to Other Entities
MoneyDNA scores Opportunities for Alan and improves through AlanMemory.

## Entity: OpportunityLifecycle

### Definition
OpportunityLifecycle describes the maturity stage of a market opportunity.

### Purpose
It helps Alan understand timing, competition, urgency, and whether service-first validation still has room.

### Key Fields
- `id`
- `opportunity_id`
- `stage`
- `stage_evidence`
- `window_open_reason`
- `crowding_indicators`
- `decay_risk`
- `recommended_posture`
- `confidence`
- `status`

### Example
The questionnaire readiness offer is Early if many vendors are newly encountering buyer requests and few service providers have positioned around it.

### Relationship to Other Entities
OpportunityLifecycle is attached to an Opportunity and informs Today's Bet selection.

## Lifecycle Stages
| Stage | Meaning | Alan OS Posture |
| --- | --- | --- |
| Birth | Signals are faint; buyers may not know the pain clearly | Explore manually, interview, avoid building |
| Early | Pain is emerging and language is unstable | Offer service, learn buyer words |
| Growth | Demand is visible and competitors appear | Validate pricing and distribution |
| Peak | Attention and spending are high | Specialize or move fast |
| Crowded | Many providers chase the same pain | Look for sub-gaps or avoid |
| Commodity | Buyers expect standard solutions | Compete only with clear advantage |
| Dead | The gap closed or demand disappeared | Archive and extract lessons |

## Entity: AlanMemory

### Definition
AlanMemory is the accumulated record of Alan's signals, bets, validation outcomes, lessons, and personal opportunity pattern.

### Purpose
AlanMemory prevents repeated mistakes and helps the system recommend better bets over time.

### Key Fields
- `id`
- `period`
- `validated_patterns`
- `rejected_patterns`
- `strong_segments`
- `weak_segments`
- `money_dna_updates`
- `weekly_revenue_signals`
- `lessons`
- `next_biases`
- `status`

### Example
After several validation cycles, AlanMemory learns that Alan gets stronger responses from founder-led B2B tools than from consumer creator tools.

### Relationship to Other Entities
AlanMemory is updated by ValidationRecords, RevenueSignals, RejectionSignals, OpportunityGenome, and MoneyDNA.

## Entity Flow
1. Signals are collected.
2. Signals are normalized and merged.
3. InformationGaps are extracted.
4. Opportunities are generated from InformationGaps.
5. OpportunityGenome explains monetizability.
6. MoneyDNA scores Alan fit.
7. OpportunityLifecycle evaluates timing.
8. One Today's Bet is selected.
9. A ValidationPlan makes the bet executable.
10. A ValidationRecord captures results.
11. RevenueSignals and RejectionSignals update AlanMemory.
