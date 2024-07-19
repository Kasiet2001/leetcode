def luckyNumbers (matrix):
    cols = list(zip(*matrix))
    ans = []
    for r in matrix:
        min_in_row = min(r)
        for c in range(len(r)):
            if min_in_row == max(cols[c]):
                ans.append(min_in_row)
    return ans
print(luckyNumbers([[7,8],[1,2]]))