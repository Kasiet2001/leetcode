def shortestToChar(s, c):
    char_idx = [i for i, ch in enumerate(s) if ch == c]
    ans = []
    for i in range(len(s)):
        curr_idx = float('inf')
        for idx in char_idx:
            if abs(i - idx) < curr_idx:
                curr_idx = abs(i - idx)
        ans.append(curr_idx)
    return ans
print(shortestToChar("loveleetcode", 'e'))