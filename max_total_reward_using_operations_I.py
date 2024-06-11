def maxTotalReward(rewardValues):
    rewardValues.sort()
    ans = {0}
    for r in rewardValues:
        new_rewards = set()
        for x in ans:
            if r > x:
                new_rewards.add(x + r)
        ans.update(new_rewards)

    return max(ans)
print(maxTotalReward([1,6,4,3,2]))