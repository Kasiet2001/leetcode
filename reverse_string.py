def reverseString(s):
    for i in reversed(range(len(s))):
        s.append(s[i])
    return s[len(s)//2:]
print(reverseString(["h","e","l","l","o"]))