class Spreadsheet:

    def __init__(self, rows):
        self.rows = rows
        self.spreadsheet = [[0] * 26 for _ in range(self.rows)]

    def setCell(self, cell, value):
        col = ord(cell[0]) - 65
        row = int(cell[1:]) - 1
        self.spreadsheet[row][col] = value

    def resetCell(self, cell):
        col = ord(cell[0]) - 65
        row = int(cell[1:]) - 1
        self.spreadsheet[row][col] = 0

    def getValue(self, formula):
        formula = formula[1:]
        tokens = formula.split('+')
        total = 0
        for token in tokens:
            token = token.strip()
            if token[0].isdigit():
                total += int(token)
            else:
                col = ord(token[0]) - 65
                row = int(token[1:]) - 1
                if 0 <= row < self.rows:
                    total += self.spreadsheet[row][col]
        return total