class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        ans = dummy
        total = remainder = 0
        while l1 or l2 or remainder:
            total = remainder
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            num = total % 10
            remainder = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next
        return ans.next
