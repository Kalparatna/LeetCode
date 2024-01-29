'''
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()   
        closest_sum = float('inf')  
        min_diff = float('inf')

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                cur_diff = abs(cur_sum - target)  

                if cur_diff < min_diff:
                    min_diff = cur_diff
                    closest_sum = cur_sum

                if cur_sum < target:
                    j += 1
                elif cur_sum > target:
                    k -= 1
                else:
                    return closest_sum  
        return closest_sum

Obj = Solution()
L = list(map(int, input().split()))
target = int(input())
Obj.threeSumClosest(L, target)
