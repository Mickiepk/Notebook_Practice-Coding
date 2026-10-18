# 01 - Longest Substring Without Repeating Characters

**Difficulty:** Medium | **Topics:** sliding window, hash map | **Target:** O(n) time

## Problem

Given a string `s`, return the length of the longest substring that contains **no repeated characters**.

A substring is contiguous (`"pwke"` is *not* a substring of `"pwwkew"`; `"wke"` is).

## Examples

| Input        | Output | Why                                  |
|--------------|--------|--------------------------------------|
| `"abcabcbb"` | `3`    | `"abc"`                              |
| `"bbbbb"`    | `1`    | `"b"`                                |
| `"pwwkew"`   | `3`    | `"wke"`                              |
| `""`         | `0`    | empty string                         |

## Constraints

- `0 <= len(s) <= 5 * 10^5`
- `s` may contain letters, digits, symbols and spaces.

## Hints

<details><summary>Hint 1</summary>Keep a window `[left, right]` that is always valid. Move `right` one step at a time.</details>
<details><summary>Hint 2</summary>When `s[right]` was already seen *inside the window*, where must `left` jump to? Store the last index of each character.</details>
<details><summary>Careful</summary>`"abba"` is the classic trap: `left` must never move backwards.</details>

## Run the tests

```bash
cd python/leetcode_like/01_longest_substring
pytest -v
```
