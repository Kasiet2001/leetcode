def isValid(word):
    n = len(word)
    if n < 3:
        return False
    vowels = 0
    cons = 0
    digits = 0
    for i in word:
        i = i.lower()
        if i.isalpha():
            if i in ['a', 'e', 'i', 'o', 'u']:
                vowels += 1
            else:
                cons += 1
        elif i.isdigit():
            digits += 1
        else:
            return False
    if vowels and cons:
        return True
    return digits == n
print(isValid("aya"))