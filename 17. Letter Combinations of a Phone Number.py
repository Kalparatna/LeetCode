class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        nums = {'2':'abc' ,
                     '3':'def',
                    '4':'ghi',
                    '5':'jkl',
                    '6':'mno',
                    '7':'pqrs',
                    '8':'tuv',
                    '9':'wxyz'}

        def backtrack(i, curstr):
            if len(curstr) == len(digits):
                output.append(curstr)
                return

            for j in nums[digits[i]]:
                backtrack(i+1, curstr+j)
                
        if digits:
            backtrack(0, "")

        return output
    


        
