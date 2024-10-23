from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def replaceValueInTree(self, root):
        if not root:
            return root
        q = deque([root])
        level_sums = []
        while q:
            level_sum = 0
            level_size = len(q)
            for _ in range(level_size):
                curr_node = q.popleft()
                level_sums += curr_node.val
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            level_sums.append(level_sum)

        q = deque([(root, root.val)])
        level = 0
        while q:
            for i in range(len(q)):
                node, val = q.popleft()
                node.val = level_sums[level] - val
                child_sum = 0
                if node.left:
                    child_sum += node.left.val
                if node.right:
                    child_sum += node.right.val
                if node.left:
                    q.append((node.left, child_sum))
                if node.right:
                    q.append((node.right, child_sum))
            level += 1
        return root
