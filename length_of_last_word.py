def lengthOfLastWord(s):
    last = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ' and last == 0:
            continue
        if s[i] == ' ' and last:
            return last
        if s[i].isalpha():
            last += 1
    return last


print(lengthOfLastWord("   fly me   to   the moon  "))