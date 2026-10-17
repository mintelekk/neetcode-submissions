# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        ansHead = ans
        carryOver = 0
        while l1 or l2:
            num = 0
            if l1:
                num += l1.val
            if l2:
                num += l2.val
            if ans is None:
                ans = ListNode(num % 10)
                ansHead = ans
            else:
                num2 = (num + carryOver) % 10                    
                ans.next = ListNode(num2)
                ans = ans.next
            carryOver = (num + carryOver) // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carryOver > 0:
            ans.next = ListNode(carryOver)
            ans = ans.next
        return ansHead