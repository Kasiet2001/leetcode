class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head):
        node = head
        curr_pos = 2
        prev_pos = -1
        minn = float('inf')
        maxx = [-1, -1]

        while node.next and node.next.next:
            if (node.val < node.next.val and node.next.val > node.next.next.val) or (
                    node.val > node.next.val and node.next.val < node.next.next.val):
                if maxx[0] == -1:
                    maxx[0] = curr_pos
                if prev_pos != -1:
                    minn = min(minn, curr_pos - prev_pos)
                maxx[1] = curr_pos
                prev_pos = curr_pos
            curr_pos += 1
            node = node.next

        return [minn, maxx[1] - maxx[0]] if minn != float('inf') else [-1, -1]