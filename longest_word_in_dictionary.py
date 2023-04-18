def longestWord(words):
    words.sort()
    v = {''}
    res = ''
    for word in words:
        if word[:-1] in v:
            v.add(word)
            if len(word) > len(res):
                res = word
    return res
print(longestWord(["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]))