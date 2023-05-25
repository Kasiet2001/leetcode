def removeDuplicateLetters(s):
    ans = []
    last_occ = {}
    visited = set()
    for i in range(len(s)):
        last_occ[s[i]] = i
    for i in range(len(s)):
        if s[i] not in visited:
            while ans and ans[-1] > s[i] and last_occ[ans[-1]] > i:
                visited.remove(ans.pop())
            ans.append(s[i])
            visited.add(s[i])
    return ''.join(ans)
print(removeDuplicateLetters("bcabc"))