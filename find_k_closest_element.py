def findClosestElements(arr, k, x):
    elem = sorted(arr, key=lambda a: abs(a - x))
    return sorted(elem[:k])
print(findClosestElements([1,2,5,5,6,6,7,7,8,9], 7, 7))