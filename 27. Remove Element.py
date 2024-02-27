from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lennums = len(nums)
        result = []

        for i in range(lennums):
            if val != nums[i]:
                result.append(nums[i])

        nums[:len(result)] = result

        return len(result)
