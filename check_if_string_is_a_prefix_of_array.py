def isPrefixString(s, words):
    ind = 0
    for word in words:
        if s[ind:ind + len(word)] != word:
            return False
        ind += len(word)
        if ind == len(s):
            return True
    return False
print(isPrefixString("applebananacookie", ["banana","apple","cookie"]))