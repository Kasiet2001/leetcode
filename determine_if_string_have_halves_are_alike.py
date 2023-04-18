def halvesAreAlike(s):
    a = [s[i] for i in range(len(s) // 2) if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]
    b = [s[i] for i in range(len(s) // 2, len(s)) if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]
    return len(a) == len(b)
print(halvesAreAlike("book"))
