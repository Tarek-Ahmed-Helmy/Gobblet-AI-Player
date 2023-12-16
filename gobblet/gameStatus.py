def check_winner(realBorad):
    # Check rows for a winner
    board = realBorad[1:5];
    for row in board:
        for col in range(len(row) - 3):
            if all(piece == row[col] for piece in row[col:col + 4]) and row[col] != ' ':
                return row[col]

    # Check columns for a winner
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if all(board[row + i][col] == board[row][col] != ' ' for i in range(4)):
                return board[row][col]

    # Check diagonals (top-left to bottom-right) for a winner
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if all(board[row + i][col + i] == board[row][col] != ' ' for i in range(4)):
                return board[row][col]

    # Check diagonals (bottom-left to top-right) for a winner
    for row in range(3, len(board)):
        for col in range(len(board[0]) - 3):
            if all(board[row - i][col + i] == board[row][col] != ' ' for i in range(4)):
                return board[row][col]

    return None  # Return None if there's no winne