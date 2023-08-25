def canMakeSubsequence(str1, str2):
    n1, n2 = len(str1), len(str2)
    i1 = i2 = 0
    while i1 < n1 and i2 < n2:
        if str1[i1] == 'z' and str2[i2] == 'a':
            i2 += 1
        elif chr(ord(str1[i1]) + 1) == str2[i2] or str1[i1] == str2[i2]:
            i2 += 1
        i1 += 1
    return n2 == i2
print(canMakeSubsequence("dm", "e"))