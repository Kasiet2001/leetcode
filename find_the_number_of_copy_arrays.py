def countArrays(original, bounds):
    n = len(original)

    lower_bound = bounds[0][0]
    upper_bound = bounds[0][1]

    for i in range(1, n):
        diff = original[i] - original[i - 1]

        lower_bound = max(lower_bound + diff, bounds[i][0])
        upper_bound = min(upper_bound + diff, bounds[i][1])

        if lower_bound > upper_bound:
            return 0
    return upper_bound - lower_bound + 1
print(countArrays([1,2,3,4], [[1,2],[2,3],[3,4],[4,5]]))