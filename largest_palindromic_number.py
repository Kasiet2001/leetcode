def largestPalindromic(num):
    s = sorted(set(num))
    left, middle, right = '', '', ''
    for i in s:
        n = num.count(i)
        left = i * (n // 2) + left
        right += i * (n // 2)
        if n % 2 > 0:
            middle = max(middle, i)
    return left + middle + right
print(largestPalindromic("6006"))