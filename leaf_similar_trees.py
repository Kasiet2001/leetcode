# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        def preOrder(root, leaf_v):
            if not root:
                return
            if not root.left and not root.right:
                leaf_v.append(root.val)
            preOrder(root.left, leaf_v)
            preOrder(root.right, leaf_v)

        leaf_vals1 = []
        leaf_vals2 = []
        preOrder(root1, leaf_vals1)
        preOrder(root2, leaf_vals2)
        return leaf_vals1 == leaf_vals2