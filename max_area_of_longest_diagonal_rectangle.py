def areaOfMaxDiagonal(dimensions):
    diagonal = 0
    area = 0
    for l, w in dimensions:
        curr_diag = (l ** 2 + w ** 2) ** 0.5
        if curr_diag > diagonal:
            diagonal = curr_diag
            area = l * w
        elif curr_diag == diagonal:
            area = max(area, l * w)
    return area
print(areaOfMaxDiagonal([[6,5],[8,6],[2,10],[8,1],[9,2],[3,5],[3,5]]))