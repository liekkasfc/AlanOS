# Alan OS

Alan OS is a Personal Revenue Operating System.

It helps Alan continuously discover information gaps, judge whether they are worth betting the next 30 days on, generate one executable money validation action per day, record results, and improve future decisions.

## What Alan OS Is
Alan OS is a personal operating loop for:

- discovering InformationGaps earlier than others,
- converting gaps into concrete money-making hypotheses,
- validating those hypotheses with real people before building products,
- recording RevenueSignals and RejectionSignals,
- learning Alan's personal opportunity pattern over time.

The system's North Star Metric is weekly validated revenue signal.

## What Alan OS Is Not
Alan OS is not:

- a news aggregator,
- GitHub Trending,
- Product Hunt daily,
- a hot list,
- a SaaS-first startup project,
- a passive inspiration database,
- a replacement for customer conversations,
- a reason to build before validation.

## Current Sprint
Sprint 1 Manual Revenue Validation Loop.

The current sprint creates the smallest manual loop for running one complete revenue validation cycle:

Signal -> InformationGap -> Opportunity -> Today's Bet -> ValidationPlan -> ValidationRecord -> RevenueSignal/RejectionSignal -> AlanMemory.

No collectors, analyzers, automation, database, UI, external integrations, or business implementation code should be written in Sprint 1.

## Directory Structure
```text
AlanOS/
  analyzers/
  configs/
  collectors/
  data/
    sample/
  docs/
    adr/
    rfc/
      RFC-0000-FOUNDATION.md
      RFC-0001-VISION.md
      RFC-0002-DOMAIN_MODEL.md
      RFC-0003-WORKFLOW.md
      RFC-0004-SCHEMA.md
    runbooks/
      manual_validation_loop.md
  engines/
  memory/
  outputs/
  prompts/
    SPRINT-000-ALAN-OS-FOUNDATION.md
    extract_information_gap.md
    generate_opportunity.md
    record_validation.md
    select_todays_bet.md
    update_alan_memory.md
  schemas/
  tests/
  validators/
  CODEX_GUIDE.md
  README.md
```

## How to Read the RFCs
Read the RFCs in order:

1. `docs/rfc/RFC-0000-FOUNDATION.md` explains why Alan OS exists and what it must not become.
2. `docs/rfc/RFC-0001-VISION.md` defines mission, vision, principles, North Star Metric, and slogan.
3. `docs/rfc/RFC-0002-DOMAIN_MODEL.md` defines the core entities and relationships.
4. `docs/rfc/RFC-0003-WORKFLOW.md` defines the end-to-end operating loop.
5. `docs/rfc/RFC-0004-SCHEMA.md` defines schema contracts and storage mappings.

Then read `CODEX_GUIDE.md` before asking an agent to modify the project.

## Sprint 1 Manual Loop
Sprint 1 supports manual validation, not a full product.

Use:

- `configs/source_registry.yaml` to pick manual-first sources,
- `data/sample/` to see one complete sample chain,
- `docs/runbooks/manual_validation_loop.md` to run the 60-minute loop,
- `prompts/` to extract gaps, generate opportunities, select Today's Bet, record validation, and update AlanMemory.

The loop still optimizes for action over information: help Alan reach a validated revenue signal faster.
