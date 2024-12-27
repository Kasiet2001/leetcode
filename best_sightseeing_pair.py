def maxScoreSightseeingPair(values):
    ans = 0
    left_max = values[0]
    for i in range(1, len(values)):
        curr_right = values[i] - i
        ans = max(ans, left_max + curr_right)
        curr_left = values[i] + i
        left_max = max(curr_left, left_max)
    return ans
print(maxScoreSightseeingPair([1,3,5]))
