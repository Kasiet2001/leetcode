def connect(root):
    q = deque([root])
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i < size - 1:
                node.next = q[0]
            if node and node.left:
                q.append(node.left)
            if node and node.right:
                q.append(node.right)
    return root