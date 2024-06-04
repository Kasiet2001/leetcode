from collections import defaultdict
def clearStars(s):
    idx = defaultdict(list)
    for i, ch in enumerate(s):
        if ch == '*':
            smallest = min(idx)
            idx[smallest].pop()
            if len(idx[smallest]) == 0:
                idx.pop(smallest)
        else:
            idx[ch].append(i)
    ch = []
    for v in idx.values():
        ch.extend(v)
    ch.sort()
    ans = [s[i] for i in ch]
    return ''.join(ans)
print(clearStars("aaba*"))