def getLucky(s, k):
    def convert(s):
        return ''.join(str(ord(c) - ord('a') + 1) for c in s)

    def transform(n):
        return sum(int(d) for d in str(n))
    num = convert(s)

    for _ in range(k):
        num = transform(num)

    return num
print(getLucky("leetcode", 2))