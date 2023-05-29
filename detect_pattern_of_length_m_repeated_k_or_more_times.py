def containsPattern(arr, m, k):
    ind = 0
    while ind <= len(arr) - 1:
        p = arr[ind: ind + m]
        if p * k == arr[ind: ind + m * k]:
            return True
        ind += 1
    return False
print(containsPattern([1,2,1,2,1,3], 2, 3))