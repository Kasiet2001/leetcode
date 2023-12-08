def inorderTraversal(root):
    ans = []
    def inorder(root):
        if not root:
            return None
        inorder(root.left)
        ans.append(root.val)
        inorder(root.right)
    inorder(root)
    return ans