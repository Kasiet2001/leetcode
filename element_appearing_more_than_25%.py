def findSpecialInteger(arr):
    n = len(arr) // 4
    for i in range(len(arr)):
        if arr[i] == arr[i + n]:
            return arr[i]
print(findSpecialInteger([1,2,2,6,6,6,6,7,10]))