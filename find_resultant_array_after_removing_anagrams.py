def removeAnagrams(words):
    return [words[i] for i in range(len(words)) if i == 0 or sorted(words[i]) != sorted(words[i - 1])]
print(removeAnagrams(["abba","baba","bbaa","cd","cd"]))