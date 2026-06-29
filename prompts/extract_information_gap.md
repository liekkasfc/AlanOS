# Extract InformationGap

Use this prompt after Alan has manually selected one to three Signals.

## Prompt
You are helping Alan OS run a manual revenue validation loop.

Alan OS is a personal revenue operating system, not a news aggregator. Your job is to extract one InformationGap that can help Alan reach a validated revenue signal faster.

Given these Signals:

```text
[PASTE SIGNAL SUMMARIES, RAW CLAIMS, SOURCE NOTES, AND TAGS]
```

Return one InformationGap with:

- `name`
- `description`
- `evidence_signal_ids`
- `who_has_the_gap`
- `who_needs_the_gap_closed`
- `why_now`
- `window_start`
- `window_risk`
- `confidence`
- `status`
- `notes`

Constraints:

- Do not call a tool, article, or trend an InformationGap.
- Do not propose a product yet.
- Name the buyer or market side that would care.
- Preserve contradictions or missing facts.
- Stop after one best InformationGap.

End with one sentence: `The fastest validation path is likely: ...`
