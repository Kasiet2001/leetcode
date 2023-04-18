def peopleIndexes(favoriteCompanies):
    ans = []
    fc = [set(i) for i in favoriteCompanies]
    for i, s1 in enumerate(fc):
        c = 0
        for j, s2 in enumerate(fc):
            if i != j:
                if s1.issubset(s2) == False:
                    c += 1
        if c == len(favoriteCompanies) - 1:
            ans.append(i)
    return ans
print(peopleIndexes([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]))