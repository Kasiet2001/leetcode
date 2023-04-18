def getWinner(arr, k):
    if len(arr) <= k:
        return max(arr)
    ans = arr.pop(0)
    n = 0
    for i in arr:
        if i > ans:
            ans = i
            n = 0
        n += 1
        if n == k:
            return ans
    return ans
print(getWinner([1,25,35,42,68,70], 2))