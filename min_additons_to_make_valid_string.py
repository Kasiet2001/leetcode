def addMinimum(word):
    n = len(word)
    curr = 0
    ans = 0
    while curr < n:
        count = 0
        if word[curr] == 'a':
            count += 1
            curr += 1
        if curr < n and word[curr] == 'b':
            count += 1
            curr += 1
        if curr < n and word[curr] == 'c':
            count += 1
            curr += 1
        ans += 3 - count
    return ans
print(addMinimum("aaa"))