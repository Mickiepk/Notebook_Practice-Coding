def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    nums = list(nums)
    result = []

    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(start + 1, path)
            path.pop()

    backtrack(0, [])
    return result
