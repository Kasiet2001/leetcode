def uniqueOccurrences(arr):
    occ = {}
    for i in arr:
        occ[i] = arr.count(i)
    return len(occ) == len(set(occ.values()))
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))