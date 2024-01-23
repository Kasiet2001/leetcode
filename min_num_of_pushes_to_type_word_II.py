def minimumPushes(word):
    ans = 0
    letter_count = dict()
    for ch in range(len(word)):
        letter_count[word[ch]] = letter_count.get(word[ch], 0) + 1
    freq = list(letter_count.values())
    freq.sort(reverse=True)
    pushes = 1
    for i in range(len(freq)):
        if i > 7 and i % 8 == 0:
            pushes += 1
        ans += freq[i] * pushes
    return ans
print(minimumPushes("xyzxyzxyzxyz"))