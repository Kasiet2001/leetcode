def findTheDistanceValue(arr1, arr2, d):
    n = 0
    for i in arr1:
        t = 0
        for j in arr2:
            if abs(i - j) <= d:
                break
            else:
                t += 1
        if t == len(arr2):
            n += 1
    return n
print(findTheDistanceValue([2,1,100,3],[-5,-2,10,-3,7], 6))