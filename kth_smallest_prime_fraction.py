import random
def kthSmallestPrimeFraction(arr, k):
    fr = []
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            fr.append([arr[i], arr[j]])
    sort = sorted(fr, key=lambda x: x[0]/x[1])
    return sort[k - 1]
print(kthSmallestPrimeFraction([1,2,3,5], 3))