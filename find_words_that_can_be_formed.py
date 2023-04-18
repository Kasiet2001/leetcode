def countCharacters(words, chars):
    from collections import Counter
    t = 0
    chars = Counter(chars)
    for w in words:
        word = Counter(w)
        for c in word:
            if word[c] > chars[c]:
                break
        else:
            t += len(w)
    return t
print(countCharacters(["hello","world","leetcode"],"welldonehoneyr"))