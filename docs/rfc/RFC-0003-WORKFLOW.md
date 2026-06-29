# RFC-0003: Workflow

## Status
Draft

## Date
2026-06-29

## Summary
This RFC defines the Alan OS workflow from raw discovery to AlanMemory updates. The workflow exists to prevent endless browsing and force one concrete validation action before product development.

## Workflow Rules
1. No endless browsing.
2. No more than one Today's Bet per day.
3. No product development before validation.
4. Every Opportunity must lead to a concrete action.
5. Every action must produce a record, even when the result is silence or rejection.

## Step 1: Discover

### Input
External sources such as posts, forums, newsletters, customer conversations, repositories, regulation changes, job posts, tool launches, and founder complaints.

### Output
Raw Signals.

### Responsibility
Capture potentially meaningful market changes without judging them too early.

### Example
Alan notices repeated founder complaints about enterprise AI security questionnaires.

### Failure Mode
Collecting interesting content with no buyer, pain, or change behind it.

### Acceptance Criteria
- Each captured Signal has a source.
- Each Signal records what changed or what pain appeared.
- Discovery stops once enough Signals exist to examine a candidate gap.

## Step 2: Normalize

### Input
Raw Signals.

### Output
Structured Signals with summaries, tags, source metadata, and confidence.

### Responsibility
Convert messy observations into comparable records.

### Example
Normalize several posts into tags like `enterprise_sales`, `ai_vendor`, `security_questionnaire`, and `procurement_delay`.

### Failure Mode
Keeping raw links without extracting the relevant claim.

### Acceptance Criteria
- The normalized Signal has a concise summary.
- The original source is preserved.
- The Signal can be compared with other Signals.

## Step 3: Merge

### Input
Normalized Signals.

### Output
Signal clusters.

### Responsibility
Group Signals that point to the same underlying market change or pain.

### Example
Merge founder posts, buyer comments, and job posts that all indicate security compliance work is slowing AI vendor sales.

### Failure Mode
Treating every Signal as a separate opportunity.

### Acceptance Criteria
- Similar Signals are grouped.
- Contradictory Signals are marked.
- Each cluster has a short explanation of the shared pattern.

## Step 4: Extract Information Gap

### Input
Signal clusters.

### Output
InformationGap candidates.

### Responsibility
Identify the temporary asymmetric advantage inside the cluster.

### Example
Many AI vendors are discovering procurement security expectations after a deal starts, while vendors that prepare earlier can move faster.

### Failure Mode
Calling a tool, article, or trend an InformationGap.

### Acceptance Criteria
- The gap names who knows or feels the issue early.
- The gap names who needs the gap closed.
- The gap explains why the advantage may be temporary.

## Step 5: Analyze Window

### Input
InformationGap candidate.

### Output
Timing assessment and OpportunityLifecycle stage.

### Responsibility
Judge whether the window is opening, already crowded, commoditized, or dead.

### Example
The opportunity is Early because demand is appearing in sales conversations but few specialized providers exist.

### Failure Mode
Assuming every new topic is early.

### Acceptance Criteria
- Lifecycle stage is assigned.
- Evidence for the stage is recorded.
- Crowding and decay risks are named.

## Step 6: Generate Opportunity

### Input
InformationGap and timing assessment.

### Output
One or more Opportunities.

### Responsibility
Translate the gap into monetizable interpretations for reachable customers.

### Example
Create a fixed-price service to review AI vendor security questionnaire readiness before enterprise procurement.

### Failure Mode
Generating product ideas without a buyer or offer.

### Acceptance Criteria
- The Opportunity has a customer segment.
- The buyer or decision maker is named.
- The revenue hypothesis is explicit.
- The first validation path does not require building software.

## Step 7: Score for Alan

### Input
Opportunity, OpportunityGenome, MoneyDNA, and AlanMemory.

### Output
Alan fit score and ranking.

### Responsibility
Judge whether this Opportunity is promising for Alan specifically.

### Example
Score high if Alan can reach founders, understand the domain language, and deliver a useful manual review quickly.

### Failure Mode
Choosing opportunities that are generally interesting but personally hard for Alan to execute.

### Acceptance Criteria
- Skill fit is assessed.
- Network or distribution path is assessed.
- Delivery risk is named.
- The score explains why Alan should or should not act.

## Step 8: Select Today's Bet

### Input
Ranked Opportunities.

### Output
One Today's Bet.

### Responsibility
Choose the single most useful action Alan should execute today.

### Example
Send five targeted outreach messages to AI founders with a specific paid review offer.

### Failure Mode
Selecting multiple bets, vague research tasks, or actions that require building first.

### Acceptance Criteria
- Exactly one Today's Bet is selected.
- The action can be completed today.
- The expected signal is clear.
- A give-up rule is defined.

## Step 9: Generate Validation Plan

### Input
Today's Bet.

### Output
ValidationPlan.

### Responsibility
Turn the bet into an executable plan with steps, script, target count, timebox, and success threshold.

### Example
Use a 60-minute plan: identify five founders, send a short message, ask whether the pain blocked a deal, offer a paid readiness review, record replies.

### Failure Mode
Producing a plan that is too broad to execute.

### Acceptance Criteria
- The plan fits the timebox.
- The plan includes specific targets.
- The plan defines success and rejection signals.
- The plan requires no product development.

## Step 10: Execute 60-Minute Action

### Input
ValidationPlan.

### Output
Completed outreach, conversation, offer, post, or other market action.

### Responsibility
Alan acts in the real world for 60 minutes or less.

### Example
Alan sends five messages and replies to any immediate responses.

### Failure Mode
Replacing execution with more browsing, polishing, or building.

### Acceptance Criteria
- The planned action was actually attempted.
- Time spent is recorded.
- Deviations are noted.

## Step 11: Record Validation

### Input
Execution results.

### Output
ValidationRecord, RevenueSignals, and RejectionSignals.

### Responsibility
Capture what happened without narrative distortion.

### Example
Record messages sent, replies received, objections, budget comments, booked calls, and silence.

### Failure Mode
Only recording positive outcomes or relying on memory.

### Acceptance Criteria
- Actions taken are listed.
- Responses and silence are recorded.
- RevenueSignals are separated from RejectionSignals.
- Lessons are written before moving to the next idea.

## Step 12: Learn from Results

### Input
ValidationRecord, RevenueSignals, RejectionSignals, OpportunityGenome, and MoneyDNA.

### Output
Updated interpretation of the Opportunity and Alan fit.

### Responsibility
Convert outcomes into reusable learning.

### Example
Learn that founders respond to procurement-delay language but not to generic compliance language.

### Failure Mode
Treating rejection as emotional failure instead of structured evidence.

### Acceptance Criteria
- At least one lesson is recorded.
- The lesson changes a future decision, script, segment, or score.
- The Opportunity status is updated.

## Step 13: Update Memory

### Input
Lessons, updated scores, RevenueSignals, and RejectionSignals.

### Output
Updated AlanMemory.

### Responsibility
Compound Alan's personal opportunity pattern over time.

### Example
Update AlanMemory to prefer urgent B2B founder pain with a clear manual service path.

### Failure Mode
Letting each validation cycle disappear as isolated notes.

### Acceptance Criteria
- AlanMemory records the pattern.
- MoneyDNA is adjusted when appropriate.
- Future Today's Bet selection can use the new learning.

## End-to-End Acceptance Criteria
The workflow is functioning when:

- discovery produces fewer, higher-quality gaps,
- no selected Opportunity lacks a customer segment,
- exactly one Today's Bet is selected per execution day,
- validation happens before product development,
- every validation attempt produces a record,
- AlanMemory improves from both RevenueSignals and RejectionSignals.
