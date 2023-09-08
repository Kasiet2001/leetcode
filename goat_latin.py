def toGoatLatin(sentence):
    s = sentence.split()
    vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    n = len(s)
    for i in range(n):
        if s[i][0] in vow:
            s[i] += 'ma'
        else:
            s[i] = s[i][1:] + s[i][0] + 'ma'
        s[i] += 'a' * (i + 1)
    return ' '.join(s)
print(toGoatLatin("I speak Goat Latin"))