def minCost(colors, neededTime):
    ans = 0
    i = 0
    j = 0
    while i < len(colors) and j < len(colors):
        curr_max = 0
        curr_sum = 0
        while j < len(neededTime) and colors[i] == colors[j]:
            curr_max = max(neededTime[j], curr_max)
            curr_sum += neededTime[j]
            j += 1
        ans += curr_sum - curr_max
        i = j
    return ans
print(minCost("aabaa", [1,2,3,4,1]))