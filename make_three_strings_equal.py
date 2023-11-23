def findMinimumOperations(s1, s2, s3):
    common = 0
    minn_len = min(len(s1), len(s2), len(s3))
    total_len = len(s1) + len(s2) + len(s3)
    for i in range(minn_len):
        if s1[i] == s2[i] == s3[i]:
            common += 3
        else:
            break
    return total_len - common if common > 0 else -1
print(findMinimumOperations("b", "aba", "aaccaa"))