def levelOrder(root):
    if not root:
        return []
    queue = [root]
    ans = [[root.val]]
    while queue:
        curr_level = []
        size = len(queue)
        for _ in range(size):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                curr_level.append(node.left.val)
            if node.right:
                queue.append(node.right)
                curr_level.append(node.right.val)
        if curr_level:
            ans.append(curr_level)
    return ans