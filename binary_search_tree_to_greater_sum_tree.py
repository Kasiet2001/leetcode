class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        node_sum = 0
        stack = []
        node = root
        while stack and node is not None:
            while node is not None:
                stack.append(node)
                node = node.right
            node = stack.pop()
            node_sum += node.val
            node.val = node_sum
            node = node.left
        return root
