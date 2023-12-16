def check_winner(realBorad):
    # Check rows for a winner
    board = realBorad[1:5];
    for row in board:
        if not (row[0].isEmpty()):
            color = row[0].peek().color;
            return all(not(row[col].isEmpty()) and row[col].peek().color == color for col in range(1, len(row)))

    # Check columns for a winner
    for col in range(len(board[0])):
        columnArray = [board[row][col] for row in range(4)]
        if not (columnArray[0].isEmpty()):
            color = columnArray[0].peek().color;
            return all(not(columnArray[row].isEmpty()) and columnArray[row].peek().color == color for row in range(1, len(columnArray)))

    return False  # Return None if there's no winne