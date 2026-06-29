# Generate Opportunity

Use this prompt after Alan has one InformationGap.

## Prompt
You are helping Alan OS turn an InformationGap into one manual-first Opportunity.

Alan OS is not a SaaS-first system. The Opportunity must be validated with real people before product development.

InformationGap:

```text
[PASTE INFORMATION GAP RECORD]
```

Alan Context:

```text
[PASTE RELEVANT SKILLS, NETWORK, CREDIBILITY, CONSTRAINTS, AND ANTI-PATTERNS]
```

Return one Opportunity with:

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

Constraints:

- Prefer a manual service, audit, teardown, review, consultation, or buyer-language rewrite.
- Do not require software, automation, a database, or a UI.
- Do not generate multiple opportunities unless the first one is invalid.
- Make the money hypothesis explicit.
- Explain why Alan can reach this buyer now.

End with one sentence: `The riskiest assumption to test today is: ...`
