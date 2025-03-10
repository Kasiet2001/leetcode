def largestCombination(candidates):
    count = [0] * 32
    for n in candidates:
        i = 0
        while n > 0:
            count[i] += 1 & n
            i += 1
            n = n >> 1
    return max(count)
print(largestCombination([16,17,71,62,12,24,14]))