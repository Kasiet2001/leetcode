from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root):
        if not root:
            return []
        ans = []
        row = deque([root])
        while row:
            size = len(row)
            maxx = float('-inf')
            for _ in range(size):
                elem = row.popleft()
                if elem.val > maxx:
                    maxx = elem.val
                if elem.left:
                    row.append(elem.left)
                if elem.right:
                    row.append(elem.right)
            ans.append(maxx)
        return ans







