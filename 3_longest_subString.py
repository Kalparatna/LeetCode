'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring
 without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        str_len = len(s)
        char_index_map = {}
        start = 0
        max_length = 0

        for i in range(str_len):
            if s[i] in char_index_map and char_index_map[s[i]] >= start:
                start = char_index_map[s[i]] + 1

            char_index_map[s[i]] = i
            current_length = i - start + 1
            max_length = max(max_length, current_length)

        return max_length

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    input_string = input()
    result = solution.lengthOfLongestSubstring(input_string)
    print(f"The length of the longest substring without repeating characters in '{input_string}' is: {result}")
