def merge(list1: ListNode, list2:ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1:
        tail.next = list1
    else:
        tail.next = list2
    return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        ans = ListNode(-10001)
        map1 = {}
        toDo = []
        #Merge pairs of lists iteratively and halved collections
        
        i = 0
        while i < len(lists)-1:
            toDo.append(merge(lists[i], lists[i+1]))
            i += 2
        if toDo and len(lists) % 2 == 1:
            toDo.append(merge(toDo.pop(0), lists[len(lists)-1]))
        while len(toDo) > 1:
            toDo.append(merge(toDo.pop(0), toDo.pop(0)))
        if toDo:
            return toDo.pop(0)
        else:
            return None
