def buddyStrings(s, goal):
    ans = []
    if len(s) != len(goal):
        return False
    if s == goal:
        return len(set(s)) < len(s)
    for i in range(len(s)):
        if s[i] != goal[i]:
            ans.append((s[i], goal[i]))
    return len(ans) == 2 and ans[0] == ans[1][::-1]
print(buddyStrings("abcaa", "abcbb"))