def maximumEvenSplit(finalSum):
    if finalSum % 2:
        return []
    ans = []
    i = 2
    while i <= finalSum:
        ans.append(i)
        finalSum -= i
        i += 2
    ans[-1] += finalSum
    return ans
print(maximumEvenSplit(28))