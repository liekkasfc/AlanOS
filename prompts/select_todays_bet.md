# Select Today's Bet

Use this prompt after Alan has one Opportunity.

## Prompt
You are helping Alan OS choose Today's Bet.

Today's Bet is the most important daily output. It is one action Alan can execute today to produce a RevenueSignal or RejectionSignal.

Opportunity:

```text
[PASTE OPPORTUNITY RECORD]
```

Available Alan Context:

```text
[PASTE AVAILABLE TIME, REACHABLE PEOPLE, CHANNELS, AND CONSTRAINTS]
```

Return one Today's Bet with:

- `opportunity_id`
- `date`
- `action`
- `target_personas`
- `timebox_minutes`
- `expected_signal`
- `give_up_rule`
- `success_criteria`
- `script_id`
- `notes`
- `confidence`
- `status`

Constraints:

- Select exactly one bet.
- The action must fit within 60 minutes.
- The action must contact or observe real buyers or referrers.
- The action must not require product development.
- The expected signal must be closer to revenue than attention.
- Include what rejection or silence would teach Alan.

End with one sentence: `Do this before any further research: ...`
