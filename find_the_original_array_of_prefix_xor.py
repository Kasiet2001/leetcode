def findArray(pref):
    ans = [pref[0]]
    n = len(pref)
    for i in range(1, n):
        ans.append(pref[i] ^ pref[i - 1])
    return ans
print(findArray([5,2,0,3,1]))