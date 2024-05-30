def occurrencesOfElement(nums, queries, x):
    indices = [i for i, num in enumerate(nums) if num == x]
    ans = []
    for q in queries:
        if q <= len(indices):
            ans.append(indices[q - 1])
        else:
            ans.append(-1)
    return ans
print(occurrencesOfElement([1,3,1,7], [1,3,2,4], 1))