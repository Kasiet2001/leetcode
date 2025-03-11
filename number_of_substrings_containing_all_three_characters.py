def numberOfSubstrings(s):
    n = len(s)
    left = 0
    charMap = [0] * 3
    ans = 0
    for i in range(n):
        charMap[ord(s[i]) - ord('a')] += 1
        while all(f > 0 for f in charMap):
            ans += n - i
            charMap[ord(s[left]) - ord('a')] -= 1
            left += 1
    return ans
print(numberOfSubstrings("abcabc"))

