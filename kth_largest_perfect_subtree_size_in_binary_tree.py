class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root, k):
        def post_order(node, sizes):
            if not node:
                return 0, True
            left_size, is_left_perfect = post_order(node.left, sizes)
            right_size, is_right_perfect = post_order(node.right, sizes)

            if is_left_perfect and is_right_perfect and left_size == right_size:
                size = 1 + left_size + right_size
                sizes.append(size)
                return size, True
            else:
                return 0, False

        sizes = []
        post_order(root, sizes)
        sizes.sort(reverse=True)
        return sizes[k - 1] if k <= len(sizes) else -1