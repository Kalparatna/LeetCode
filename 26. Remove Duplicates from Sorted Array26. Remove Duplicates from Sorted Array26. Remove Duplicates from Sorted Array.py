class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lennums = len(nums)

        if lennums <= 1:
           return lennums

        i = 0

        for j in range(1, lennums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i+1
