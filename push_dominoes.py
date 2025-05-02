def pushDominoes(dominoes):
    dominoes = list(dominoes)
    l = 0
    n = len(dominoes)
    for r, d in enumerate(dominoes):
        if dominoes[l] == 'L' and dominoes[r] == 'R':
            l = r
        if dominoes[l] == '.':
            if d == 'L':
                while l < r:
                    dominoes[l] = 'L'
                    l += 1
        elif dominoes[l] == 'R' and dominoes[r] == 'L':
            r1 = r
            while l < r1:
                dominoes[l] = 'R'
                dominoes[r1] = 'L'
                r1 -= 1
                l += 1
            l = r
        elif dominoes[l] == d:
            while l < r:
                dominoes[l] = d
                l += 1
        if dominoes[r] != '.':
            l = r
    if l < n - 1 and dominoes[l] == 'R':
        for i in range(l, n):
            dominoes[i] = 'R'
    return ''.join(dominoes)
print(pushDominoes(".R..L."))

