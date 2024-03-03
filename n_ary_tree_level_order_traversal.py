from collections import deque
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node'):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            size = len(queue)
            level_values = []
            for _ in range(size):
                current = queue.popleft()
                level_values.append(current.val)
                for child in current.children:
                    queue.append(child)
            result.append(level_values)
        return result