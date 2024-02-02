def sequentialDigits(low, high):
    ditigs = '123456789'
    ans = []
    for i in range(10):
        for j in range(i + 1, 10):
            d = int(ditigs[i: j])
            if low <= d <= high:
                ans.append(d)
    return sorted(ans)
print(sequentialDigits(1000, 13000))
