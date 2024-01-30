def postorderTraversal(root):
    ans = []

    def postOrder(root):
        if root is None:
            return
        postOrder(root.left)
        postOrder(root.right)
        ans.append(root.val)

    postOrder(root)
    return ans