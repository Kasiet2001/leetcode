def checkIfExist(arr):
    for i in range(len(arr)):
        if arr[i] / 2 in arr[i + 1:] or arr[i] / 2 in arr[:i]:
            return True
    return False
print(checkIfExist([-2,0,10,-19,4,6,-8]))