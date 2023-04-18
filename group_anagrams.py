def groupAnagrams(strs):
    ana = {}
    for w in strs:
        s = ''.join(sorted(w))
        if s in ana:
            ana[s].append(w)
        else:
            ana[s] = [w]
    return list(ana.values())
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))