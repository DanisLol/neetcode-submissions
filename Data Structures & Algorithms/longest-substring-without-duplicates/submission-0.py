class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        st = set()
        res = 0
        #dynamic sliding window not static since size is not fixed
        for r in range(0, len(s)):
            while s[r] in st:
                st.remove(s[l])
                l+=1
            st.add(s[r])
            res = max(res, r-l+1)

            
            
        return res



