from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return False

    queue = deque([root])
    level = 0

    while queue:
        size = len(queue)
        prev_val = None

        for _ in range(size):
            node = queue.popleft()

            if level % 2 == 0:
                if node.val % 2 == 0:
                    return False
                if prev_val is not None and prev_val >= node.val:
                    return False
            else:
                if node.val % 2 != 0:
                    return False
                if prev_val is not None and prev_val <= node.val:
                    return False

            prev_val = node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        level += 1

    return True