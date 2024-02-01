def minimumLengthEncoding(words):
    s = ''
    words.sort(key=len, reverse=True)
    for i in words:
        if i + '#' not in s:
            s += i + '#'
    return len(s)