# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        arr = []
        curr1 = head
        while curr1 is not None:
            arr.append(curr1.val)
            curr1 = curr1.next
        

        curr2 = head
        index = 0
        while curr2 is not None:
            if arr[index] != arr[len(arr) - 1 - index]:
                return False
            curr2 = curr2.next
            index += 1


        return True



