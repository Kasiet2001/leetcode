def mostPoints(questions):
    dp = {}
    for i in range(len(questions) - 1, -1, -1):
        dp[i] = max(questions[i][0] + dp.get(i + 1 + questions[i][1], 0), dp.get(i + 1, 0))
    return dp[0]
print(mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]))