def firstUniqChar(s):
    dict = {}
    for i in s:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    index = -1
    for k, v in dict.items():
        if v == 1:
            return s.index(k)
    return -1


    """dict = {}
    for i in s:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    index = -1
    for i in range(len(s)):
        if dict[s[i]] == 1:
            index = i
            break
    return index"""
print(firstUniqChar("loveleetcode"))