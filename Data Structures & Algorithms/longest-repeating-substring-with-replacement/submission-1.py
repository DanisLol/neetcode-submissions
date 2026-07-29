class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #find a window of lettes where almost all of htem are already
        #the same
        #use k changes to fix the different letters
        #total - most frequent = k
        res = 0
        l = 0
        maxf = 0
        count = {}
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            window_len = r - l + 1
            maxf = max(count.values())
            if window_len - maxf > k:
                count[s[l]] -= 1
                l+=1
            res = max(res, r-l + 1)
              
        
        return res




