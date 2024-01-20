'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

'''
import math
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            Reverse = int(str(x)[:: -1])
        else:
            Reverse = -(int(str(abs(x))[::-1]))
        
        if Reverse <  -2**31 or Reverse > 2**31-1:
            return 0
        else:
            return Reverse


obj = Solution()
Number = int(input("Enter the NUmber: "))
print(obj.reverse(Number))



        