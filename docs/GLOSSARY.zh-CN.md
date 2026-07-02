# Alan OS 术语表

这个术语表用于帮助 Alan 用中文操作 Alan OS，同时保持英文技术契约稳定。JSON keys、schema entity names、enum values、目录名和命令名仍然使用英文。

| Term | 中文 | 说明 |
| --- | --- | --- |
| Signal | 信号 / 观察到的原始线索 | Alan 从真实世界手动看到的痛点、变化、买家行为或反常现象。 |
| InformationGap | 信息差 | 一段暂时存在的不对称认知、执行或供需缺口。 |
| Opportunity | 可变现机会 | 把 InformationGap 翻译成某个真实买家可能愿意付费解决的问题。 |
| Today's Bet | 今日唯一验证动作 | Alan 今天只做一个最短路径动作，用来产生 RevenueSignal 或 RejectionSignal。 |
| ValidationPlan | 验证计划 | 执行 Today's Bet 的具体计划，包括目标人数、渠道、脚本、成功阈值和放弃规则。 |
| ValidationRecord | 验证记录 | Alan 行动之后对动作、回复、沉默、结果、教训和耗时的记录。 |
| RevenueSignal | 收入信号 | 真实人更接近付款的证据，例如 booked call、预算确认、付费请求、deposit、paid pilot 或 buyer referral。 |
| RejectionSignal | 拒绝信号 | 真实人不买、不急、没预算、找错买家、时机不对或沉默的证据。 |
| AlanMemory | Alan 机会记忆 | Alan 从验证结果中积累的选择偏好、强弱 segment、教训和下一次下注方向。 |
| MoneyDNA | Alan 赚钱适配基因 | 用来描述某个机会是否适合 Alan 的技能、渠道、可信度、执行速度和现金流约束。 |
| Give-up Rule | 放弃规则 | 何时停止、跟进、转向或记录 RejectionSignal 的明确规则。 |
| Expected Signal | 预期信号 | 执行 Today's Bet 后希望观察到的收入或拒绝证据。 |

## 使用原则
- 面向 Alan 的说明可以使用中文。
- Schema/entity names 保持英文，例如 `todays_bet.json`、`ValidationPlan`、`RevenueSignal`。
- JSON keys 保持英文，例如 `expected_signal`、`give_up_rule`、`target_personas`。
- 命令保持不变，例如 `make validate-ready DATE=2026-06-29`。
