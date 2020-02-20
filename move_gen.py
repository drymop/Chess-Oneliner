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

# EMPTY    = 0
# W_KING   = 1
# W_QUEEN  = 2
# W_ROOK   = 3
# W_BISHOP = 4
# W_KNIGHT = 5
# W_PAWN   = 6
# B_QUEEN  = 8
# B_ROOK   = 9
# B_BISHOP = 10
# B_KNIGHT = 11
# B_PAWN   = 12

CARDINAL_DIRS = [(0,1),(0,-1),(1,0),(-1,0)]
DIAGONAL_DIRS = [(1,1),(-1,1),(1,-1),(-1,-1)]
QUEEN_DIRS = CARDINAL_DIRS  + DIAGONAL_DIRS
APPLICABLE_PIECE = {**{d:(W_QUEEN,W_ROOK) for d in CARDINAL_DIRS},**{d:(W_QUEEN,W_BISHOP) for d in DIAGONAL_DIRS}}
KNIGHT_DIRS = ((1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1))
FORWARD = (1, -1) # forward direction for white, black

def initialize_board():
    return [
        [W_ROOK,W_KNIGHT,W_BISHOP,W_QUEEN,W_KING,W_BISHOP,W_KNIGHT,W_ROOK],
        [W_PAWN]*8,
        [EMPTY]*8,[EMPTY]*8,[EMPTY]*8,[EMPTY]*8,
        [B_PAWN]*8,
        [B_ROOK,B_KNIGHT,B_BISHOP,B_QUEEN,B_KING,B_BISHOP,B_KNIGHT,B_ROOK],
    ]

def is_out(r,c):
    return 2-(0<=r<8)-(0<=c<8)

# @param color Color of the attacker, 0 for white, 1 for black
def is_controlled(b,r,c,color):
    # Sliding pieces
    print("%s %s" % (r, c))
    for x,y in QUEEN_DIRS:
        r2,c2 = r+x,c+y
        if not is_out(r2,c2) and b[r2][c2]-color == W_KING:
            print("Checked by king at %s %s" % (r2, c2))
            return True
        for i in range(1,8):
            r2 = r+i*x
            c2 = c+i*y
            if is_out(r2,c2):
                break
            if b[r2][c2]-color in APPLICABLE_PIECE[x,y]:
                print("Checked by slide at %s %s" % (r2, c2))
                return True
            if b[r2][c2]>=0: # not empty
                break
    # Knight
    for x,y in KNIGHT_DIRS:
        r2,c2 = r+x,c+y
        if not is_out(r2, c2) and b[r2][c2]-color == W_KNIGHT:
            print("Checked by knight at %s %s" % (r2, c2))
            return True
    # Pawn
    r2 = r-FORWARD[color]
    for y in (-1, 1):
        c2 = c+y
        if not is_out(r2,c2) and b[r2][c2]-color == W_PAWN:
            print("Checked by pawn at %s %s" % (r2, c2))
            return True
    return False

if __name__ == '__main__':
    from print_board import print_board
    b = initialize_board()
    for c in range(8):
        b[1][c] = EMPTY
        b[6][c] = EMPTY
    print_board(b)
    is_controlled(b,3,0,1)
    is_controlled(b,3,1,1)
    is_controlled(b,3,2,1)
    is_controlled(b,3,3,1)
    is_controlled(b,3,4,1)
    is_controlled(b,3,5,1)
    is_controlled(b,3,6,1)
    is_controlled(b,3,7,1)
