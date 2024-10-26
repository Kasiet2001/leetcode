from collections import defaultdict, deque


def treeSubtreeSizes(parent, s):
    n = len(parent)
    tree = defaultdict(list)
    for i in range(1, n):
        tree[parent[i]].append(i)

    new_tree = defaultdict(list)
    closest_ancestor = {}

    def dfs_update(node):
        char = s[node]
        original_parent = parent[node]

        if char in closest_ancestor:
            new_parent = closest_ancestor[char]
            new_tree[new_parent].append(node)
        else:
            new_tree[original_parent].append(node)

        prev_ancestor = closest_ancestor.get(char)
        closest_ancestor[char] = node

        for child in tree[node]:
            dfs_update(child)

        if prev_ancestor is None:
            del closest_ancestor[char]
        else:
            closest_ancestor[char] = prev_ancestor

    dfs_update(0)

    subtree_size = [0] * n

    def dfs_size(node):
        size = 1
        for child in new_tree[node]:
            size += dfs_size(child)
        subtree_size[node] = size
        return size

    dfs_size(0)

    return subtree_size

