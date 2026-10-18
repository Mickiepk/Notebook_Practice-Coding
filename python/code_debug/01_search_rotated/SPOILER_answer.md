# Spoiler - bugs in `search_rotated.py`

There are 4 planted bugs.

## Bug 1

`hi` starts one past the last index while the loop uses `lo <= hi`, so `nums[mid]` can read out of range (`IndexError`). Try `search([1], 2)`.

```diff
- lo, hi = 0, len(nums)
+ lo, hi = 0, len(nums) - 1
```

## Bug 2

When `lo == mid` (a one- or two-element window) the left half is a single sorted element, but `<` sends us to the 'right half is sorted' branch. Try `search([3, 1], 1)`.

```diff
- if nums[lo] < nums[mid]:
+ if nums[lo] <= nums[mid]:
```

## Bug 3

The target may equal `nums[lo]`; the lower bound must be inclusive. Try `search([4,5,6,7,0,1,2], 4)`.

```diff
- if nums[lo] < target < nums[mid]:
+ if nums[lo] <= target < nums[mid]:
```

## Bug 4

The target may equal `nums[hi]`; the upper bound must be inclusive. Try `search([5, 1, 3], 3)`.

```diff
- if nums[mid] < target < nums[hi]:
+ if nums[mid] < target <= nums[hi]:
```
