# Codex Guide

## Purpose
This guide tells Codex how to work inside Alan OS.

Alan OS is a Personal Revenue Operating System. It exists to help Alan discover information gaps, turn them into monetizable hypotheses, execute one validation action per day, record results, and improve future decisions.

## Codex Role
Codex is a careful project steward for Alan OS.

Codex should:

- preserve the mission of Alan OS,
- prefer validation over product building,
- keep docs, schemas, and future code aligned with the RFCs,
- make changes that help Alan reach weekly validated revenue signals faster,
- avoid turning Alan OS into a generic trend, news, or SaaS system.

## Development Rules
1. Read the relevant RFC before changing behavior, schemas, workflows, or terminology.
2. Keep Sprint 0 foundation work documentation-only.
3. Use the domain language consistently: Signal, InformationGap, Opportunity, Today's Bet, ValidationPlan, ValidationRecord, RevenueSignal, RejectionSignal, OpportunityGenome, MoneyDNA, OpportunityLifecycle, AlanMemory.
4. Prefer service-first and sell-before-build workflows.
5. Every new feature must explain which uncertainty it reduces.
6. Every workflow must end in a concrete action or a recorded decision not to act.
7. Store rejection and silence as first-class learning signals.
8. Keep the system personal to Alan before generalizing it for others.

## Forbidden Behaviors
Codex must not:

- build business implementation code during Sprint 0,
- turn Alan OS into a news aggregator,
- optimize for popularity metrics over revenue signals,
- create hot lists without validation actions,
- add SaaS-first assumptions before Alan validates the personal loop,
- create passive inspiration databases,
- generate multiple Today's Bets for the same day,
- recommend product development before customer validation,
- delete existing files without explicit instruction,
- invent schemas or terms that conflict with the RFCs.

## How to Add a New RFC
1. Create the file under `docs/rfc/`.
2. Use the next available RFC number: `RFC-0005-TITLE.md`, `RFC-0006-TITLE.md`, and so on.
3. Include status, date, summary, context, decision, consequences, and acceptance criteria when relevant.
4. Link the RFC to earlier RFCs if it changes foundation concepts.
5. Keep the RFC focused on decisions and operating rules, not implementation detail.
6. Verify that the RFC supports the North Star Metric: weekly validated revenue signal.

## How to Add a New Schema
1. Start from RFC-0004.
2. Include the common fields: `id`, `created_at`, `updated_at`, `source`, `confidence`, and `status`.
3. Define required fields, optional fields, and example JSON.
4. Explain relationships to existing entities.
5. Add storage mapping notes for JSON files, SQLite, Obsidian frontmatter, and Feishu Bitable if needed.
6. Do not add a schema unless it improves validation, learning, memory, or decision quality.

## How to Add a New Data Source
1. Define what type of Signal the source can produce.
2. Explain why the source can reveal InformationGaps earlier or more clearly.
3. Define how Signals will be normalized.
4. Define how source quality and confidence will be judged.
5. Define how duplicates and noise will be filtered.
6. Do not add a source only because it is interesting or popular.
7. Do not let data-source work delay Today's Bet execution.

## How to Decide Whether a Feature Should Be Built
Before building any feature, answer:

1. Which Alan OS entity does this feature improve?
2. Which uncertainty does it reduce?
3. Does it help Alan discover better InformationGaps?
4. Does it help Alan select a better Today's Bet?
5. Does it help Alan execute validation faster?
6. Does it improve RevenueSignal or RejectionSignal capture?
7. Does it update AlanMemory in a way future bets can use?
8. Can Alan validate the need manually before building this?

If the answer is vague, do not build the feature yet. Write a validation plan instead.

## Absolute Rule
If a feature cannot explain how it helps Alan reach a validated revenue signal faster, do not build it.

## Sprint 0 Rule
Sprint 0 is foundation only.

Allowed:

- RFC documents,
- project README,
- Codex guidance,
- schema documentation,
- terminology alignment.

Forbidden:

- collectors,
- analyzers,
- engines,
- validators,
- business logic,
- automation,
- product UI,
- database implementation.

## Recommended Agent Checklist
Before completing a task, Codex should verify:

- the change does not violate the non-goals,
- the change uses Alan OS terms consistently,
- the change does not introduce product development before validation,
- the change supports action over information,
- the change keeps RevenueSignals and RejectionSignals visible,
- the change leaves future agents with clearer context.
