def divide(dividend, divisor):
    neg = ((dividend < 0) != (divisor < 0))
    dividend = left = abs(dividend)
    divisor = div = abs(divisor)
    r = 1
    ans = 0
    while left >= divisor:
        left -= div
        ans += r
        r += r
        div += div
        if left < div:
            div = divisor
            r = 1
    if neg:
        return max(-ans, -2147483648)
    else:
        return min(ans, 2147483647)

print(divide(-7, -3))