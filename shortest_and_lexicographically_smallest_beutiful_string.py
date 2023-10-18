def shortestBeautifulSubstring(s, k):
    if k == 1 and s.count('1') != 0:
        return '1'
    s = s.lstrip('0').rstrip('0')
    left = 0
    count_ones = 0
    right = 0
    st = ''
    res = []
    l = len(s)
    while right < len(s):
        st += s[right]
        if s[right] == '1':
            count_ones += 1
            if count_ones == 2:
                left = right
        if count_ones == k:
            l = min(l, len(st))
            res.append(st)
            st = '1'
            count_ones = 1
            right = left
        right += 1
    r = list(filter(lambda x: len(x) == l, res))
    return sorted(r)[0] if r else ''
print(shortestBeautifulSubstring("0000000000", 1))