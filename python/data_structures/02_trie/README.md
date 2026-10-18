# 02 - Trie (Prefix Tree)

**Difficulty:** Medium | **Topics:** tree, hash map, strings | **Target:** O(L) per operation (L = word length)

## Problem

Implement a `Trie` that stores lowercase words.

| Method                   | Meaning                                                              |
|--------------------------|----------------------------------------------------------------------|
| `insert(word)`           | add a word (inserting twice is fine)                                 |
| `search(word)`           | `True` only if exactly this word was inserted                        |
| `starts_with(prefix)`    | `True` if any inserted word begins with `prefix` (`""` -> `True` if trie is non-empty) |
| `words_with_prefix(p)`   | all inserted words that start with `p`, **sorted alphabetically**   |
| `count_words()`          | number of **distinct** words stored                                  |

## Example

```python
t = Trie()
t.insert("apple")
t.search("apple")      # True
t.search("app")        # False  (only a prefix)
t.starts_with("app")   # True
t.insert("app")
t.search("app")        # True
```

## Hints

<details><summary>Hint 1</summary>Each node = a dict `char -> child` plus a boolean `is_end`.</details>
<details><summary>Hint 2</summary>`search` and `starts_with` share one helper: walk down the prefix and return the final node (or `None`).</details>
<details><summary>Hint 3</summary>`words_with_prefix`: walk to the prefix node, then DFS below it collecting words. Walk children in sorted order for sorted output.</details>

## Run the tests

```bash
cd python/data_structures/02_trie
pytest -v
```
