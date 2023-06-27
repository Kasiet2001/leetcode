def reverseOnlyLetters(s):
    alphabets = [i for i in s if i.isalpha()][::-1]
    for i in range(len(s)):
        if not s[i].isalpha():
            alphabets.insert(i, s[i])
    return ''.join(alphabets)
print(reverseOnlyLetters("ab-cd"))