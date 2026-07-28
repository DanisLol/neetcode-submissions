class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums)

        while a < b:
            mid = (a+b)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                b = mid
            else:
                a = mid + 1

        return -1