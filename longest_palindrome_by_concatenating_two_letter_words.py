from collections import defaultdict
def longestPalindrome(words):
    ans = 0
    d = defaultdict(int)
    for i in words:
        if d[i] > 0:
            ans += 4
            d[i] -= 1
        else:
            d[i[::-1]] += 1
    return ans + (2 if any(k[0] == k[1] for k, v in d.items() if v == 1) else 0)
print(longestPalindrome(["mm","mm","yb","by","bb","bm","ym","mb","yb","by","mb","mb","bb","yb","by","bb","yb","my","mb","ym"]))