from collections import defaultdict
def checkIfPrerequisite(numCourses, prerequisites, queries):
    def dfs(should_be_done, visited, src, target):
        if src == target:
            return True
        if visited[src]:
            return False
        visited[src] = True
        for t in should_be_done[src]:
            if dfs(should_be_done, visited, t, target):
                return True
        return False
    should_be_done = defaultdict(list)
    ans = [False] * len(queries)
    for s, e in prerequisites:
        should_be_done[s].append(e)
    for i in range(len(queries)):
        visited = [False] * numCourses
        ans[i] = dfs(should_be_done, visited, queries[i][0], queries[i][1])

    return ans
print(checkIfPrerequisite(3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]))