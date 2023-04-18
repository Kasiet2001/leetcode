def maximumElementAfterDecrementingAndRearranging(arr):
    arr.sort()
    arr[0] = 1
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i - 1]) <= 1:
            continue
        else:
            arr[i] = arr[i - 1] + 1
    return max(arr)
print(maximumElementAfterDecrementingAndRearranging([1,2,3,4,5]))
