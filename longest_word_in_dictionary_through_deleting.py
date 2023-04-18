def findLongestWord(s, dictionary):
    dict = sorted(dictionary, key=lambda x: (-len(x), x))
    for i in dict:
        it = iter(s)
        if all(c in it for c in i):
            return i
    return ''
print(findLongestWord("abce", ["abe","abc"]))