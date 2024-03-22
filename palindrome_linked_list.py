class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        n = []
        while head:
            n.append(head.val)
            head = head.next
        return n == n[::-1]