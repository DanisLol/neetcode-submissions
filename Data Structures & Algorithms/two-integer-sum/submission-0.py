class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = 0
        s = {}
        while r < len(nums):
            if target - nums[r] in s:
                return [s[target-nums[r]],r]
            else:
                s[nums[r]] = r
                r += 1
        return []