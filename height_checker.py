def heightChecker(heights):
    s_heights = sorted(heights)
    return sum([1 if heights[i] != s_heights[i] else 0 for i in range(len(heights))])
print(heightChecker([1,2,3,4,5]))