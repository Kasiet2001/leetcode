def decrypt(code, k):
    result = [0] * len(code)
    if k == 0:
        return result
    for i in range(len(result)):
        if k > 0:
            for j in range(i + 1, i + k + 1):
                result[i] += code[j % len(code)]
        else:
            for j in range(i - abs(k), i):
                result[i] += code[(j + len(code)) % len(code)]
    return result
print(decrypt([5,7,1,4], 3))