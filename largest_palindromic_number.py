def largestPalindromic(num):
    if len(num.strip('0')) == 0:
        return '0'
    num = sorted(num)
    d = {}
    ans = []
    for i in num:
        d[i] = d.get(i, 0) + 1
    for k, v in d.items():
        if v // 2 > 0:
            ans.insert(0, k * (v // 2))
            ans.append(k * (v // 2))
        d[k] = v % 2
    m = [k for k, v in d.items() if v > 0]
    if len(m) > 0:
        ans.insert(len(ans) // 2, max(m))
    return ''.join(ans).strip('0')
print(largestPalindromic("987650000"))