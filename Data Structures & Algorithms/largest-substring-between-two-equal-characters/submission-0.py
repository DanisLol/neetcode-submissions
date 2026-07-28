class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        count = {}
        maximum = 0
        for i in range(len(s)):
            if s[i] in count:
                if i - count[s[i]] > maximum:
                    maximum = i - count[s[i]] -1
            else:
                count[s[i]] = i
        
        if len(count) == len(s):
            return -1
        
        return maximum


