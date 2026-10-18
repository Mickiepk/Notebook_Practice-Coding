# Debug 05 - Subsets II (with duplicates)

**Difficulty:** Medium | **Topics:** backtracking, de-duplication

## The problem the code is supposed to solve

Given a list `nums` that may contain **duplicates**, return all possible **unique** subsets (the power set without repeats).
Order of subsets and order inside a subset does not matter to the tests.

| Input        | Output                                                |
|--------------|-------------------------------------------------------|
| `[1,2,2]`    | `[[], [1], [1,2], [1,2,2], [2], [2,2]]`               |
| `[0]`        | `[[], [0]]`                                           |
| `[]`         | `[[]]`                                                |

A list with `n` distinct values has `2^n` subsets.

## How to practice

1. **Read** `subsets_dup.py` without running anything. It looks reasonable, but it is wrong.
2. Write your findings in a copy of `../REVIEW_TEMPLATE.md` (line number, what is wrong, an input that breaks it).
3. **Run** `pytest -v` to confirm which of your guesses were real.
4. **Fix** the code until every test passes.
5. Only then open `SPOILER_answer.md` and compare.

```bash
cd python/code_debug/05_subsets_with_dup
pytest -v
```
