class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = 0
        b = len(matrix) - 1
        
        row = 0
        while a <= b:
            m = (a+b)//2
            if matrix[m][0] <= target:
                row = m
                a = m + 1
            else:
                b = m - 1
        
        x = 0 
        y = len(matrix[0]) - 1

        while x <= y:
            mid = (x+y)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                x = mid + 1
            else:
                y = mid - 1
        
        return False