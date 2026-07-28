# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lst = set()
    
        curr1 = head

        while curr1 is not None:
            lst.add(curr1)

            if curr1.next is not None and curr1.next in lst:
                return True

            curr1 = curr1.next
            
        return False
