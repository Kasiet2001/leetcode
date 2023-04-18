def countPrefixes(words, s):
    total = 0
    for i in words:
        if s[:len(i)] == i:
            total += 1
    return total
print(countPrefixes(["a","b","c","ab","bc","abc"], "abc"))