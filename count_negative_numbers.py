def countNegatives(grid):
    return sum([1 for i in grid for j in i if j < 0])
print(countNegatives([[3,2],[1,0]]))