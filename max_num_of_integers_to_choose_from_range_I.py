def maxCount(banned, n, maxSum):
    ans = 0
    total = 0
    b = banned
    for i in range(1, n + 1):
        if total + i > maxSum:
            break
        elif i not in b:
            total += i
            ans += 1
    return ans
print(maxCount([1,6,5], 5, 6))