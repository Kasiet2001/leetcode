from collections import Counter
def minDeletions(s):
    ch = Counter(s)
    ans = 0
    used = set()
    for char, freq in ch.items():
        while freq > 0 and freq in used:
            ans += 1
            freq -= 1
        used.add(freq)
    return ans
print(minDeletions("ceabaacb"))
