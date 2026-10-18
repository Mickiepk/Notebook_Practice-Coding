# 03 - Build a Min-Heap

**Difficulty:** Medium | **Topics:** heap, array representation of a tree | **Target:** push/pop O(log n), peek O(1), heapify O(n)

## Problem

Implement your own binary min-heap **without** using `heapq`.

| Method / function      | Meaning                                                         |
|------------------------|-----------------------------------------------------------------|
| `push(x)`              | insert a value                                                  |
| `pop()`                | remove and return the smallest value; `IndexError` if empty     |
| `peek()`               | return the smallest value without removing; `IndexError` if empty |
| `len(heap)`            | number of items                                                 |
| `MinHeap.heapify(lst)` | classmethod: build a heap from a list in **O(n)** (do not call `push` n times) |
| `heap_sort(lst)`       | return a new sorted list using your heap                        |

## Index math (0-based array)

```
parent(i) = (i - 1) // 2
left(i)   = 2 * i + 1
right(i)  = 2 * i + 2
```

## Hints

<details><summary>Hint 1</summary>`push`: append at the end, then sift **up** while smaller than parent.</details>
<details><summary>Hint 2</summary>`pop`: save the root, move the last item to the root, then sift **down** swapping with the *smaller* child.</details>
<details><summary>Hint 3</summary>`heapify`: sift down every non-leaf node, starting from index `n // 2 - 1` going to 0.</details>
<details><summary>Careful</summary>Popping when only one item is left, and nodes that have only a left child.</details>

## Run the tests

```bash
cd python/data_structures/03_min_heap
pytest -v
```
