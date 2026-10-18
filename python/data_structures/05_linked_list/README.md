# 05 - Linked List: Add Two Numbers + Reverse Between

**Difficulty:** Medium | **Topics:** singly linked list, carry, pointer rewiring | **Target:** O(n) time, O(1) extra space for part B

`ListNode`, `from_list` and `to_list` are already written for you in `linked_list.py` (use them in your own experiments).

## Part A - Add Two Numbers

Two non-negative integers are stored as linked lists, **digits in reverse order** (least significant digit first).
Return their sum as a linked list in the same format.

```
342 + 465 = 807
[2,4,3] + [5,6,4] -> [7,0,8]
```

- Lists can have different lengths.
- Don't convert to an int and back; practice the carry.

## Part B - Reverse Linked List II

Reverse the nodes from position `left` to `right` (1-indexed, inclusive) in one pass and return the head.

```
[1,2,3,4,5], left=2, right=4  ->  [1,4,3,2,5]
```

## Constraints

- Part A: each list has `1..100` nodes, digits `0..9`, no leading zeros except the number 0 itself.
- Part B: `1 <= left <= right <= length`

## Hints

<details><summary>Hint 1 (A)</summary>Use a dummy head node and a `carry` variable. Loop while either list has nodes **or** carry is non-zero.</details>
<details><summary>Hint 2 (B)</summary>Use a dummy node before the head so `left == 1` is not a special case. Walk to the node before `left`, then repeatedly move the next node to the front of the reversed section.</details>
<details><summary>Careful</summary>`9999999 + 9999 = 10009998`: the final carry creates a brand-new node.</details>

## Run the tests

```bash
cd python/data_structures/05_linked_list
pytest -v
```
