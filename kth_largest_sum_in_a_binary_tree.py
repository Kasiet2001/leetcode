from collections import deque
import heapq
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root, k):
        q = deque([root])
        level_sum = []
        while q:
            size = len(q)
            total = 0
            for _ in range(size):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                total += n.val
            heapq.heappush(level_sum, total)
            if len(level_sum) > k:
                heapq.heappop(level_sum)
        if len(level_sum) < k:
            return -1
        return heapq.heappop(level_sum)

