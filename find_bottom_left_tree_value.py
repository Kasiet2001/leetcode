from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findBottomLeftValue(root) -> int:
    queue = deque([root])
    leftmost = None
    while queue:
        node = queue.popleft()
        leftmost = node.val
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return leftmost
root = TreeNode(1)

root.right = TreeNode(3)

print(findBottomLeftValue(root))