def maxEqualRowsAfterFlips(matrix):
    pattern_freq = {}
    for row in matrix:
        if row[0] == 1:
            for i in range(len(row)):
                if row[i] == 0:
                    row[i] = 1
                else:
                    row[i] = 0
        r = tuple(row)
        pattern_freq[r] = pattern_freq.get(r, 0) + 1
    return max(pattern_freq.values())
print(maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]]))
