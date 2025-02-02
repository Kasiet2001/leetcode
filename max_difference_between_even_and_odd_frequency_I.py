def maxDifference(s):
    freq = dict()
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    max_odd = 0
    min_odd = float('inf')
    max_even = 0
    min_even = float('inf')
    for v in freq.values():
        if v % 2 == 0:
            max_even = max(max_even, v)
            min_even = min(min_even, v)
        else:
            max_odd = max(max_odd, v)
            min_odd = min(min_odd, v)
    res1 = max_odd - min_even
    res2 = min_odd - max_even
    return max(res1, res2)
print(maxDifference("tzt"))