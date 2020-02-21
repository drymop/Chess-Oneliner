from move_gen import is_checked, gen_move
from heuristic import heuristic

INF = 1e6

def negamax(board, depth, a, b, player):
    if depth == 0:
        return (player*heuristic(board),0)
    moves = gen_move(board, player < 0)
    if not moves:
        if is_checked(board, player < 0):
            return (-INF,0)
        else:
            return (0,0)
    v = -INF
    best = None
    for i, (brd2,*_) in enumerate(moves):
        v2, _ = negamax(brd2,depth-1,-b,-a,-player)
        if -v2 > v:
            best = i
            v = -v2
            a = max(a, v)
            if a >= b:
                break
    return (v, best)