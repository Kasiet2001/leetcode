def greatestLetter(s):
    letters = []
    m = set([i.lower() for i in s])
    for i in m:
        if i in s and i.upper() in s:
            letters.append(i.upper())
    return max(letters) if len(letters) != 0 else ''
print(greatestLetter("AbCdEfGhIjK"))