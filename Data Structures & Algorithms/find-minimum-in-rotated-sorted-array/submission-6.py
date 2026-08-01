class Solution:
    def findMin(self, nums: List[int]) -> int:
        a = 0
        b = len(nums) -1
        res = nums[0]
        while a <= b:
            if nums[a] < nums[b]:
                res = min(res, nums[a])
                break

            m = (a+b)//2
            res = min(res, nums[m])
            if nums[m] >= nums[a]:
                a = m+1
            else:
                b = m-1
            

        return res
        

        