def lastVisitedIntegers(words):
    ans = []
    integers = []
    k = 0
    for i in words:
        if i == 'prev':
            k += 1
            if k > len(integers):
                ans.append(-1)
            else:
                ans.append(integers[-k])
        else:
            k = 0
            integers.append(i)
    return ans
print(lastVisitedIntegers(["1","prev","2","prev","prev"]))