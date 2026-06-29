# Update AlanMemory

Use this prompt after Alan records a ValidationRecord and related signals.

## Prompt
You are helping Alan OS update AlanMemory from one completed manual validation loop.

AlanMemory should improve future Today's Bet selection. It should not become vague journaling.

Inputs:

```text
[PASTE INFORMATION GAP, OPPORTUNITY, TODAYS BET, VALIDATION RECORD, REVENUE SIGNALS, REJECTION SIGNALS, AND CURRENT MEMORY NOTES]
```

Return one AlanMemory update with:

- `period`
- `validated_patterns`
- `rejected_patterns`
- `strong_segments`
- `weak_segments`
- `money_dna_updates`
- `weekly_revenue_signals`
- `lessons`
- `next_biases`
- `confidence`
- `status`

Constraints:

- Tie every memory update to observed behavior.
- Prefer specific buyer, channel, message, timing, and offer lessons.
- Do not make personality claims unless execution evidence supports them.
- Include how rejection or silence changes future selection.
- Keep the update useful for choosing the next Today's Bet.

End with one sentence: `Next time Alan should bias toward: ...`
