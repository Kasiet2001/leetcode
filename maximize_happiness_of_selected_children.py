def maximumHappinessSum(happiness, k):
    decreases = 0
    happiness.sort(reverse=True)
    ans = 0
    for i in range(k):
        if happiness[i] - decreases <= 0:
            return ans
        ans += happiness[i] - decreases
        decreases += 1
    return ans
print(maximumHappinessSum([2,3,4,5], 1))