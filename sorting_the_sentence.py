def sortSentence(s):
    w = s.split()
    w = sorted(w, key=lambda x: int(x[-1]))
    w = [i[:-1] for i in w]
    return ' '.join(w)
print(sortSentence("is2 sentence4 This1 a3"))