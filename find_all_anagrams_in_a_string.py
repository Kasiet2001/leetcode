def findAnagrams(s, p):
    from collections import Counter
    p = sorted(p)
    ans = []
    for i in range(len(s) - len(p) + 1):
        if sorted(s[i:i+len(p)]) == p:
            ans.append(i)
    return ans
print(findAnagrams("cbaebabacd", "abc"))