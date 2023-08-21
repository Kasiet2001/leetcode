def peakIndexInMountainArray(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
print(peakIndexInMountainArray([0,10,5,2]))