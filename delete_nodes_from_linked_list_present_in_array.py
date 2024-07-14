class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nodes(head, nums):
    nums_set = set(nums)

    dummy = ListNode(next=head)
    current = dummy

    while current.next:
        if current.next.val in nums_set:
            current.next = current.next.next
        else:
            current = current.next
    return dummy.next