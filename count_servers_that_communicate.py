def countServers(grid):
    rows = dict()
    cols = dict()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                rows[i] = rows.get(i, 0) + 1
                cols[j] = cols.get(j, 0) + 1
    isolated = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                isolated += 1
    servers = sum(sum(i) for i in grid)
    return servers - isolated
print(countServers([[1,0],[0,1]]))
