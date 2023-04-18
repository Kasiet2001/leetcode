def findLeastNumOfUniqueInts(arr, k):
    from collections import Counter
    c = Counter(arr)
    n = Counter(c.values())
    l = len(c)
    for i in sorted(n):
        if k > i * n[i]:
            k -= i * n[i]
            l -= n.pop(i)
        else:
            return l - k // i
    return l
print(findLeastNumOfUniqueInts([24,119,157,446,251,117,22,168,374,373,323,311,441,213,120,412,200,236,328,24,164,104,331,32,19,223,89,114,152,82,456,381,355,343,157,245,443,368,229,49,82,16,373,142,240,125,8], 41))