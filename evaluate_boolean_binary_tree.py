class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def evaluateTree(self, root):
        stack = [root]
        evaluated = {}
        while stack:
            top_node = stack[-1]
            if not top_node.left and not top_node.right:
                stack.pop()
                evaluated[top_node] = top_node.val == 1
                continue
            if top_node.left in evaluated and top_node.right in evaluated:
                stack.pop()
                if top_node.val == 2:
                    evaluated[top_node] = evaluated[top_node.left] or evaluated[top_node.right]
                else:
                    evaluated[top_node] = evaluated[top_node.left] and evaluated[top_node.right]
            else:
                if top_node.left:
                    stack.append(top_node.left)
                if top_node.right:
                    stack.append(top_node.right)
        return evaluated[root]


    # if not root.left and not root.right:
    #
    #     return root.val != 0
    #
    # evaluate_left_subtree = self.evaluateTree(root.left)
    # evaluate_right_subtree = self.evaluateTree(root.right)
    # if root.val == 2:
    #     evaluate_root = evaluate_left_subtree or evaluate_right_subtree
    # else:
    #     evaluate_root = evaluate_left_subtree and evaluate_right_subtree
    #
    # return evaluate_root

