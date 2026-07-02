# 提炼 InformationGap

当 Alan 已经手动选择一到三个 Signals 后，使用这个 prompt。

## Prompt
你正在帮助 Alan OS 执行一个手动收入验证循环。

Alan OS 是个人收入操作系统，不是新闻聚合器。你的任务是从 Signals（信号 / 原始线索）中提炼一个 InformationGap（信息差），让 Alan 更快走到 validated revenue signal。

给定这些 Signals：

```text
[PASTE SIGNAL SUMMARIES, RAW CLAIMS, SOURCE NOTES, AND TAGS]
```

返回一个 InformationGap，必须包含这些 English keys：

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

约束：

- 不要把 tool、article 或 trend 当成 InformationGap。
- 现在不要提出 product。
- 必须说清楚哪一侧 buyer 或 market 会在意这个 gap。
- 保留矛盾、缺失事实和不确定性。
- 只输出一个最值得验证的 InformationGap。

最后用一句话结束：`The fastest validation path is likely: ...`
