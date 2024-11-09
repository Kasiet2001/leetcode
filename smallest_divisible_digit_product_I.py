def smallestNumber(n, t):
    while True:
        m = str(n)
        a = 1
        for i in m:
            a *= int(i)
            if int(a) % t == 0:
                return n
        n += 1
print(smallestNumber(15, 3))