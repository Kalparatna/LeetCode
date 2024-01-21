'''
8. String to Integer (atoi)
Medium
Topics
Companies
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
 

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        Negative = False
        Integer = 0

        if s[0] == "-":
            Negative = True
        elif s[0] == "+":
            Negative = False
        elif not s[0].isnumeric():
            return 0
        else:
            Integer = ord(s[0]) - ord("0")

        for i in range(1, len(s)):
            if s[i].isnumeric():
                Integer = Integer * 10 + (ord(s[i]) - ord("0"))
                if not Negative and Integer >= 2**(31) - 1:
                    return 2**(31) - 1
                if Negative and Integer >= 2**(31):
                    return -2**(31)
            else:
                break

        if not Negative:
            return Integer
        else:
            return -Integer


obj = Solution()
STR = input("Enter the Number: ")
obj.myAtoi(STR)