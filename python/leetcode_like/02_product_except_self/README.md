# 02 - Product of Array Except Self

**Difficulty:** Medium | **Topics:** array, prefix / suffix | **Target:** O(n) time, no division

## Problem

Given an integer list `nums`, return a list `answer` where `answer[i]` is the product of **all elements of `nums` except `nums[i]`**.

- You must **not use division**.
- Do not modify `nums`.

## Examples

| Input              | Output              |
|--------------------|---------------------|
| `[1, 2, 3, 4]`     | `[24, 12, 8, 6]`    |
| `[-1, 1, 0, -3, 3]`| `[0, 0, 9, 0, 0]`   |

## Constraints

- `2 <= len(nums) <= 10^5`
- Values fit in a normal Python `int`; the product may be huge, that is fine.

## Hints

<details><summary>Hint 1</summary>`answer[i] = (product of everything left of i) * (product of everything right of i)`.</details>
<details><summary>Hint 2</summary>Two passes: one left-to-right, one right-to-left. Can you reuse the output list so extra space is O(1)?</details>
<details><summary>Careful</summary>Zeros: one zero and two zeros behave differently. Prefix/suffix handles both for free, division does not.</details>

## Run the tests

```bash
cd python/leetcode_like/02_product_except_self
pytest -v
```
