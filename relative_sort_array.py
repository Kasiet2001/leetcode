def relativeSortArray(arr1, arr2):
    a = len(arr1)
    n_a = [i for i in arr1 if i not in arr2]
    for i in arr2:
        arr1.extend([i] * arr1.count(i))
    arr1.extend(n_a)
    return arr1[a:]
print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))