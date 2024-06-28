def maximumImportance(n, roads):
    freq = [0] * n
    for a, b in roads:
        freq[a] += 1
        freq[b] += 1
    freq.sort()
    val = 1
    ans = 0
    for f in freq:
        ans += val * f
        val += 1
    return ans
print(maximumImportance(5, [[0,1]]))