
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #last node .next should be the second node
        #store the second node in a set
        #have the last node.next = second node from the set
        
        #slow and fast pointer to find middle element
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        #reversing second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #Merging:
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        
