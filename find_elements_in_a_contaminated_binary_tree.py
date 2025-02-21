class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root):
        self.seen = set()
        self.bfs(root)

    def find(self, target: int):
        return target in self.seen

    def bfs(self, root):
        q = [root]
        root.val = 0
        while q:
            curr_node = q.pop(0)
            self.seen.add(curr_node.val)
            if curr_node.left:
                curr_node.left.val = 2 * curr_node.val + 1
                q.append(curr_node.left)
            if curr_node.right:
                curr_node.right.val = 2 * curr_node.val + 2
                q.append(curr_node.right)
