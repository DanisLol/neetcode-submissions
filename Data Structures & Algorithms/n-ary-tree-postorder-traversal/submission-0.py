"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        elif root.children is None:
            return [root.val]
        else:
            lst = []
            for i in root.children:
                lst += self.postorder(i)
            lst += [root.val]
        return lst