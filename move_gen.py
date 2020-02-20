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

def initialize_board():
    return [
        [B_ROOK,B_KNIGHT,B_BISHOP,B_QUEEN,B_KING,B_BISHOP,B_KNIGHT,B_ROOK],
        [B_PAWN]*8,
        [EMPTY]*8,[EMPTY]*8,[EMPTY]*8,[EMPTY]*8,
        [W_PAWN]*8,
        [W_ROOK,W_KNIGHT,W_BISHOP,W_QUEEN,W_KING,W_BISHOP,W_KNIGHT,W_ROOK]
    ]

if __name__ == '__main__':
    from print_board import print_board
    print_board(initialize_board())