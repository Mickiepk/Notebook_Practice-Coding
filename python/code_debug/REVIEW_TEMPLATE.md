# Code review notes - <problem name>

Copy this file next to the problem (e.g. `REVIEW.md`) and fill it in **before** running the tests.

## 1. What should the code do? (one sentence, in your own words)


## 2. Suspects

| # | Line | What looks wrong | Input that would break it | Confidence (low/med/high) |
|---|------|------------------|---------------------------|---------------------------|
| 1 |      |                  |                           |                           |
| 2 |      |                  |                           |                           |
| 3 |      |                  |                           |                           |

## 3. Edge-case checklist

- [ ] empty input
- [ ] single element
- [ ] duplicates
- [ ] negative numbers / zero
- [ ] first and last index (off-by-one)
- [ ] inclusive vs exclusive bounds (`<` vs `<=`)
- [ ] does it mutate the caller's input?
- [ ] aliasing: is a list/dict shared when it should be copied?
- [ ] big input: is it fast enough? any recursion depth problem?

## 4. After running pytest

- Bugs I found by reading:
- Bugs only the tests revealed:
- Bugs I missed that I should look for next time:
