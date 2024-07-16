class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDirections(self, root, startValue, destValue):

        def find(node, val, path):
            if node.val == val:
                return True
            if node.left and find(node.left, val, path):
                path.append('L')
                return True
            if node.right and find(node.right, val, path):
                path.append('R')
                return True
            return False
        p1 = []
        p2 = []
        find(root, startValue, p1)
        find = find(root, destValue, p2)
        while p1 and p2 and p1[-1] == p2[-1]:
            p1.pop()
            p2.pop()
        return 'U' * len(p1) + ''.join(p2[::-1])

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)

solution = Solution()
print(solution.getDirections(root, 3, 6))