from print_board import *
from move_gen_minified import GM as gen_move
from notation import get_move_notation

PLAYERS = ["White", "Black"]

def get_user_move(b,moves):
    move_notations = {get_move_notation(b,m[0],*m[1],*m[2]):m for m in moves}
    print(">> ", end="")
    return move_notations.get(input().strip().lower(),None)

def main():
    b = [[4,8,6,2,0,6,8,4],[10]*8,[-1]*8,[-1]*8,[-1]*8,[-1]*8,[11]*8,[5,9,7,3,1,7,9,5]]
    color = 0
    moves = gen_move(b,color)
    while True:
        print(chr(27) + "c") # clear screen
        print_board(b)
        print()
        if not moves:
            print("Game over")
            break
        print(f"{PLAYERS[color]}'s turn:")
        print(len(moves))
        m = get_user_move(b,moves)
        if m:
            b = m[0]
            color = 1-color
            moves = gen_move(b,color)

if __name__ == '__main__':
    main()