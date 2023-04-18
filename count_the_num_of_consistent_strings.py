def countConsistentStrings(allowed, words):
    return list(all(ch in allowed for ch in w) for w in words).count(True)
print(countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))