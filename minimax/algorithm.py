from copy import deepcopy
from gobblet.constants import *
from gobblet.board import Board
from gobblet.gameStatus import check_winner

def minimax(board_state, depth, max_player):

    if depth == 0 or check_winner(board_state.board) != False:
        return board_state.evaluate(), board_state
    
    if max_player:
        max_evaluation = float('-inf')
        best_move = None
        moves = get_all_moves(board_state, RED)
        for move in moves:
            evaluation = minimax(move, depth-1, False)[0]
            max_evaluation = max(max_evaluation, evaluation)
            if max_evaluation == evaluation:
                best_move = move
        return max_evaluation, best_move
    else:
        min_evaluation = float('inf')
        best_move = None
        moves = get_all_moves(board_state, NAVY)
        for move in moves:
            evaluation = minimax(move, depth-1, True)[0]
            min_evaluation = min(min_evaluation, evaluation)
            if min_evaluation == evaluation:
                best_move = move
        
        return min_evaluation, best_move


def simulate_move(piece, move, board):
    piece = board.board[piece[0]][piece[1]].pop()
    piece.x = move[1] * SQUARE_SIZE + PADDING + SQUARE_SIZE // 2
    piece.y = (move[0]-1) * SQUARE_SIZE + PADDING + SQUARE_SIZE // 2
    board.board[move[0]][move[1]].push(piece)
    return board


def get_all_moves(board, color):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move in valid_moves:
            temp_board = deepcopy(board)
            temp_piece = piece[0], piece[1]
            new_board = simulate_move(temp_piece, move, temp_board)
            moves.append(new_board)
    
    return moves

