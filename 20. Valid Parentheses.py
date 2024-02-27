class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = { ")": "(",  "]":"[", "}":"{" }
        stk = []

        for i in s:
            if i in dictionary:
                if stk and stk[-1]==dictionary[i]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(i)
        return not stk


        
