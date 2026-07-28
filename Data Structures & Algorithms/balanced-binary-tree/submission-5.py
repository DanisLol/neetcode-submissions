# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]

    def dfs(self, root: Optional[TreeNode]) -> list:
            if root is None:
                return [True,0]
            left, right = self.dfs(root.left), self.dfs(root.right)

            balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balance, 1 + max(left[1], right[1])]
            
            




    #     if root is None:
    #         return True
        
    #     if abs(self.count(root.left) - self.count(root.right)) > 1:
    #         return False
    #     return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    # def count(self, root: Optional[TreeNode]) -> int:
    #     if root is not None: 
    #         return 1 + max(self.count(root.left), self.count(root.right))
    #     else:
    #         return 0





