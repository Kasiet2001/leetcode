class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head, root) -> bool:
        if not root:
            return False
        stack = root
        while stack:
            node = stack.pop()
            if self._is_match(node, head):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
    def _is_match(self, node, lst):
        stack = [(node, lst)]
        while stack:
            curr_node, curr_list = stack.pop()
            while curr_node and curr_list:
                if curr_node.val != curr_list.val:
                    break
                curr_list = curr_list.next
                if curr_list:
                    if curr_node.left:
                        stack.append((curr_node.left, curr_list))
                    if curr_node.right:
                        stack.append((curr_node.right, curr_list))
            if not curr_list:
                return True
        return False