class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        count = {}
        maximum = -1
        for i in range(len(s)):
            if s[i] in count:
                if i - count[s[i]] > maximum:
                    maximum = i - count[s[i]] -1
            else:
                count[s[i]] = i
        
        return maximum


