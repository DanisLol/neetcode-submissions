class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #hashmap
        s = {}
        
        for i in range(len(nums)):
            s[nums[i]] = 1 + s.get(nums[i], 0)
            if s[nums[i]] > 1:
                return nums[i]
        
