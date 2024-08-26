class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node'):
        res = []
        if not root:
            return res

        stack = [root]
        while stack:
            curr_node = stack.pop()
            stack.append(curr_node)
            for child in curr_node.children:
                stack.append(child)
        res.reverse()
        return res