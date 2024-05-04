def numberOfSpecialChars(word):
    chars = set()
    visited = set()
    for ch in word:
        if ch.islower() and ch.upper() in chars:
            visited.add(ch)
        elif ch.isupper() and ch.lower() in chars:
            visited.add(ch)
        chars.add(ch)
    return len(visited)
print(numberOfSpecialChars("BBbab"))