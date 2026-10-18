# Spoiler - bugs in `three_sum.py`

There are 4 planted bugs.

## Bug 1

Missing `i > 0`: at `i = 0` this compares with `nums[-1]` (the last element). Try `[0, 0, 0]` or `[-2, 0, 2, -2]`.

```diff
- if nums[i] == nums[i - 1]:
+ if i > 0 and nums[i] == nums[i - 1]:
```

## Bug 2

`list.sort()` sorts the caller's list in place - a hidden side effect. `sorted()` returns a copy.

```diff
- nums.sort()
+ nums = sorted(nums)
```

## Bug 3

`lo` must start *after* `i`; otherwise the same element is used twice. Try `[-2, 1, 4]`: it returns `[-2, -2, 4]`.

```diff
- lo, hi = i, n - 1
+ lo, hi = i + 1, n - 1
```

## Bug 4

`if` skips only ONE duplicate, `while` skips them all. Try `[-2, 0, 0, 0, 2, 2, 2]` - `[-2, 0, 2]` appears twice in the output.

```diff
- if lo < hi and nums[lo] == nums[lo - 1]:
+ while lo < hi and nums[lo] == nums[lo - 1]:
```
