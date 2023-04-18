def findScore(nums):
    score = 0
    visited = [0] * (len(nums) + 1)
    for x, y in sorted([x, y] for y, x in enumerate(nums)):
        if visited[y]:
            continue
        score += x
        visited[y] = visited[y + 1] = visited[y - 1] = 1
    return score
print(findScore([2,1,3,4,5,2]))