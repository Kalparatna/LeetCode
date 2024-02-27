class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenstr = len(haystack)
        lenndl = len(needle)
        for i in range(lenstr-lenndl+1):
            if haystack[i:i+lenndl] == needle:
                return i
        return -1

        
