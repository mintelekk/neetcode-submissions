class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        head5 = head
        head2 = None
        oldToNewMap = {None: None}
        if head:
            head2 = Node(head.val, head.next, head.random)
            oldToNewMap[head]=head2
            head = head.next
        head3 = head2
        while(head):
            n1 = Node(head.val, head.next, head.random)
            oldToNewMap[head]=n1
            head2.next = n1
            head = head.next
            head2 = head2.next
        head4 = head3
        while head4:
            head4.random = oldToNewMap[head5.random]
            head4 = head4.next
            head5 = head5.next
        return head3