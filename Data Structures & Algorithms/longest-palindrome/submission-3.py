class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = set()
        res = 0
        for i in s:
            if i in count:
                count.remove(i)
                res += 2
            else:
                count.add(i)
        
        #odd would be still left in count set
        if count:
            res += 1
        
        return res

