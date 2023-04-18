def findLucky(arr):
    lucky = []
    for i in set(arr):
        if i == arr.count(i):
            lucky.append(i)
    return max(lucky) if len(lucky) > 0 else -1
print(findLucky([2,2,2,3,3]))