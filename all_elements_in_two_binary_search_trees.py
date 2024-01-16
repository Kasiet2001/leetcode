# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1, root2):
        ans = []
        def traversal(root):
            if root == None:
                return
            ans.append(root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root1)
        traversal(root2)
        ans.sort()
        return ans