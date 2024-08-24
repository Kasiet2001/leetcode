class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        odd = ListNode(0)
        curr_odd = odd
        even = ListNode(0)
        curr_even = even
        idx = 0
        while head != None:
            if idx % 2 == 0:
                curr_even.next = head
                curr_even = curr_even.next
            else:
                curr_odd.next = head
                curr_odd = curr_odd.next
            head = head.next
            idx += 1
        curr_even.next = None
        curr_odd.next = even.next
        return odd.next
