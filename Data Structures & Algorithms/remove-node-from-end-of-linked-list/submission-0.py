# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        curr = head
        prev = dummy
        i = 0

        c = head
        count = 0
        while c is not None:
            count += 1
            c = c.next

        while curr is not None:
            
            if count - n == i:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            i += 1

        return dummy.next



