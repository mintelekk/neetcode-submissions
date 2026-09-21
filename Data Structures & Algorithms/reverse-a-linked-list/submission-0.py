# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = None
        while head:
            s1 = ListNode(val=head.val, next=None)
            s1.next = s
            s = s1
            head = head.next

        
        return s