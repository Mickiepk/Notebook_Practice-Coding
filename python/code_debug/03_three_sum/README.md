# Debug 03 - 3Sum

**Difficulty:** Medium | **Topics:** sorting, two pointers, de-duplication

## The problem the code is supposed to solve

Return all **unique** triplets `[a, b, c]` from `nums` such that `a + b + c == 0`.

- Each element may be used at most once per triplet (by position).
- No duplicate triplets in the result.
- Each triplet should be in ascending order and the result in ascending order (the tests sort the result before comparing, so order of triplets does not matter).
- The input list must not be modified.

| Input                   | Output                       |
|-------------------------|------------------------------|
| `[-1,0,1,2,-1,-4]`      | `[[-1,-1,2],[-1,0,1]]`       |
| `[0,1,1]`               | `[]`                         |
| `[0,0,0]`               | `[[0,0,0]]`                  |

## How to practice

1. **Read** `three_sum.py` without running anything. It looks reasonable, but it is wrong.
2. Write your findings in a copy of `../REVIEW_TEMPLATE.md` (line number, what is wrong, an input that breaks it).
3. **Run** `pytest -v` to confirm which of your guesses were real.
4. **Fix** the code until every test passes.
5. Only then open `SPOILER_answer.md` and compare.

```bash
cd python/code_debug/03_three_sum
pytest -v
```
