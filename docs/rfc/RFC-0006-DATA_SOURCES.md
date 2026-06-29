# RFC-0006: Data Sources

## Status
Draft

## Date
2026-06-29

## Summary
This RFC defines how Alan OS should think about data sources during the foundation stage.

Alan OS is not a news aggregator. Data sources are useful only when they help Alan discover information gaps, identify reachable buyers, and design a validation action that can produce a revenue signal.

This RFC does not define collectors. Sprint 0.1 is documentation and schema preparation only.

## Source Principle
A source is valuable when it helps answer at least one of these questions:

1. What changed?
2. Who feels the pain before others notice?
3. Who needs the gap closed?
4. Why might the timing matter now?
5. What paid offer could Alan test manually?
6. Where can Alan reach the buyer today?

If a source cannot help answer these questions, it may be interesting but it is not Alan OS input yet.

## Source Categories

### Customer Pain Surfaces
Places where real users, founders, operators, or buyers describe a painful workflow, blocked deal, urgent confusion, or costly workaround.

Examples:

- founder posts,
- operator complaints,
- community questions,
- customer interviews,
- support threads,
- job-to-be-done conversations.

### Buyer Intent Surfaces
Places where budgets, procurement activity, hiring, vendor evaluation, or purchase language appears.

Examples:

- job posts,
- RFP language,
- vendor comparison discussions,
- procurement checklists,
- paid community requests,
- public calls for consultants or tools.

### Change Surfaces
Places where a regulation, platform shift, model capability, API policy, pricing change, or workflow constraint creates new confusion.

Examples:

- regulation updates,
- platform changelogs,
- API deprecations,
- model releases,
- security requirements,
- ecosystem policy changes.

### Crowding Surfaces
Places that show whether an opportunity is still early, already crowded, commoditized, or dead.

Examples:

- competitor landing pages,
- marketplace listings,
- service provider positioning,
- search results,
- pricing pages,
- social proof density.

### Alan-Owned Surfaces
Places where Alan can directly learn from people or test offers.

Examples:

- personal network,
- direct messages,
- past clients,
- friends of friends,
- communities Alan can credibly participate in,
- audiences where Alan can post an offer.

## Source Eligibility Rules
A source should be admitted into Alan OS only when it can produce or improve one of these records:

- Signal,
- InformationGap,
- Opportunity,
- OpportunityLifecycle,
- Today's Bet,
- ValidationRecord,
- RevenueSignal,
- RejectionSignal,
- AlanMemory.

The source should also have at least one of:

- buyer proximity,
- pain specificity,
- timing evidence,
- reachable people,
- contradiction value,
- revenue language,
- validation path.

## Source Scoring Dimensions
Sources should be judged by:

- `gap_relevance`: does it reveal a temporary mismatch or advantage?
- `buyer_proximity`: does it involve people who can pay or influence payment?
- `actionability`: can Alan act on it today?
- `freshness`: does timing affect the opportunity window?
- `specificity`: does it name a concrete workflow, pain, or constraint?
- `contradiction_value`: does it prevent Alan from chasing a false signal?
- `reachability`: can Alan contact or observe the relevant people?

Popularity is not a scoring dimension by itself.

## Manual-First Rule
Before collectors exist, Alan OS should support manual capture and review. The system should prefer fewer high-quality Signals over many weak ones.

Automation can be considered later only after the manual loop proves which sources regularly produce validated revenue learning.

## Source Non-Goals
Alan OS should not optimize for:

- maximum link volume,
- comprehensive news coverage,
- trending topic coverage,
- passive dashboards,
- generic market intelligence,
- collecting content without buyer access,
- collecting sources that cannot affect Today's Bet.

## Acceptance Criteria
The data source model is successful when:

- every source can explain its role in the revenue-validation loop,
- source review ends in action or rejection rather than hoarding,
- Today's Bet selection improves because source quality improves,
- sources help Alan find buyers, not just topics,
- no collector is implied before manual validation proves source value.
