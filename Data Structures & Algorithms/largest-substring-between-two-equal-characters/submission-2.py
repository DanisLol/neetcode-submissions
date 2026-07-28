class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        count = {}
        maximum = -1
        for i in range(len(s)):
            if s[i] in count:
                current_length = i - count[s[i]] -1
                maximum = max(maximum, current_length)
            else:
                count[s[i]] = i
        
        return maximum


