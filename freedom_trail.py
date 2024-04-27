def findRotateSteps(ring, key):
    dp = [0] * len(ring)

    for k in reversed(range(len(key))):
        curr_dp = [float('inf')] * len(ring)
        for r in range(len(ring)):
            for i, c in enumerate(ring):
                if c == key[k]:
                    distance = min(abs(r - i), len(ring) - abs(r - i))
                    curr_dp[r] = min(curr_dp[r], dp[i] + 1 + distance)
        dp = curr_dp
    return dp[0]
print(findRotateSteps("godding", 'gd'))