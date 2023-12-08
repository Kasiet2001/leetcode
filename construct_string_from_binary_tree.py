def tree2str(root):
    res = []
    def preorder(root):
        if not root:
            return
        res.append('(')
        res.append(str(root.val))
        if not root.left and root.right:
            res.append('()')
        preorder(root.left)
        preorder(root.right)
        res.append(')')

    preorder(root)
    return ''.join(res)[1:-1]