class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #find min and max height using end point two pointer. 
        #replace each min and max if smaller or larger
        l = 0
        r = len(heights) - 1
        maximum = 0

        while l < r:
            h = min(heights[l], heights[r])
            width = r - l
            area = h * width
            maximum = max(maximum, area)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maximum 
        



        