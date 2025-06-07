def maxSumDistinctTriplet(x, y):
    if len(set(x)) < 3:
        return -1
    vals = dict()
    for i, num in enumerate(x):
        if num in vals:
            vals[num] = max(vals[num], y[i])
        else:
            vals[num] = y[i]
    max_vals = sorted(vals.values())
    return max_vals[-1] + max_vals[-2] + max_vals[-3]
print(maxSumDistinctTriplet([1,2,1,3,2], [5,3,4,6,2]))