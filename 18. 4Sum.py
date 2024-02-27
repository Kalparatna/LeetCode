from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                a, b = j + 1, n - 1
                
                while a < b:
                    current_sum = nums[i] + nums[j] + nums[a] + nums[b]

                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[a], nums[b]])

                        while a < b and nums[a] == nums[a + 1]:
                            a += 1
                        while a < b and nums[b] == nums[b - 1]:
                            b -= 1

                        a += 1
                        b -= 1

                    elif current_sum < target:
                        a += 1
                    else:
                        b -= 1

        return result
