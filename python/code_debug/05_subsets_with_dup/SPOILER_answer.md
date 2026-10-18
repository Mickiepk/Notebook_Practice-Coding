# Spoiler - bugs in `subsets_dup.py`

There are 4 planted bugs.

## Bug 1

Appends a reference to the one shared `path` list, which is emptied again by `pop()`. Every stored subset ends up as `[]`. Copy it.

```diff
- result.append(path)
+ result.append(path[:])
```

## Bug 2

The duplicate check must compare against `start`, not `0`. With `i > 0` you also skip a duplicate that is legitimately the *next element of the same path* (e.g. `[1,2,2]` is lost).

```diff
- if i > 0 and nums[i] == nums[i - 1]:
+ if i > start and nums[i] == nums[i - 1]:
```

## Bug 3

Recursing with `start + 1` instead of `i + 1` revisits elements and builds wrong subsets such as `[2, 2]` from a single 2.

```diff
- backtrack(start + 1, path)
+ backtrack(i + 1, path)
```

## Bug 4

Without sorting, equal values are not adjacent, so the `nums[i] == nums[i-1]` de-duplication fails. Try `[2, 1, 2]`.

```diff
- nums = list(nums)
+ nums = sorted(nums)
```
