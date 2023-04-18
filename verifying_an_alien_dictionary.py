def isAlienSorted(words, order):
    c = {ch: i for i, ch in enumerate(order)}
    prev = [c[ch] for ch in words[0]]
    for i in range(1, len(words)):
        cur = [c[ch] for ch in words[i]]
        if cur < prev:
            return False
        prev = cur
    return True
print(isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
