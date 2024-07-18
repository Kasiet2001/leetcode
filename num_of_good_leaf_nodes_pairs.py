class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [1]
            left = dfs(root.left)
            right = dfs(root.right)
            for i in left:
                for j in right:
                    if i+j <= distance:
                        self.ans += 1
            return [i+1 for i in left+right if i+1 < distance]
        dfs(root)
        return self.ans

# Constructing a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Counting good leaf node pairs with a distance of 3
solution = Solution()
result = solution.countPairs(root, 3)
print(result)  # Output depends on the tree structure and distance
