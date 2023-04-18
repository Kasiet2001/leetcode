def strStr(haystack, needle) -> int:
    s = haystack.replace(needle, " ", 1)
    return s.index(' ') if ' ' in s else -1
print(strStr("butsad","sad"))