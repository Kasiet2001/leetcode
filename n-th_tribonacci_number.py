def tribonacci(n):
    trib = [0, 1, 1]
    for i in range(2, n):
        num = trib[i] + trib[i - 1] + trib[i - 2]
        trib.append(num)
        if i == n - 1:
            return num
    return trib[n]