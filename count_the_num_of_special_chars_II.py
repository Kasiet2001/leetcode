def numberOfSpecialChars(word):
    low = dict()
    upper = dict()
    for i, ch in enumerate(word):
        if ch.islower():
            low[ch] = i
        elif ch.isupper() and ch not in upper:
            upper[ch] = i
    ans = 0
    for k, v in low.items():
        n = k.upper()
        if n in upper and v < upper[n]:
            ans += 1
    return ans
print(numberOfSpecialChars("AbBCab"))