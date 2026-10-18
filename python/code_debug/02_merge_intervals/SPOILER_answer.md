# Spoiler - bugs in `merge_intervals.py`

There are 4 planted bugs.

## Bug 1

The intervals are never sorted, so overlapping intervals that are not adjacent in the input are missed. Try `[[8,10],[1,3],[2,6]]`.

```diff
- intervals = list(intervals)
+ intervals = sorted(intervals, key=lambda x: x[0])
```

## Bug 2

Touching intervals like `[1,4]` and `[4,5]` should merge; strict `<` keeps them separate.

```diff
- if start < last[1]:
+ if start <= last[1]:
```

## Bug 3

When an interval is fully contained in the previous one (`[1,10]`, `[2,3]`) the merged end must not shrink - take the `max`.

```diff
- last[1] = end
+ last[1] = max(last[1], end)
```

## Bug 4

Aliasing: `merged[0]` is the caller's own inner list, so `last[1] = ...` silently mutates the input. Copy it.

```diff
- merged = [intervals[0]]
+ merged = [list(intervals[0])]
```
