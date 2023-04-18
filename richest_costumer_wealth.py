def maximumWealth(accounts):
    return max([sum(i) for i in accounts])
print(maximumWealth([[1,5],[7,3],[3,5]]))