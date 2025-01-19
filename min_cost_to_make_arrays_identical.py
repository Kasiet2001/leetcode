def minCost(arr, brr, k):
    res1 = 0
    for i in range(len(arr)):
        res1 += abs(arr[i] - brr[i])
    arr.sort()
    brr.sort()
    res2 = 0
    for i in range(len(arr)):
        res2 += abs(arr[i] - brr[i])
    return min(res2 + k, res1)