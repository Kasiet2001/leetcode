from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(descriptions):
        node_map = {}

        children = set()

        for parent_value, child_value, is_left in descriptions:

            if parent_value not in node_map:
                node_map[parent_value] = TreeNode(parent_value)
            if child_value not in node_map:
                node_map[child_value] = TreeNode(child_value)

            if is_left:
                node_map[parent_value].left = node_map[child_value]
            else:
                node_map[parent_value].right = node_map[child_value]

            children.add(child_value)

        for node in node_map.values():
            if node.val not in children:
                return node

        return None
    print(createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]))

