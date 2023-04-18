def replaceWords(dictionary, sentence):
    s = sentence.split()
    dict = sorted(dictionary, key=lambda x: (len(x), x))
    for i in range(len(dict)):
        for j in range(len(s)):
            if len(dict[i]) <= len(s[j]) and dict[i] == s[j][:len(dict[i])]:
                s[j] = dict[i]
    return ' '.join(s)
print(replaceWords(["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))
