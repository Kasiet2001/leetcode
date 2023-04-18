def commonChars(words):
    w = list(words[0])
    for word in words:
        characters = []
        for c in word:
            if c in w:
                characters.append(c)
                w.remove(c)
        w = characters
    return w
print(commonChars(["cool","lock","cook"]))