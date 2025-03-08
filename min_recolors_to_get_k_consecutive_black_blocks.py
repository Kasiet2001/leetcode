def minimumRecolors(blocks, k):
    res = float('inf')
    white = 0
    left = 0
    for i in range(len(blocks)):
        if blocks[i] == 'W':
            white += 1
        if i - left == k - 1:
            res = min(res, white)
            if blocks[left] == 'W':
                white -= 1
            left += 1
    return res
print(minimumRecolors("WBWBBBW", 2))
