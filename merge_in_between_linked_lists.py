
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = ListNode()
        end = list1
        for idx in range(b):
            if idx == a - 1:
                start = end
            end = end.next
        start.next = list2
        while list2.next is not None:
            list2 = list2.next
        list2.next = end.next
        end.next = None
        return list1