def minimumMoves(s):
    ans = 0
    idx = 0
    while idx < len(s):
        if s[idx] == 'X':
            ans += 1
            idx += 3
        else:
            idx += 1
    return ans
print(minimumMoves("XXOX"))