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

FILES = ("a","b","c","d","e","f","g","h")
PIECES = {
    W_QUEEN  //2: "q",
    W_ROOK   //2: "r",
    W_BISHOP //2: "b",
    W_KNIGHT //2: "n"
}

def get_move_notation(b, b2, r, c, r2, c2):
    s = f"{FILES[c]}{r+1}{FILES[c2]}{r2+1}"
    if b[r][c]//2==5 and r2%7==0: # pawn reaches 0 or 7 rank 
        s += f"={PIECES[b2[r2][c2]//2]}"
    return s

NT=lambda b,B,r,c,R,C:f"{FILES[c]}{r+1}{FILES[c2]}{r2+1}"
