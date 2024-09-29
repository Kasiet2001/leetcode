def kthCharacter(k):
    word = 'a'
    while len(word) < k:
        n = len(word)
        idx = 0
        while idx < n:
            word += chr((ord(word[idx]) % 97) + 97 + 1)
            idx = idx % len(word) + 1
    return word[k - 1]
print(kthCharacter(10))