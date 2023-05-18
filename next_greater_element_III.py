def nextGreaterElement(n):
    n = list(str(n))
    i = len(n) - 1
    while i > 0 and n[i - 1] >= n[i]:
        i -= 1
    if i == 0:
        return -1
    j = len(n) - 1
    while j > i - 1 and n[j] <= n[i - 1]:
        j -= 1
    n[i - 1], n[j] = n[j], n[i - 1]
    n[i:] = n[i:][::-1]
    ans = int(''.join(n))
    return ans if ans < 2 ** 31 else -1
print(nextGreaterElement(12374987))
