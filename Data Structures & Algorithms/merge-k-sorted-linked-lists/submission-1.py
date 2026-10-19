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
        for i, l in enumerate(lists):
            map1[i] = l
            toDo.append(i)
        #Merge pairs of lists iteratively and halved collections
        i_0 = toDo[len(toDo)-1]
        while len(toDo) > 1:
            i_0 += 1
            map1[i_0] = merge(map1[toDo.pop(0)], map1[toDo.pop(0)])
            toDo.append(i_0)
        return map1[i_0]
