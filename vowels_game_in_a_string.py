def doesAliceWin(s):
    num_of_vowels = 0
    vowels = ('a', 'e', 'i', 'o', 'u')
    for ch in s:
        if ch in vowels:
            num_of_vowels += 1
    return True if num_of_vowels else False
print(doesAliceWin("bbcd"))