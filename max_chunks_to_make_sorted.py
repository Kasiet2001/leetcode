def maxChunksToSorted(arr):
    res = 0
    pref_sum = 0
    sorted_sum = 0
    n = len(arr)
    for i in range(n):
        pref_sum += arr[i]
        sorted_sum += i
        if pref_sum == sorted_sum:
            res += 1
            pref_sum = 0
            sorted_sum = 0
    return res
print(maxChunksToSorted([1,0,2,3,4]))