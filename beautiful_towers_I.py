def maximumSumOfHeights(heights):
    ans = 0
    for i in range(len(heights)):
        curr, v = heights[i], heights[i]
        for j in range(i + 1, len(heights)):
            v = min(v, heights[j])
            curr += v
        v = heights[i]
        for j in range(i - 1, -1, -1):
            v = min(v, heights[j])
            curr += v
        ans = max(ans, curr)
    return ans
print(maximumSumOfHeights([3,2,5,5,2,3]))
