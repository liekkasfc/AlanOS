# Alan OS

Alan OS 是 Alan 的 Personal Revenue Operating System，也就是个人收入操作系统。

它帮助 Alan 持续发现可行动的信息差，判断这些信息差是否值得下注，把它们转成每天一个可执行的收入验证动作，记录结果，并把经验沉淀进下一次判断。

## Alan OS 是什么
Alan OS 是一个个人操作循环，用来帮助 Alan：

- 从真实世界里捕捉 Signal（信号，观察到的原始线索）；
- 从 Signal 中提炼 InformationGap（信息差，暂时存在的不对称机会）；
- 把 InformationGap 转成 Opportunity（可变现机会）；
- 每天选择一个 Today's Bet（今日唯一验证动作）；
- 用 ValidationPlan（验证计划）去接触真实买家或推荐人；
- 用 ValidationRecord（验证记录）记录行动结果；
- 把 RevenueSignal（收入信号）和 RejectionSignal（拒绝信号）沉淀进 AlanMemory（Alan 机会记忆）。

系统的 North Star Metric 是 weekly validated revenue signal，也就是每周产生多少经过真实行动验证的收入信号。

## Alan OS 不是什么
Alan OS 不是：

- 新闻聚合器；
- GitHub Trending；
- Product Hunt daily；
- 热点列表；
- SaaS-first startup project；
- 被动灵感数据库；
- 客户访谈的替代品；
- 让 Alan 在验证前就开始构建产品的理由。

## Current Sprint
Sprint 3.2 Pre/Post Execution Validation Split.

当前 Sprint 把验证拆成两个阶段：行动前确认 Today's Bet 是否可执行，行动后确认 ValidationRecord、RevenueSignal、RejectionSignal 和 AlanMemory 是否被真实回填。

本地 workspace 只创建、验证、渲染已准备好的本地记录。它不会收集数据、浏览网页、调用外部 API、使用数据库、创建 UI，也不会把 Alan OS 变成新闻看板。

## 目录结构
```text
AlanOS/
  analyzers/
  configs/
  collectors/
  data/
    daily/
    sample/
      daily_output.sample.md
  docs/
    GLOSSARY.zh-CN.md
    adr/
    rfc/
      RFC-0000-FOUNDATION.md
      RFC-0001-VISION.md
      RFC-0002-DOMAIN_MODEL.md
      RFC-0003-WORKFLOW.md
      RFC-0004-SCHEMA.md
    runbooks/
      daily_bet_generation.md
      local_validation_workspace.md
      manual_validation_loop.md
  engines/
  memory/
    alan_context.json
  outputs/
  prompts/
    SPRINT-000-ALAN-OS-FOUNDATION.md
    extract_information_gap.md
    generate_opportunity.md
    record_validation.md
    select_todays_bet.md
    update_alan_memory.md
  schemas/
  scripts/
    generate_daily_output.py
    init_daily_workspace.py
    validate_records.py
  templates/
    daily_output_template.md
  tests/
    test_generate_daily_output.py
    test_init_daily_workspace.py
    test_validate_records.py
  validators/
  Makefile
  CODEX_GUIDE.md
  README.md
```

## 如何阅读 RFC
按顺序阅读：

1. `docs/rfc/RFC-0000-FOUNDATION.md` 解释 Alan OS 为什么存在，以及它绝对不能变成什么。
2. `docs/rfc/RFC-0001-VISION.md` 定义 mission、vision、principles、North Star Metric 和 slogan。
3. `docs/rfc/RFC-0002-DOMAIN_MODEL.md` 定义核心实体和它们之间的关系。
4. `docs/rfc/RFC-0003-WORKFLOW.md` 定义端到端操作循环。
5. `docs/rfc/RFC-0004-SCHEMA.md` 定义 schema contracts 和 storage mappings。

再阅读 `CODEX_GUIDE.md`，然后再让 agent 修改项目。

术语可参考 `docs/GLOSSARY.zh-CN.md`。

## Sprint 1 Manual Loop
Sprint 1 支持手动验证，不是完整产品。

使用：

- `configs/source_registry.yaml` 选择 manual-first sources；
- `data/sample/` 查看一条完整样例链；
- `docs/runbooks/manual_validation_loop.md` 执行 60 分钟手动验证循环；
- `prompts/` 提炼 InformationGap、生成 Opportunity、选择 Today's Bet、记录验证结果、更新 AlanMemory。

这个循环始终优先行动，而不是优先信息收集：帮助 Alan 更快到达 validated revenue signal。

## Sprint 2 Daily Bet Generator
Sprint 2 从本地已准备好的 JSON records 渲染每日行动包。

使用：

- `scripts/generate_daily_output.py` 从本地 JSON records 渲染 Markdown；
- `templates/daily_output_template.md` 查看输出结构；
- `data/sample/daily_output.sample.md` 查看样例输出；
- `docs/runbooks/daily_bet_generation.md` 手动运行生成器。

脚本必须为一个日期只输出一个 Today's Bet，并在同一天有多个 active candidates 时失败。

## Sprint 3 Local Validation Workspace
Sprint 3 支持 `data/daily/YYYY-MM-DD/` 下的真实本地每日记录。

使用：

- `make init-day DATE=2026-06-29` 创建本地手动 record files；
- `make validate-day DATE=2026-06-29` 对本地 JSON records 做结构验证；
- `make validate-links DATE=2026-06-29` 验证本地 records 之间的关系；
- `make validate-ready DATE=2026-06-29` 检查 bet 和 plan 是否可执行；
- `make validate-result DATE=2026-06-29` 检查执行结果是否已记录；
- `make render-day DATE=2026-06-29` 渲染 daily action packet；
- `make sample-output` 查看 sample packet；
- `make test` 运行本地测试套件。

`scripts/validate_records.py` 使用一个小型本地 schema validator 覆盖当前 Alan OS schema 子集。不需要安装 `jsonschema` package。

`validate-day` 检查本地 JSON 结构、required fields、简单类型、enums 和日期格式。`validate-links` 检查本地 ID 关系。`validate-ready` 检查行动前 records 是否足以执行一个 Today's Bet。`validate-result` 检查 Alan 已行动之后的结果 records 是否已回填。

## 当前推荐工作流
行动前：

- `make validate-day DATE=2026-06-29`
- `make validate-links DATE=2026-06-29`
- `make validate-ready DATE=2026-06-29`
- `make render-day DATE=2026-06-29`

行动后：

- fill `validation_record.json`
- fill `revenue_signal.json` or `rejection_signal.json`
- update `alan_memory.json`
- `make validate-result DATE=2026-06-29`

`memory/alan_context.json` 保存 Alan 的长期个人上下文。每日文件夹可以放置 `alan_context.json` 覆盖当天上下文；如果不存在，渲染器会回退到 `memory/alan_context.json`。
