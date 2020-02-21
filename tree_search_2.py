from heuristic import heuristic as FH
from move_gen import is_checked as Fc
from move_gen import gen_move as GM

# recursive function, board, moves, depth, alpha, beta, player (1 or -1)
NM=lambda f,b,M,d,A,B,p,D={}:\
    d==0 and(p*FH(b),0)or not M and(Fc(b,p<0)and (-1e6,0)or(0,0))or D.update({0:-1e7,1:-1,2:A,3:B})or\
    [D.update({4:-f(f,m[0],GM(m[0],p>0),d-1,-D[3],-D[2],-p,{})[0]})or D[4]<=D[0]or\
    D.update({0:D[4],1:i,2:max(D[2],D[4])})
    for i,m in enumerate(M)]and(D[0],D[1])