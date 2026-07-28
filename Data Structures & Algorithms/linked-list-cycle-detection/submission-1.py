# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lst = {}
        
        curr_i = 0
        curr1 = head

        while curr1 is not None:
            lst[curr1] = curr_i

            if curr1.next is not None and curr1.next in lst:
                return True

            curr1 = curr1.next
            curr_i+=1
            
        return False
