def lengthOfLongestSubstring(s):
    l = []
    ch = ''
    for i in s:
        if i not in ch:
            ch += i
        else:
            ch = ch[ch.index(i) + 1:] + i
        if len(ch) > l:
            l = len(ch)
    return l
print(lengthOfLongestSubstring("pwwkew"))

