def circularGameLosers(n, k):
    start = 0
    visited = set()
    p = 1
    while start not in visited:
        visited.add(start)
        start += p * k
        start = start % n
        p += 1
    ans = []
    for i in range(n):
        if i not in visited:
            ans.append(i + 1)
    return ans

print(circularGameLosers(4, 4))
