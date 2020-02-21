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

PIECES = ({W_KING,W_QUEEN,W_ROOK,W_BISHOP,W_KNIGHT,W_PAWN},{B_KING,B_QUEEN,B_ROOK,B_BISHOP,B_KNIGHT,B_PAWN})

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
PAWN_START = (1, 6)
PAWN_MID = (2,5)
PAWN_END = (3, 4)

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

def is_checked(b,color):
    k = [(i,j)for i in range(8) for j in range(8) if b[i][j]-color==W_KING][0]
    return is_controlled(b,*k,1-color)

# @param color Color of the attacker, 0 for white, 1 for black
def is_controlled(b,r,c,color):
    # print("%s %s" % (r, c))
    # Sliding pieces
    for x,y in QUEEN_DIRS:
        r2,c2 = r+x,c+y
        if not is_out(r2,c2) and b[r2][c2]-color == W_KING:
            # print("Checked by king at %s %s" % (r2, c2))
            return True
        for i in range(1,8):
            r2 = r+i*x
            c2 = c+i*y
            if is_out(r2,c2):
                break
            if b[r2][c2]-color in APPLICABLE_PIECE[x,y]:
                # print("Checked by slide at %s %s" % (r2, c2))
                return True
            if b[r2][c2]>=0 and b[r2][c2]!=B_KING-color: # not empty and not opponent king
                break
    # Knight
    for x,y in KNIGHT_DIRS:
        r2,c2 = r+x,c+y
        if not is_out(r2, c2) and b[r2][c2]-color == W_KNIGHT:
            # print("Checked by knight at %s %s" % (r2, c2))
            return True
    # Pawn
    r2 = r-FORWARD[color]
    for y in (-1, 1):
        c2 = c+y
        if not is_out(r2,c2) and b[r2][c2]-color == W_PAWN:
            # print("Checked by pawn at %s %s" % (r2, c2))
            return True
    return False

# @param  b     The board
# @oaram  color Color of the moving player (0 for white, 1 for black)
# @return List of next states, each is a tuple of (move, board)
# def gen_moves(b,color):

def gen_king_move(b,r,c,color):
    moves = []
    # normal move
    for x,y in QUEEN_DIRS:
        r2,c2=r+x,c+y
        if is_out(r2,c2) or b[r2][c2] in PIECES[color] or is_controlled(b,r2,c2,1-color):
            continue
        b2 = [[b[r][c] if (i,j)==(r2,c2) else EMPTY if (i,j)==(r,c) else b[i][j] for j in range(8)]for i in range(8)]
        moves.append((b2,(r,c),(r2,c2)))
    # castle: later
    return moves

def gen_slide_move(b,r,c,kr,kc,color,dirs,stop=8):
    moves = []
    for x,y in dirs:
        for i in range(1, stop):
            r2, c2 = r+i*x, c+i*y
            if is_out(r2,c2) or b[r2][c2] in PIECES[color]:
                break
            b2 = [[b[r][c] if (i,j)==(r2,c2) else EMPTY if (i,j)==(r,c) else b[i][j] for j in range(8)]for i in range(8)]
            if not is_controlled(b2,kr,kc,1-color):
                moves.append((b2,(r,c),(r2,c2)))
            if b[r2][c2]>=0: break
    return moves

def gen_pawn_move(b,r,c,kr,kc,color):
    moves = []
    # forward once (possibly promotion)
    r2 = r+FORWARD[color]
    if b[r2][c] == EMPTY:
        b2 = [[b[r][c] if (i,j)==(r2,c) else EMPTY if (i,j)==(r,c) else b[i][j] for j in range(8)]for i in range(8)]
        if not is_controlled(b2,kr,kc,1-color):
            if r2 % 7:
                # not 0 or 7, aka not promotion
                moves.append((b2,(r,c),(r2,c)))
            else:
                # 0 or 7, aka promotion
                for p in range(W_QUEEN, W_PAWN, 2):
                    b2 = [[p+color if (i,j)==(r2,c) else b2[i][j] for j in range(8)]for i in range(8)]
                    moves.append((b2,(r,c),(r2,c)))
    # forward twice
    if r==PAWN_START[color] and b[PAWN_MID[color]][c] == EMPTY and b[PAWN_END[color]][c] == EMPTY:
        b2 = [[b[r][c] if (i,j)==(PAWN_END[color],c) else EMPTY if (i,j)==(r,c) else b[i][j] for j in range(8)]for i in range(8)]
        if not is_controlled(b2,kr,kc,1-color):
            moves.append((b2,(r,c),(PAWN_END[color],c)))
    # diagonal capture
    r2 = r+FORWARD[color]
    for c2 in (c-1, c+1):
        if 0<=c2<8 and b[r2][c2] >= 0 and b[r2][c2]%2!=color:
            b2 = [[b[r][c] if (i,j)==(r2,c2) else EMPTY if (i,j)==(r,c) else b[i][j] for j in range(8)]for i in range(8)]
            if not is_controlled(b2,kr,kc,1-color):
                if r2 % 7:
                    # not 0 or 7, aka not promotion
                    moves.append((b2,(r,c),(r2,c2)))
                else:
                    # 0 or 7, aka promotion
                    for p in range(W_QUEEN, W_PAWN, 2):
                        b2 = [[p+color if (i,j)==(r2,c2) else b2[i][j] for j in range(8)]for i in range(8)]
                        moves.append((b2,(r,c),(r2,c2)))
    # en passant
    # TODO
    return moves

def gen_move(b,color):
    try:
        kr, kc = next((i,j) for i in range(8) for j in range(8) if b[i][j]==W_KING+color)
    except:
        from print_board import print_board
        print_board(b)
    moves = []
    table = {
        W_KING  : lambda r,c: gen_king_move(b,r,c,color),
        W_QUEEN : lambda r,c: gen_slide_move(b,r,c,kr,kc,color,QUEEN_DIRS),
        W_ROOK  : lambda r,c: gen_slide_move(b,r,c,kr,kc,color,CARDINAL_DIRS),
        W_BISHOP: lambda r,c :gen_slide_move(b,r,c,kr,kc,color,DIAGONAL_DIRS),
        W_KNIGHT: lambda r,c :gen_slide_move(b,r,c,kr,kc,color,KNIGHT_DIRS,stop=2),
        W_PAWN  : lambda r,c :gen_pawn_move(b,r,c,kr,kc,color),
    }
    do_nothing = lambda r,c: []
    for i in range(8):
        for j in range(8):
            moves += table.get(b[i][j]-color,do_nothing)(i,j)
    return moves

if __name__ == '__main__':
    from print_board import print_board
    b = initialize_board()
    print_board(b)
    moves = gen_move(b,0)
    for m in moves:
        print(m[2])
        print_board(m[0])