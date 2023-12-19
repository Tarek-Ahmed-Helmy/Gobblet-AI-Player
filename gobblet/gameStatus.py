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





    return False  # Return None if there's no winner


def can_play(board, rowS, colS, Gcolor):
    #checking the desired place is empty or having a gobblet of the same color
    if board[rowS][colS].isEmpty() or board[rowS][colS].peek().color == Gcolor:
        return True
    else:
        color = board[rowS][colS].peek().color;
        rowCounter = 0;
        #checking if the opponent is close to win from the row
        for col in board[rowS]:
            if not(col.isEmpty()) and col.peek().color == color:
                rowCounter += 1;
        if rowCounter == 3 :
            for col in board[rowS]:
                if(col.isEmpty()):
                    return True

        # checking if the opponent is close to win from the column
        columnCounter = 0;
        columnArray = [board[row][colS] for row in range(1,5)]
        for row in columnArray:
            if not(row.isEmpty()) and row.peek().color == color:
                columnCounter += 1;
        if columnCounter == 3 :
            for row in columnArray:
                if (row.isEmpty()):
                    return True

        # checking if the gobblet in the main diagonal and is close to win from it
        if rowS == colS + 1:
            main_diagonal = [board[i + 1][i] for i in range(4)]
            diagonalCounter = 0
            for square in main_diagonal:
                if not (square.isEmpty()) and square.peek().color == color:
                    diagonalCounter += 1;
            if diagonalCounter == 3:
                for square in main_diagonal:
                    if (square.isEmpty()):
                        return True

        # checking if the gobblet in the secondary diagonal and is close to win from it
        elif rowS + colS == 4:
            secondary_diagonal = [board[i][4 - i] for i in range(1, 5)]
            diagonalCounter = 0
            for square in secondary_diagonal:
                if not (square.isEmpty()) and square.peek().color == color:
                    diagonalCounter += 1;
            if diagonalCounter == 3:
                for square in secondary_diagonal:
                    if (square.isEmpty()):
                        return True

    return False    # Return None if the opponent is not about to win



