# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True
        
        if abs(self.count(root.left) - self.count(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def count(self, root: Optional[TreeNode]) -> int:
        if root is not None: 
            return 1 + max(self.count(root.left), self.count(root.right))
        else:
            return 0





