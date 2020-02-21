from print_board import *
from move_gen_2 import GM as gen_move
from notation import get_move_notation
from tree_search_2 import NM as negamax

PLAYERS = ["White","Black"]
DEPTH = 3

def get_user_move(b,moves):
    move_notations = {get_move_notation(b,m[0],*m[1],*m[2]):m for m in moves}
    print(">> ", end="")
    return move_notations.get(input().strip().lower(),None)

def get_com_move(b,moves):
    print("... Thinking ...")
    v, best = negamax(negamax,b,moves,DEPTH,-1e6,1e6,-1)
    return moves[best]

def get_move(b,moves,color):
    if color:
        return get_com_move(b,moves)
        # return get_user_move(b,moves)
    else:
        return get_user_move(b,moves)


def main():
    b = fasdfasd
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
        m = get_move(b,moves,color)
        if m:
            b = m[0]
            color = 1-color
            moves = gen_move(b,color)

if __name__ == '__main__':
    main()



D.update({0:[[4,8,6,2,0,6,8,4],[10]*8,[-1]*8,[-1]*8,[-1]*8,[-1]*8,[11]*8,[5,9,7,3,1,7,9,5]],1:0})or D.update({2,GM(D[0],D[1])})or any(
        print(chr(27)+"c")or PB(D[0])or print()or not(input(),)
        for _ in iter(int,1))

MU,MC
(lambda b,M:print(">> ", end="")or{NT(b,m[0],*m[1],*m[2]):m for m in M}.get(input().strip().lower(),0)),(lambda b,M:print("... Thinking ...")or M[NM(NM,b,M,2,-1e6,1e6,-1)[1]])


NM
lambda f,b,M,d,A,B,p,D={}:d==0 and(p*HF(b),0)or not M and(Fc(b,p<0)and (-1e6,0)or(0,0))or D.update({0:-1e7,1:-1,2:A,3:B})or[D.update({4:-f(f,m[0],GM(m[0],p>0),d-1,-D[3],-D[2],-p,{})[0]})or D[4]<=D[0]or D.update({0:D[4],1:i,2:max(D[2],D[4])})for i,m in enumerate(M)]and(D[0],D[1])