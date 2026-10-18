# 03 - Coin Change

**Difficulty:** Medium | **Topics:** dynamic programming | **Target:** O(amount * len(coins)) time

## Problem

You have coins of different denominations (unlimited supply of each) and a total `amount`.
Return the **fewest number of coins** needed to make exactly `amount`, or `-1` if it is impossible.

## Examples

| coins          | amount | Output | Why                          |
|----------------|--------|--------|------------------------------|
| `[1, 2, 5]`    | `11`   | `3`    | 5 + 5 + 1                    |
| `[2]`          | `3`    | `-1`   | cannot make an odd amount    |
| `[1]`          | `0`    | `0`    | nothing to pay               |

## Constraints

- `1 <= len(coins) <= 12`, `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

## Hints

<details><summary>Hint 1</summary>`dp[a]` = fewest coins to make amount `a`. What is `dp[0]`?</details>
<details><summary>Hint 2</summary>`dp[a] = min(dp[a - c] + 1)` over coins `c <= a`. What should "unreachable" look like in the table?</details>
<details><summary>Careful</summary>Greedy (always take the biggest coin) is wrong: `coins=[1,3,4], amount=6` needs 2 coins (3+3), not 3 (4+1+1).</details>

## Run the tests

```bash
cd python/leetcode_like/03_coin_change
pytest -v
```
