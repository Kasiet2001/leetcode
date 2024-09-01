def checkTwoChessboards(coordinate1, coordinate2):
    def get_index(coordinate):
        letter, number = coordinate[0], coordinate[1]
        column = ord(letter) - ord('a') + 1
        row = int(number)
        return column + row

    sum1 = get_index(coordinate1)
    sum2 = get_index(coordinate2)

    return sum1 % 2 == sum2 % 2
print(checkTwoChessboards("h7", "c8"))