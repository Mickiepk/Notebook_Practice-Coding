# Debug 02 - Merge Intervals

**Difficulty:** Medium | **Topics:** sorting, intervals

## The problem the code is supposed to solve

Given a list of closed intervals `[start, end]`, merge all overlapping intervals and return the result sorted by start.
Intervals that **touch** (`[1,4]` and `[4,5]`) count as overlapping.
The input list must **not be modified**.

| Input                              | Output            |
|------------------------------------|-------------------|
| `[[1,3],[2,6],[8,10],[15,18]]`     | `[[1,6],[8,10],[15,18]]` |
| `[[1,4],[4,5]]`                    | `[[1,5]]`         |
| `[[1,10],[2,3]]`                   | `[[1,10]]`        |

## How to practice

1. **Read** `merge_intervals.py` without running anything. It looks reasonable, but it is wrong.
2. Write your findings in a copy of `../REVIEW_TEMPLATE.md` (line number, what is wrong, an input that breaks it).
3. **Run** `pytest -v` to confirm which of your guesses were real.
4. **Fix** the code until every test passes.
5. Only then open `SPOILER_answer.md` and compare.

```bash
cd python/code_debug/02_merge_intervals
pytest -v
```
