def sortVowels(s):
    vowels = []
    ind = []
    s = list(s)
    for i, ch in enumerate(s):
        if ch.lower() in 'aeiou':
            vowels.append(ch)
            ind.append(i)
    vowels.sort()
    for j in range(len(vowels)):
        s[ind[j]] = vowels[j]
    return ''.join(s)
print(sortVowels("LQRamBOHfq"))
