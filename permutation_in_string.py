from collections import defaultdict
def checkInclusion(s1, s2):
    mp = defaultdict(int)
    mp2 = defaultdict(int)
    for ch in s1:
        mp2[ch] += 1
    i, j = 0, 0
    k = len(s1)
    n = len(s2)
    while j < n:
        mp[s2[j]] += 1
        j += 1
        if j - i == k:
            if mp == mp2:
                return True
            mp[s2[i]] -= 1
            if mp[s2[i]] == 0:
                del mp[s2[i]]
            i += 1
    return False
print(checkInclusion("ab", "eidboaoo"))
