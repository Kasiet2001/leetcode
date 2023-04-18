def vowelStrings(words, queries):
    pref = [0]
    total = 0
    for i in words:
        if i[0] in 'aeiou' and i[-1] in 'aeiou':
            total += 1
        pref.append(total)
    ans = []
    for l, r in queries:
        ans.append(pref[r + 1] - pref[l])
    return ans
print(vowelStrings(["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]]))