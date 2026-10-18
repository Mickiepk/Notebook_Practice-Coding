# 05 - Top K Frequent Elements

**Difficulty:** Medium | **Topics:** hash map, heap, bucket sort | **Target:** better than O(n log n)

## Problem

Given an integer list `nums` and an integer `k`, return the `k` most frequent elements.
The answer may be in **any order**. The tests guarantee the answer is unique (no ties at the cut-off).

## Examples

| nums                    | k | Output     |
|-------------------------|---|------------|
| `[1,1,1,2,2,3]`        | 2 | `[1, 2]`   |
| `[1]`                   | 1 | `[1]`      |

## Constraints

- `1 <= k <= number of distinct elements`
- `1 <= len(nums) <= 10^5`, values can be negative.

## Hints

<details><summary>Hint 1</summary>Count with a dict (or `collections.Counter`).</details>
<details><summary>Hint 2</summary>Option A: a min-heap of size `k` -> O(n log k). Option B: bucket sort where index = frequency -> O(n).</details>

## Bonus

Solve it twice: once with `heapq`, once with bucket sort, without calling `Counter.most_common`.

## Run the tests

```bash
cd python/leetcode_like/05_top_k_frequent
pytest -v
```
