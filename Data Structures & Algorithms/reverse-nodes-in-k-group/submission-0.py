def reverse(head: ListNode):
    s = None
    while head:
        prev = head
        head = head.next
        prev.next = s
        s = prev
    return s
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        toDo = []
        i = 0
        prev = head
        #Break up into k length sections in Todo
        while head:
            i+=1
            if i == k:
                i = 0
                toDo.append(prev)
                prev = head
                head = head.next
                prev.next = None
                prev = head
            else:
                head = head.next
        #Add prev to end of reversed lists
        ans = None
        ans1 = None
        for t in toDo:
            #Reverse each one and add
            if ans == None:
                ans = reverse(t)
                ans1 = ans
                while ans.next:
                    ans= ans.next
            else:
                ans.next = reverse(t)
                while ans.next:
                    ans = ans.next
        ans.next = prev
        return ans1
