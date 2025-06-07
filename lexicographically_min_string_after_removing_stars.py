from collections import defaultdict
def clearStars(s):
    freq = defaultdict(list)
    for i, ch in enumerate(s):
        if ch.isalpha():
            freq[ch].append(i)
        else:
            smallest = min(freq)
            freq[smallest].pop()
            if len(freq[smallest]) == 0:
                del freq[smallest]
    idx = []
    for v in freq.values():
        idx.extend(v)
    idx.sort()
    ans = []
    for i in idx:
        ans.append(s[i])
    return ''.join(ans)
print(clearStars("d*yed"))