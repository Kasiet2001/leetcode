from collections import defaultdict
def minimumLength(s):
    freq = defaultdict(int)
    for ch in s:
        freq[ch] += 1
        if freq[ch] == 3:
            freq[ch] -= 2
    return sum(freq.values())
print(minimumLength("aa"))