# 手动验证循环 Runbook

## 目的
这个 runbook 说明 Alan 如何手动跑完一个 60 分钟 Alan OS 验证循环：

Signal（信号 / 原始线索） -> InformationGap（信息差） -> Opportunity（可变现机会） -> Today's Bet（今日唯一验证动作） -> ValidationPlan（验证计划） -> ValidationRecord（验证记录） -> RevenueSignal（收入信号）/RejectionSignal（拒绝信号） -> AlanMemory（Alan 机会记忆）。

重点不是收集更多信息，而是让 Alan 更快从信息差走到经过验证的收入信号。

## 时间盒
默认时间盒：60 分钟。

- 5 分钟：选择 Signals。
- 5 分钟：提炼一个 InformationGap。
- 5 分钟：创建一个 Opportunity。
- 10 分钟：选择 Today's Bet 并写出 ValidationPlan。
- 30 分钟：执行动作。
- 5 分钟：记录结果并更新 AlanMemory。

如果执行本身需要完整 60 分钟，就记录准备工作并安排下一次动作。不要把循环变成无限研究。

## 准备清单
开始前，Alan 应该准备好：

- 一个安静的 60 分钟时间块；
- 打开 `configs/source_registry.yaml`；
- 打开 `data/sample/` 作为样例；
- 准备好 Sprint 1 的五个 prompts；
- 一个保存本地 JSON records 的位置；
- 复查 `memory/alan_context.json` 中的当前约束；
- 一个可触达买家路径或 audience surface；
- 明确规则：本循环内不做产品开发。

## Step 1: 选择 Signals
从 source registry 中选择一到三个手动 Signals。

好的 Signals 通常包含：

- 一个具名 pain 或 workflow；
- 一个可触达 customer segment；
- 一个 timing clue；
- 一个可能的付费动作；
- 足够具体，可以联系真实的人。

避免只选择：

- 有趣链接；
- 宽泛趋势判断；
- 热度指标；
- 没有买家痛点的工具发布；
- Alan 今天无法行动的话题。

输出：每个有效观察对应一个 `signal` record。

## Step 2: 提炼 InformationGap
问自己：这些 Signals 暴露了什么暂时性错配？

使用这些问题：

- 谁最早知道或感受到这个问题？
- 谁需要这个 gap 被关闭？
- 为什么现在这个时间点重要？
- 什么会让窗口关闭？
- 什么会证明这不是一个真实 gap？

InformationGap 不是产品点子。它应该解释一个暂时的不对称优势。

输出：一个 `information_gap` record。

## Step 3: 创建一个 Opportunity
把 InformationGap 转成一个可触达客户愿意付费的解释。

定义：

- customer segment；
- buyer；
- pain；
- manual offer；
- revenue hypothesis；
- distribution path；
- lifecycle stage；
- riskiest assumption。

在软件之前，优先考虑 service、audit、teardown、consultation、review、script cleanup、buyer-language rewrite 等手动 offer。

输出：一个 `opportunity` record。

## Step 4: 选择 Today's Bet
Today's Bet 是 Alan 现在要做的唯一动作。

这个 bet 必须：

- 适合今天；
- 指向可触达的人；
- 小到可以立刻开始；
- 能产生 RevenueSignal 或 RejectionSignal；
- 包含 give-up rule；
- 避免构建软件。

如果有多个可能 bet，选择离真实买家回应最近的那个。

输出：一个 `todays_bet` record。

## Step 5: 执行 ValidationPlan
把 Today's Bet 转成具体计划。

包含：

- target count；
- channels；
- action steps；
- message 或 offer script；
- timebox；
- success threshold；
- give-up rule；
- risk notes。

然后执行动作。发消息、发布 offer、询问买家、请求 call，或提供付费手动服务。

不要润色。不要构建。动作清楚后不要继续研究。

输出：执行前一个 `validation_plan` record。

## Step 6: 记录 Validation
执行后立刻记录发生了什么。

捕捉：

- actions taken；
- people contacted；
- responses；
- silence；
- objections；
- outcome；
- lesson；
- next action；
- time spent。

沉默是数据。拒绝是数据。困惑回复也是数据。

输出：一个 `validation_record` record。

## Step 7: 记录 RevenueSignals 和 RejectionSignals
RevenueSignals 是真实人可能付费、已经付费或更接近付款的证据。

例子：

- booked call；
- budget-confirming reply；
- paid pilot；
- deposit；
- referral to a buyer；
- direct request for a paid service。

RejectionSignals 是 offer、segment、timing、price、buyer 或 pain 不成立的证据。

例子：

- no response；
- not urgent；
- no budget；
- wrong buyer；
- already solved；
- price objection；
- timing objection；
- scope mismatch。

输出：一个或多个 `revenue_signal` 和 `rejection_signal` records。

## Step 8: 更新 AlanMemory
写下下一次选择应该如何改变。

更新：

- validated patterns；
- rejected patterns；
- strong segments；
- weak segments；
- MoneyDNA notes；
- weekly revenue signals；
- next biases。

Memory update 必须改变未来选择。如果它不能改变下一次 bet，说明它太模糊。

输出：当前周或 review period 的一个 `alan_memory` update。

## 不要做什么
- 不要构建 collectors。
- 不要构建 analyzers。
- 不要构建 automation。
- 不要创建 database。
- 不要创建 UI。
- 不要添加 external integrations。
- 不要把循环变成 SaaS workflow。
- 不要追新闻摘要。
- 不要选择多个 Today's Bets。
- 不要在 buyer validation 前构建 product artifacts。
- 不要忽略拒绝或沉默。

## 完成标准
一个手动循环完成时，Alan 至少拥有：

- 至少一个 Signal；
- 一个 InformationGap；
- 一个 Opportunity；
- 一个 Today's Bet；
- 一个 ValidationPlan；
- 一个 ValidationRecord；
- 至少一个 RevenueSignal 或 RejectionSignal；
- 一个 AlanMemory update；
- 一个具体的 future selection bias。
