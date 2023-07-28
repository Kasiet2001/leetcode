from collections import defaultdict
def arrayRankTransform(arr):
    ans = []
    d = defaultdict(int)
    lis = list(set(arr))
    lis.sort()
    for i in range(len(lis)):
        d[lis[i]] += i + 1
    for j in arr:
        ans.append(d[j])
    return ans
print(arrayRankTransform([40,10,20,30]))