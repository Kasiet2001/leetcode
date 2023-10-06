def maxScore(s):
    ones = s.count('1')
    zeros = 0
    ans = 0
    for i in range(len(s) - 1):
        if s[i] == '0':
            zeros += 1
        else:
            ones -= 1
        ans = max(ans, zeros + ones)
    return ans
print(maxScore("00"))