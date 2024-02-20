
def lastNonEmptyString(s):
    freq = {}
    ans = ''
    maximum = 0
    for i in s:
        freq[i] = freq.get(i, 0) + 1
        if maximum < freq[i]:
            maximum = freq[i]
            ans = i
        elif maximum == freq[i]:
            ans += i
    return ans
print(lastNonEmptyString("abcd"))