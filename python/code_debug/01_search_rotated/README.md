# Debug 01 - Search in Rotated Sorted Array

**Difficulty:** Medium | **Topics:** binary search

## The problem the code is supposed to solve

A sorted list of **distinct** integers was rotated at an unknown pivot (`[0,1,2,4,5,6,7]` -> `[4,5,6,7,0,1,2]`).
`search(nums, target)` must return the **index** of `target`, or `-1` if absent, in **O(log n)**.

| nums                  | target | expected |
|-----------------------|--------|----------|
| `[4,5,6,7,0,1,2]`     | `0`    | `4`      |
| `[4,5,6,7,0,1,2]`     | `3`    | `-1`     |
| `[1]`                 | `0`    | `-1`     |

The idea in the code (decide which half is sorted, then check if the target is inside it) is correct.
The **implementation details** are not.

## How to practice

1. **Read** `search_rotated.py` without running anything. It looks reasonable, but it is wrong.
2. Write your findings in a copy of `../REVIEW_TEMPLATE.md` (line number, what is wrong, an input that breaks it).
3. **Run** `pytest -v` to confirm which of your guesses were real.
4. **Fix** the code until every test passes.
5. Only then open `SPOILER_answer.md` and compare.

```bash
cd python/code_debug/01_search_rotated
pytest -v
```
