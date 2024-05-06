class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def removeNodes(self, head):
        curr = head
        stack = []
        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            stack.append(curr)
            curr = curr.next
        n = None
        while stack:
            curr = stack.pop()
            curr.next = n
            n = curr
        return curr

