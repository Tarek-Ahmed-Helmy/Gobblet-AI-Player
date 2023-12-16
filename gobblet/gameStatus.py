def check_winner(realBorad):
    # Check rows for a winner
    board = realBorad[1:5];
    for row in board:
        if not (row[0].isEmpty()):
            color = row[0].peek().color;
            if (all(not(row[col].isEmpty()) and row[col].peek().color == color for col in range(1, len(row)))):
                return True;

    # Check columns for a winner
    for col in range(len(board[0])):
        columnArray = [board[row][col] for row in range(4)]
        if not (columnArray[0].isEmpty()):
            color = columnArray[0].peek().color;
            if(all(not(columnArray[row].isEmpty()) and columnArray[row].peek().color == color for row in range(1, len(columnArray)))):
                return True;

    # Check diagonals (top-left to bottom-right) for a winner
    isBroken = False
    if(not (board[0][0].isEmpty())):
        color = board[0][0].peek().color
        for i, j in zip(range(3), range(3)):
            if (board[i + 1][j + 1].isEmpty()) or not(board[i + 1][j + 1].peek().color == color):
                isBroken = True
                break
        if(not isBroken):
            return True

    # Check diagonals (top-right to bottom-left) for a winner
    isBroken = False
    if (not (board[0][3].isEmpty())):
        color = board[0][3].peek().color
        for i, j in zip(range(4), range(3, -1, -1)):
            if (board[i][j].isEmpty()) or not (board[i][j].peek().color == color):
                isBroken = True
                break
        if (not isBroken):
            return True





    return False  # Return None if there's no winne