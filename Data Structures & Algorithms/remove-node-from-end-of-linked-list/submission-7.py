# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        #Count the Length
        length = 0
        head2 = head
        while head2:
            head2 = head2.next
            length += 1
        
        #position of the node to remove (0-indexed from the front)
        n2 = length - n
        #removing head
        if n2 == 0:
            return head.next
        #Walk to the node just before the one we want to remove
        prev = head
        for _ in range(n2-1):
            prev = prev.next

        #Unlink the nth-from-end node
        prev.next = prev.next.next

        return head