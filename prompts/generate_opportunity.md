# 生成 Opportunity

当 Alan 已经有一个 InformationGap 后，使用这个 prompt。

## Prompt
你正在帮助 Alan OS 把一个 InformationGap（信息差）转成一个 manual-first Opportunity（可变现机会）。

Alan OS 不是 SaaS-first system。Opportunity 必须先用真实的人验证，再考虑产品开发。

InformationGap：

```text
[PASTE INFORMATION GAP RECORD]
```

Alan Context：

```text
[PASTE RELEVANT SKILLS, NETWORK, CREDIBILITY, CONSTRAINTS, AND ANTI-PATTERNS]
```

返回一个 Opportunity，必须包含这些 English keys：

- `information_gap_id`
- `customer_segment`
- `buyer`
- `pain`
- `offer`
- `revenue_hypothesis`
- `distribution_path`
- `lifecycle_stage`
- `pricing_guess`
- `riskiest_assumption`
- `confidence`
- `status`

约束：

- 优先选择 manual service、audit、teardown、review、consultation 或 buyer-language rewrite。
- 不要要求 software、automation、database 或 UI。
- 除非第一个机会无效，否则不要生成多个 opportunities。
- 明确 money hypothesis。
- 说明 Alan 为什么现在能触达这个 buyer。

最后用一句话结束：`The riskiest assumption to test today is: ...`
