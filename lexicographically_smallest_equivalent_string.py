from collections import defaultdict
def smallestEquivalentString(s1, s2, baseStr):
    adj = defaultdict(list)
    for ch1, ch2 in zip(s1, s2):
        adj[ch1].append(ch2)
        adj[ch2].append(ch1)

    def dfs(char, visited):
        visited.add(char)
        min_char = char
        for nei in adj[char]:
            if nei not in visited:
                candidate = dfs(nei, visited)
                min_char = min(min_char, candidate)
        return min_char

    ans = []
    for char in baseStr:
        visited = set()
        ans.append(dfs(char, visited))
    return ''.join(ans)
print(smallestEquivalentString("parker", "morris", "parser"))