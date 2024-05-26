def compressedString(word):
    i, n, str1 = 0, len(word), ""
    while i < n:
        j, count = i, 0
        while j < n and word[i] == word[j] and count < 9:
            count += 1
            j += 1
        str1 += str(count) + word[i]
        i = j
    return str1
print(compressedString("abcde"))


