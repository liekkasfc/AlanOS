# Alan OS Sprint 0: Foundation RFC Documents

You are working on a new branch for Alan OS.

Alan OS is NOT a news aggregator, NOT GitHub Trending, NOT Product Hunt daily, and NOT a SaaS-first startup project.

Alan OS is a Personal Revenue Operating System.

Its purpose is to help Alan continuously discover information gaps, judge whether they are worth betting the next 30 days on, generate one executable money validation action per day, record results, and improve future decisions.

## Core Mission

Help Alan build a lifelong ability to:

1. discover information gaps earlier than others,
2. convert them into concrete money-making hypotheses,
3. validate them with real people before building products,
4. record execution results,
5. learn Alan's personal opportunity pattern over time.

## Important Design Rule

Do NOT write business implementation code in this sprint.

Only create foundational project documents.

## Files to create

Create the following files:

1. docs/rfc/RFC-0000-FOUNDATION.md
2. docs/rfc/RFC-0001-VISION.md
3. docs/rfc/RFC-0002-DOMAIN_MODEL.md
4. docs/rfc/RFC-0003-WORKFLOW.md
5. docs/rfc/RFC-0004-SCHEMA.md
6. CODEX_GUIDE.md
7. README.md

## Document Requirements

### RFC-0000-FOUNDATION.md

Describe the foundation of Alan OS.

Must include:

- Why Alan OS exists.
- What problem it solves for Alan.
- Why this is not a normal product.
- Why it is a personal second-income operating system.
- Difference between Opportunity Radar and Alan OS.
- Core design philosophy:
  - reduce uncertainty,
  - increase validated income,
  - avoid endless research,
  - force small execution,
  - learn from rejection.
- Non-goals:
  - not a news system,
  - not a hot list,
  - not a SaaS-first system,
  - not a passive inspiration database.

### RFC-0001-VISION.md

Describe the mission, vision, principles, and long-term direction.

Must include:

- One sentence description.
- English mission.
- Chinese mission.
- Vision for 1 year, 3 years, 10 years.
- Product principles:
  1. Action over information.
  2. Revenue signal over popularity.
  3. One Today's Bet per day.
  4. Service before product.
  5. Sell before build.
  6. No customer, no opportunity.
  7. No give-up rule, no execution.
  8. Rejection is an asset.
- North Star Metric:
  weekly validated revenue signal.
- System slogan:
  "Don't chase trends. Own the gap."

### RFC-0002-DOMAIN_MODEL.md

Define the domain model.

Must include these core entities:

1. Signal
2. InformationGap
3. Opportunity
4. Today's Bet
5. ValidationPlan
6. ValidationRecord
7. RevenueSignal
8. RejectionSignal
9. OpportunityGenome
10. MoneyDNA
11. OpportunityLifecycle
12. AlanMemory

For each entity include:

- Definition
- Purpose
- Key fields
- Example
- Relationship to other entities

Important concepts:

- Information Gap is not a tool, project, or news item.
- Information Gap is a temporary asymmetric advantage.
- Opportunity is a monetizable interpretation of an Information Gap.
- Today's Bet is the one action Alan should do today.
- OpportunityGenome explains why an opportunity can make money.
- MoneyDNA explains why an opportunity fits or does not fit Alan.
- OpportunityLifecycle includes:
  - Birth
  - Early
  - Growth
  - Peak
  - Crowded
  - Commodity
  - Dead

### RFC-0003-WORKFLOW.md

Define the full workflow.

Must include:

1. Discover
2. Normalize
3. Merge
4. Extract Information Gap
5. Analyze Window
6. Generate Opportunity
7. Score for Alan
8. Select Today's Bet
9. Generate Validation Plan
10. Execute 60-minute action
11. Record Validation
12. Learn from Results
13. Update Memory

For each step include:

- Input
- Output
- Responsibility
- Example
- Failure mode
- Acceptance criteria

The workflow must emphasize:

- No endless browsing.
- No more than one Today's Bet.
- No product development before validation.
- Every opportunity must lead to a concrete action.

### RFC-0004-SCHEMA.md

Define JSON schemas and storage schemas.

Must include schemas for:

1. signal.schema.json
2. information_gap.schema.json
3. opportunity.schema.json
4. todays_bet.schema.json
5. validation_plan.schema.json
6. validation_record.schema.json
7. revenue_signal.schema.json
8. rejection_signal.schema.json
9. opportunity_genome.schema.json
10. money_dna.schema.json
11. alan_memory.schema.json

Each schema should include:

- id
- created_at
- updated_at
- source
- confidence
- status
- required fields
- optional fields
- example JSON

Also include storage mapping for:

- JSON files
- SQLite tables
- Obsidian frontmatter
- Feishu Bitable fields

### CODEX_GUIDE.md

Create a development guide for Codex.

Must include:

- Codex role.
- Development rules.
- Forbidden behaviors.
- How to add new RFC.
- How to add new schema.
- How to add new data source.
- How to decide whether a feature should be built.
- Absolute rule:
  If a feature cannot explain how it helps Alan reach a validated revenue signal faster, do not build it.

### README.md

Create a project-level README.

Must include:

- What Alan OS is.
- What it is not.
- Current Sprint: Sprint 0 Foundation.
- Directory structure.
- How to read RFCs.
- Next Sprint suggestion.

## Output Style

Write all documents in clear Markdown.

Use English file names.

Chinese content is acceptable and preferred where useful.

Do not create implementation code yet.

Do not modify existing business logic.

Do not delete existing files.

At the end, print a summary of created files and next recommended command.
