# Python Practice

Hands-on Python practice with a LeetCode-like feel: every problem has a README, a skeleton to fill in, and a pytest file that tells you if you are right.

## Setup (once)

```bash
cd python
python3 -m venv .venv && source .venv/bin/activate   # optional but recommended
pip install -r requirements.txt
```

Python 3.10+ is required.

## Three kinds of practice

| Folder | What you do | Files in each problem |
|--------|-------------|-----------------------|
| `leetcode_like/` | Solve a classic algorithm problem from scratch | `README.md`, `<name>.py` (skeleton), `test_<name>.py` |
| `data_structures/` | Implement a data structure / design a class | same as above |
| `code_debug/` | **Code review practice.** A solution is given but it is subtly wrong. Find the bugs by reading, then confirm with tests | `README.md`, `<name>.py` (buggy), `test_<name>.py`, `SPOILER_answer.md` |

For `code_debug/` see `code_debug/REVIEW_TEMPLATE.md` for a note-taking checklist.

## Workflow

```bash
cd python/leetcode_like/01_longest_substring
cat README.md              # read the problem
# edit longest_substring.py
pytest -v                  # run the tests for this problem only
```

Useful commands (from the `python/` folder):

```bash
pytest leetcode_like                      # all algorithm problems
pytest data_structures                    # all data structure problems
pytest code_debug                         # all debug problems (they FAIL until you fix them)
pytest leetcode_like/03_coin_change -v    # a single problem
pytest -x                                 # stop at first failure
pytest -k "edge"                          # run tests matching a name
```

Every skeleton starts by raising `NotImplementedError`, so a fresh problem is red until you solve it.

## Problem list

### leetcode_like (medium)
1. `01_longest_substring` - sliding window
2. `02_product_except_self` - prefix / suffix products
3. `03_coin_change` - dynamic programming
4. `04_number_of_islands` - grid DFS / BFS
5. `05_top_k_frequent` - hash map + heap / bucket sort

### data_structures (medium)
1. `01_lru_cache` - hash map + doubly linked list
2. `02_trie` - prefix tree
3. `03_min_heap` - array-backed heap, heapify, heap sort
4. `04_union_find` - DSU + redundant connection
5. `05_linked_list` - add two numbers, reverse between

### code_debug (find the bugs)
1. `01_search_rotated` - binary search
2. `02_merge_intervals` - sorting / aliasing
3. `03_three_sum` - two pointers / de-duplication
4. `04_grid_shortest_path` - BFS
5. `05_subsets_with_dup` - backtracking

## Progress tracker

Copy this and tick as you go.

| Problem | Solved | Date | Notes (what tripped me up) |
|---------|--------|------|----------------------------|
| lc 01 |  |  |  |
| lc 02 |  |  |  |
| lc 03 |  |  |  |
| lc 04 |  |  |  |
| lc 05 |  |  |  |
| ds 01 |  |  |  |
| ds 02 |  |  |  |
| ds 03 |  |  |  |
| ds 04 |  |  |  |
| ds 05 |  |  |  |
| debug 01 |  |  |  |
| debug 02 |  |  |  |
| debug 03 |  |  |  |
| debug 04 |  |  |  |
| debug 05 |  |  |  |

## Tips

- Time-box yourself (25-30 minutes per medium problem) before looking at hints.
- Write down the complexity of your solution before running the tests.
- For debug problems, list suspects **before** running pytest. Scoring yourself on "found by reading" vs "found by tests" is the actual exercise.
