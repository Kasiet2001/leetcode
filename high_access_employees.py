from collections import defaultdict
def findHighAccessEmployees(access_times):
    d = defaultdict(list)
    for e, t in access_times:
        d[e].append(int(t[:2]) * 60 + int(t[2:]))
    ans = []
    for k, v in d.items():
        if len(v) > 2:
            v.sort()
            for i in range(2, len(v)):
                if v[i] - v[i - 2] < 60:
                    ans.append(k)
                    break
    return ans
print(findHighAccessEmployees([["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]))