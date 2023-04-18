def numberOfMatches(n):
    ''' :return n - 1'''
    m = 0
    while n != 1:
        if n % 2 != 0:
            n //= 2
            m += 1 + n
        else:
            n //= 2
            m += n
    return m
print(numberOfMatches(14))
