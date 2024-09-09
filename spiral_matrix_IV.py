class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head):
        matrix = [[-1] * n for _ in range(m)]
        u, l, r, d = 0, 0, n-1, m-1
        current = head
        while current and l <= r and u <= d:
            for i in range(l, r + 1):
                if current:
                    matrix[u][i] = current.val
                    current = current.next
            u += 1
            for i in range(u, d + 1):
                if current:
                    matrix[i][r] = current.val
                    current = current.next
            r -= 1
            if l <= r:
                for i in range(r, l - 1, -1):
                    if current:
                        matrix[d][i] = current.val
                        current = current.next
            d -= 1
            if u <= d:
                for i in range(d, u - 1, -1):
                    if current:
                        matrix[i][l] = current.val
                        current = current.next
            l += 1
        return matrix
