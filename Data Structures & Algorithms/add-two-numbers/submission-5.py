# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = l1
        curr2 = l2
        temp = ListNode(0)
        result = temp
        remaining = 0
        
        while curr1 is not None or curr2 is not None or remaining > 0:
            

            if curr1 is None:
                val1 = 0
            else:
                val1 = curr1.val
            
            if curr2 is None:
                val2 = 0
            else:
                val2 = curr2.val
                
            total = val1 + val2 + remaining
            remaining = total//10
            temp.next = ListNode(total % 10)
            temp = temp.next 

            if curr1 is not None:
                curr1 = curr1.next
            if curr2 is not None:
                curr2 = curr2.next
                

        return result.next
            

        