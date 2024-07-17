from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root, to_delete):
        delete = set(to_delete)
        res = []
        nodes = deque([root])
        while nodes:
            node = nodes.popleft()
            if node.left:
                nodes.append(node.left)
                if node.left.val in delete:
                    node.left = None
            if node.right:
                nodes.append(node.right)
                if node.left.val in delete:
                    node.right = None
            if node.val in delete:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
        if root.val not in delete:
            res.append(root)
        return res