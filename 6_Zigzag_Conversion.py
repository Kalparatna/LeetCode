'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

'''

class Solution:
    def convert(self, s: str, Rows: int) -> str:

        if Rows == 1 or  Rows >= len(s):
            return s
        
        List = [''] * Rows

        index = 0
        step = 1

        for i in s:
            List[index] += i

            if index == 0:
                step = 1
            elif index == Rows - 1:
                step = -1

            index += step

        return  "".join(List)
            

obj = Solution()

Str = input("Enter the String: ")
Rows = int(input("Enter No of Rows: "))

Output = obj.convert(Str, Rows)
print(Output)
        
