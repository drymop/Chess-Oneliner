EMPTY    = -1
W_KING   = 0
B_KING   = 1
W_QUEEN  = 2
B_QUEEN  = 3
W_ROOK   = 4
B_ROOK   = 5
W_BISHOP = 6
B_BISHOP = 7
W_KNIGHT = 8
B_KNIGHT = 9
W_PAWN   = 10
B_PAWN   = 11

# print stuff
BOARD_TEMPLATE_STR = \
"""     +---+---+---+---+---+---+---+---+
  8  | %s | %s | %s | %s | %s | %s | %s | %s |
     +---+---+---+---+---+---+---+---+
  7  | %s | %s | %s | %s | %s | %s | %s | %s |
     +---+---+---+---+---+---+---+---+
  6  | %s | %s | %s | %s | %s | %s | %s | %s |
     +---+---+---+---+---+---+---+---+
  5  | %s | %s | %s | %s | %s | %s | %s | %s |
     +---+---+---+---+---+---+---+---+
  4  | %s | %s | %s | %s | %s | %s | %s | %s |
     +---+---+---+---+---+---+---+---+
  3  | %s | %s | %s | %s | %s | %s | %s | %s |
     +---+---+---+---+---+---+---+---+
  2  | %s | %s | %s | %s | %s | %s | %s | %s |
     +---+---+---+---+---+---+---+---+
  1  | %s | %s | %s | %s | %s | %s | %s | %s |
     +---+---+---+---+---+---+---+---+
       a   b   c   d   e   f   g   h"""

# ASCII_PIECE_STR =   [" ", "k", "q", "r", "b", "n", "p", "K", "Q", "R", "B", "N", "P"]
# UNICODE_PIECE_STR = [" ", "\u2654", "\u2655","\u2656","\u2657","\u2658","\u2659","\u265A","\u265B","\u265C","\u265D","\u265E","\u265F"]
ASCII_PIECE_STR =   ["k","K","q","Q","r","R","b","B","n","N","p","P"," "]
UNICODE_PIECE_STR = ["\u2654","\u265A","\u2655","\u265B","\u2656","\u265C","\u2657","\u265D","\u2658","\u265E","\u2659","\u265F"," "]
PIECE_STR = UNICODE_PIECE_STR
def print_board(board):
    print("     +---+---+---+---+---+---+---+---+\n  8  | %s | %s | %s | %s | %s | %s | %s | %s |\n     +---+---+---+---+---+---+---+---+\n  7  | %s | %s | %s | %s | %s | %s | %s | %s |\n     +---+---+---+---+---+---+---+---+\n  6  | %s | %s | %s | %s | %s | %s | %s | %s |\n     +---+---+---+---+---+---+---+---+\n  5  | %s | %s | %s | %s | %s | %s | %s | %s |\n     +---+---+---+---+---+---+---+---+\n  4  | %s | %s | %s | %s | %s | %s | %s | %s |\n     +---+---+---+---+---+---+---+---+\n  3  | %s | %s | %s | %s | %s | %s | %s | %s |\n     +---+---+---+---+---+---+---+---+\n  2  | %s | %s | %s | %s | %s | %s | %s | %s |\n     +---+---+---+---+---+---+---+---+\n  1  | %s | %s | %s | %s | %s | %s | %s | %s |\n     +---+---+---+---+---+---+---+---+\n       a   b   c   d   e   f   g   h" % tuple(PIECE_STR[p] for row in reversed(board) for p in row))


PB = lambda b:print()


if __name__ == '__main__':
    # board[row][col] with A1 being (0, 0), H8 being (0, 7)
    board = [[EMPTY]*8 for _ in range(8)]
    board[0][0] = W_KING
    board[7][0] = B_KING
    print_board(board)