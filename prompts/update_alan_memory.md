# 更新 AlanMemory

当 Alan 已经记录 ValidationRecord 和相关 signals 后，使用这个 prompt。

## Prompt
你正在帮助 Alan OS 从一个完成的手动验证循环中更新 AlanMemory（Alan 机会记忆）。

AlanMemory 应该改善未来 Today's Bet 的选择。它不应该变成模糊日记。

Inputs：

```text
[PASTE INFORMATION GAP, OPPORTUNITY, TODAYS BET, VALIDATION RECORD, REVENUE SIGNALS, REJECTION SIGNALS, AND CURRENT MEMORY NOTES]
```

返回一个 AlanMemory update，必须包含这些 English keys：

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

约束：

- 每一条 memory update 都必须绑定观察到的行为。
- 优先记录具体 buyer、channel、message、timing 和 offer lessons。
- 不要做没有执行证据支持的人格判断。
- 写清楚 rejection 或 silence 如何改变未来选择。
- 保持 update 对下一次选择 Today's Bet 有用。

最后用一句话结束：`Next time Alan should bias toward: ...`
