class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        n = {}
        m = {}

        if len(s) != len(t):
            return False
        
        for i in s:
            n[i] = 1 + n.get(i, 0)
        for j in t:
            m[j] = 1 + m.get(j, 0)
        
        return n==m
        


            