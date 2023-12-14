def removeAlmostEqualCharacters(word):
    ans = 0
    left = 0
    right = 1
    while right < len(word):
        if abs(ord(word[left]) - ord(word[right])) < 2:
            ans += 1
            left += 2
            right += 2
        else:
            left += 1
            right += 1
    return ans
print(removeAlmostEqualCharacters("acb"))
