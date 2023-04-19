def countBattleships(board):
    ans = 0
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            if col - 1 >= 0:
                left = board[row][col - 1]
            else:
                left = '.'
            if row - 1 >= 0:
                right = board[row - 1][col]
            else:
                right = '.'
            if board[row][col] == 'X' and left != 'X' and right != 'X':
                ans += 1
    return ans
print(countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))