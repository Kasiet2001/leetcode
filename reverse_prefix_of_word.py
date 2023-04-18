def reversePrefix(word, ch):
    if ch in word:
        pref = ''.join([word[i] for i in range(word.index(ch), -1, -1)])
        return word.replace(word[:word.index(ch) + 1], pref)
    return word
print(reversePrefix("abcdefd", "g"))
