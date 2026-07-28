class Solution:
    def longestPalindrome(self, s: str) -> int:
        #find even and odd palindrome
        #use hash map to find occurences of each character
        #we could have constnat space complexity if we have 52 distinct characters
        #but depending on charcter set, it could be linear space complexity
        #time complexity is linear time O(n)
        count = defaultdict(int)
        res = 0
        for i in s:
            count[i] += 1
            if count[i] % 2 == 0:
                res += 2

        for n in count.values():
            if n % 2 == 1:
                res += 1
                break

        return res

