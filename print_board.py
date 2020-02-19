EMPTY    = 0
W_KING   = 1
W_QUEEN  = 2
W_ROOK   = 3
W_BISHOP = 4
W_KNIGHT = 5
W_PAWN   = 6
B_KING   = 7
B_QUEEN  = 8
B_ROOK   = 9
B_BISHOP = 10
B_KNIGHT = 11
B_PAWN   = 12

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
       A   B   C   D   E   F   G   H"""

ASCII_PIECE_STR =   [" ", "k", "q", "r", "b", "n", "p", "K", "Q", "R", "B", "N", "P"]
UNICODE_PIECE_STR = [" ", "\u2654", "\u2655","\u2656","\u2657","\u2658","\u2659","\u265A","\u265B","\u265C","\u265D","\u265E","\u265F"]
PIECE_STR = UNICODE_PIECE_STR
def print_board(board):
    print(BOARD_TEMPLATE_STR % tuple(PIECE_STR[p] for row in reversed(board) for p in row))

# board[row][col] with A1 being (0, 0), H8 being (0, 7)
board = [[EMPTY]*8 for _ in range(8)]
board[0][0] = W_KING
board[7][0] = B_KING
print_board(board)