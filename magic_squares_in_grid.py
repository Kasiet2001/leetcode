def numMagicSquaresInside(grid):
    if len(grid) < 3 or len(grid[0]) < 3:
        return 0
    rows, cols = len(grid), len(grid[0])

    def magic(r, c):
        g = []
        values = set()
        for i in range(r, r + 3):
            row = []
            for j in range(c, c + 3):
                if grid[i][j] in values or not (1 <= grid[i][j] <= 9):
                    return 0
                values.add(grid[i][j])
                row.append(grid[i][j])
            g.append(row)
        for i in range(len(g)):
            if sum(g[i]) != 15:
                return 0
        if g[0][0] + g[1][1] + g[2][2] != 15 or g[2][0] + g[1][1] + g[0][2] != 15:
            return 0
        g = list(zip(*g))
        for i in range(len(g)):
            if sum(g[i]) != 15:
                return 0
        return 1
    res = 0
    for r in range(rows - 2):
        for c in range(cols - 2):
            res += magic(r, c)
    return res
print(numMagicSquaresInside([[5,5,5],[5,5,5],[5,5,5]]))