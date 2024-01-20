'''
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        merged_list = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged_list += [nums1[i]]
                i += 1
            else:
                merged_list += [nums2[j]]
                j += 1
                
        merged_list += nums1[i:]
        merged_list += nums2[j:]

        len_of_merge = len(merged_list)
        mid = len_of_merge // 2

        if len_of_merge % 2 == 0:
            return (merged_list[mid - 1] + merged_list[mid]) / 2
        else:
            return merged_list[mid]
