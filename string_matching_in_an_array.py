def stringMatching(words):
    return [i for i in words if (' '.join(words)).count(i) >= 2]
print(stringMatching(["leetcode","et","code"]))