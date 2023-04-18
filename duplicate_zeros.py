def duplicateZeros(arr):
    if 0 not in arr:
        return arr
    i = 0
    temp = len(arr)
    while i < len(arr):
        if arr[i] == 0:
            arr[i:i] = [0]
            i += 1
        i += 1
        if i > temp:
            break
    arr = arr[:temp]
    return arr
print(duplicateZeros([1,0,2,3,0,4,5,0]))