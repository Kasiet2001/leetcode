class neighborSum:
    def __init__(self, grid):
        self.grid = grid

    def find_value(self, value):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.grid[r][c] == value:
                    return r, c
        return None, None

    def adjacent_sum(self, value: int):
        row, col = self.find_value(value)
        if row is None or col is None:
            return None

        res = 0
        if row > 0:
            res += self.grid[row - 1][col]
        if row < len(self.grid) - 1:
            res += self.grid[row + 1][col]
        if col > 0:
            res += self.grid[row][col - 1]
        if col < len(self.grid[0]) - 1:
            res += self.grid[row][col + 1]
        return res

    def diagonal_sum(self, value: int):
        row, col = self.find_value(value)
        if row is None or col is None:
            return None
        res = 0
        if row > 0 and col > 0:
            res += self.grid[row - 1][col - 1]
        if row > 0 and col < len(self.grid[0]) - 1:
            res += self.grid[row - 1][col + 1]
        if row < len(self.grid) - 1 and col > 0:
            res += self.grid[row + 1][col - 1]
        if row < len(self.grid) - 1 and col < len(self.grid[0]) - 1:
            res += self.grid[row + 1][col + 1]
        return res

