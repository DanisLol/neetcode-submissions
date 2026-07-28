class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        result = []
        r = 0
        
        while r < len(strs):
            if tuple(sorted(strs[r])) in s:
                s[tuple(sorted(strs[r]))] += [strs[r]]
            else:
                s[tuple(sorted(strs[r]))] = [strs[r]]
            r += 1
            
        
        return list(s.values())