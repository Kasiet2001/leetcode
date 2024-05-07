class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def doubleIt(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        new_head = None
        carry = 0

        while nums or carry:
            if nums:
                carry += nums.pop() * 2
            new_node = ListNode(carry % 10)
            new_node.next = new_head
            new_head = new_node
            carry //= 10

        return new_head
