class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        k = 0
        st1 = {}

        if len(s1) > len(s2):
            return False

        # set up:
        for i in range(len(s1)):
            st1[s1[i]] = st1.get(s1[i], 0) + 1

        st2 = {}
        for i in range(len(s1)):
            st2[s2[i]] = st2.get(s2[i], 0) + 1


        for r in range(len(s1), len(s2)):
            if st1 == st2:
                return True
            st2[s2[r]] = st2.get(s2[r], 0) + 1

            st2[s2[l]] -= 1
            if st2[s2[l]] == 0:
                del st2[s2[l]]
            l += 1
            
        return st1 == st2