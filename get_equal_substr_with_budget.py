def equalSubstring(s, t, maxCost):
    ans = 0
    left = 0
    currCost = 0
    for right in range(len(s)):
        currCost += abs(ord(s[right]) - ord(t[right]))
        while currCost > maxCost:
            currCost -= abs(ord(s[left]) - ord(t[left]))
            left += 1
        ans = max(ans, right - left + 1)
    return ans
print(equalSubstring("vjlqwkzamvyv", "suusjpqkhlkz", 7))