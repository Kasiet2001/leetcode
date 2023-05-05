def maxVowels(s, k):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    ans = cur_vow = 0
    for i, c in enumerate(s):
        if c in vowels:
            cur_vow += 1
        if i >= k and s[i - k] in vowels:
            cur_vow -= 1
        ans = max(ans, cur_vow)
    return ans
print(maxVowels("abciiidef", 3))