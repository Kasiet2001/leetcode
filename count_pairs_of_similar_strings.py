def similarPairs(words):
    p = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if set(words[i]) == set(words[j]):
                p += 1
    return p
print(similarPairs(["aabb","ab","ba"]))