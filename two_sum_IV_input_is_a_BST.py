def findTarget(self, root, k):
    self.hashMap = {}

    def dfs(root, k):
        if root == None:
            return
        if k - root.val in self.hashMap:
            return True
        self.hashMap[root.val] = True
        n = dfs(root.left, k) or dfs(root.right, k)
        return n

    return dfs(root, k)