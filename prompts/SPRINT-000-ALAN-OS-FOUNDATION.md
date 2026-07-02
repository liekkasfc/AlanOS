# Alan OS Sprint 0: Foundation RFC Documents

你正在为 Alan OS 的 foundation sprint 工作。

Alan OS 不是 news aggregator，不是 GitHub Trending，不是 Product Hunt daily，也不是 SaaS-first startup project。

Alan OS 是 Personal Revenue Operating System。它的目标是帮助 Alan 持续发现信息差，判断它们是否值得下注，把它们转成每天一个可执行的收入验证动作，记录结果，并改进未来判断。

## Core Mission

帮助 Alan 建立长期能力：

1. 比别人更早发现 information gaps；
2. 把它们转成具体 money-making hypotheses；
3. 在构建产品前用真实的人验证；
4. 记录 execution results；
5. 学习 Alan 的个人 opportunity pattern。

## Important Design Rule

本 sprint 不写 business implementation code。

只创建 foundational project documents。

## Files to create

创建以下文件：

1. docs/rfc/RFC-0000-FOUNDATION.md
2. docs/rfc/RFC-0001-VISION.md
3. docs/rfc/RFC-0002-DOMAIN_MODEL.md
4. docs/rfc/RFC-0003-WORKFLOW.md
5. docs/rfc/RFC-0004-SCHEMA.md
6. CODEX_GUIDE.md
7. README.md

## Document Requirements

### RFC-0000-FOUNDATION.md

说明 Alan OS 的基础：

- Alan OS 为什么存在；
- 它为 Alan 解决什么问题；
- 为什么它不是普通产品；
- 为什么它是 personal second-income operating system；
- Opportunity Radar 和 Alan OS 的区别；
- core design philosophy：
  - reduce uncertainty；
  - increase validated income；
  - avoid endless research；
  - force small execution；
  - learn from rejection；
- non-goals：
  - not a news system；
  - not a hot list；
  - not a SaaS-first system；
  - not a passive inspiration database。

### RFC-0001-VISION.md

说明 mission、vision、principles 和 long-term direction。

必须包含：

- one sentence description；
- English mission；
- Chinese mission；
- 1 year、3 years、10 years vision；
- product principles：
  1. Action over information.
  2. Revenue signal over popularity.
  3. One Today's Bet per day.
  4. Service before product.
  5. Sell before build.
  6. No customer, no opportunity.
  7. No give-up rule, no execution.
  8. Rejection is an asset.
- North Star Metric：weekly validated revenue signal；
- system slogan："Don't chase trends. Own the gap."

### RFC-0002-DOMAIN_MODEL.md

定义 domain model。

必须包含这些 core entities：

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

每个 entity 包含：

- Definition；
- Purpose；
- Key fields；
- Example；
- Relationship to other entities。

重要概念：

- InformationGap 不是 tool、project 或 news item。
- InformationGap 是 temporary asymmetric advantage。
- Opportunity 是 InformationGap 的 monetizable interpretation。
- Today's Bet 是 Alan 今天应该做的唯一动作。
- OpportunityGenome 解释为什么一个 opportunity 能赚钱。
- MoneyDNA 解释一个 opportunity 为什么适合或不适合 Alan。
- OpportunityLifecycle 包括：
  - Birth
  - Early
  - Growth
  - Peak
  - Crowded
  - Commodity
  - Dead

### RFC-0003-WORKFLOW.md

定义完整 workflow。

必须包含：

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

每个 step 包含：

- Input；
- Output；
- Responsibility；
- Example；
- Failure mode；
- Acceptance criteria。

workflow 必须强调：

- No endless browsing；
- No more than one Today's Bet；
- No product development before validation；
- Every opportunity must lead to a concrete action。

### RFC-0004-SCHEMA.md

定义 JSON schemas 和 storage schemas。

必须包含这些 schemas：

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

每个 schema 包含：

- id；
- created_at；
- updated_at；
- source；
- confidence；
- status；
- required fields；
- optional fields；
- example JSON。

还要包含 storage mapping：

- JSON files；
- SQLite tables；
- Obsidian frontmatter；
- Feishu Bitable fields。

### CODEX_GUIDE.md

创建 Codex development guide。

必须包含：

- Codex role；
- Development rules；
- Forbidden behaviors；
- How to add new RFC；
- How to add new schema；
- How to add new data source；
- How to decide whether a feature should be built；
- absolute rule：
  If a feature cannot explain how it helps Alan reach a validated revenue signal faster, do not build it.

### README.md

创建 project-level README。

必须包含：

- What Alan OS is；
- What it is not；
- Current Sprint: Sprint 0 Foundation；
- Directory structure；
- How to read RFCs；
- Next Sprint suggestion。

## Output Style

用清晰 Markdown 写所有 documents。

使用 English file names。

中文内容可接受，并且在对 Alan 说明时优先使用中文。

不要创建 implementation code。

不要修改 existing business logic。

不要删除 existing files。

最后输出 created files summary 和 next recommended command。
