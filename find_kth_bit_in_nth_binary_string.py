def findKthBit(n, k):
    s = '011'
    prev = '011'
    for i in range(2, n):
        curr = ''
        for num in prev:
            if num == '0':
                curr += '1'
            else:
                curr += '0'
        s += '1' + curr[::-1]
        prev = s
    return s[k]
print(findKthBit(3, 1))