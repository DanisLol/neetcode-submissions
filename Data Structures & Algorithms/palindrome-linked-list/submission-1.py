# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #hasmap for each element: index
        #while loop and see if they are not equal to each other + 
        #s[current index] != s[length of LinkedList - currindex] then return False

        s = {}
        count = 0
        temp = head
        while temp is not None:
            s[count] = temp.val
            temp = temp.next
            count += 1
        
        curr = head
        index = 0
        while curr is not None:
            if s[index] != s[count - 1 - index]:
                return False
            curr = curr.next
            index += 1


        return True