def maxHeightOfTriangle(red, blue):
    ans = 0
    b1, b2, r1, r2 = 0, 0, 0, 0
    i = 0
    while True:
        if i % 2 == 0:
            b1 += i
            r2 += i
        else:
            b2 += i
            r1 += i
        if (blue >= b1 and red >= r1) or (blue >= b2 and red >= r2):
            ans = i
        else:
            return ans
        i += 1
print(maxHeightOfTriangle(2, 1))