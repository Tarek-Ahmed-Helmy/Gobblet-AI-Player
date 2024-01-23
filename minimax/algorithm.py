from copy import deepcopy
from gobblet.constants import *
from gobblet.board import Board
from gobblet.gameStatus import check_winner

def minimax(boardState, depth, maxPlayer, difficulty):

    if depth == 0 or check_winner(boardState.board) != False:
        return boardState.evaluate(difficulty), boardState
    
    if maxPlayer:
        maxEvaluation = float('-inf')
        bestMove = None
        moves = get_all_moves(boardState, RED)
        for move in moves:
            evaluation = minimax(move, depth-1, False, difficulty)[0]
            maxEvaluation = max(maxEvaluation, evaluation)
            if maxEvaluation == evaluation:
                bestMove = move
        return maxEvaluation, bestMove
    else:
        minEvaluation = float('inf')
        bestMove = None
        moves = get_all_moves(boardState, NAVY)
        for move in moves:
            evaluation = minimax(move, depth-1, True, difficulty)[0]
            minEvaluation = min(minEvaluation, evaluation)
            if minEvaluation == evaluation:
                bestMove = move
        
        return minEvaluation, bestMove


def simulate_move(piece, move, board):
    piece = board.board[piece[0]][piece[1]].pop()
    piece.x = move[1] * SQUARE_SIZE + PADDING + SQUARE_SIZE // 2
    piece.y = (move[0]-1) * SQUARE_SIZE + PADDING + SQUARE_SIZE // 2
    board.board[move[0]][move[1]].push(piece)
    return board


def get_all_moves(board, color):
    moves = []
    for piece in board.get_all_pieces(color):
        validMoves = board.get_valid_moves(piece)
        for move in validMoves:
            temp_board = deepcopy(board)
            temp_piece = piece[0], piece[1]
            new_board = simulate_move(temp_piece, move, temp_board)
            moves.append(new_board)
    
    return moves