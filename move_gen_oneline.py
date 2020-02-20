# directions of rook, bishop, queen, knight,pawn
Dr = [(0,1),(0,-1),(1,0),(-1,0)]
Db = [(1,1),(-1,1),(1,-1),(-1,-1)]
Dq = Dr  + Db
Dn = ((1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1))
Dp = (1,-1) # pawn Dp direction for white, black
# map queen directions to the appropriate piece (queen, rook, or bishop)
DM = {**{d:(2,4)for d in Dr},**{d:(2,6)for d in Db}}
R8 = range(8) # save characters
R7 = range(1,8) # save characters
# piece of each color
PC = ({0,2,4,6,8,10},{1,3,5,7,9,11})
P1 = (1,6)
P2 = (2,5)
P3 = (3,4)

# is_in: check out of bound
# Return True or False
FI=lambda r,c:0<=r<8 and 0<=c<8

# is_out: check out of bound
# Return 1 or 0
FO=lambda r,c:1-FI(r,c)

# is_controlled
# board,row,col,player
# P[0], P[1] is used to store position r2,c2
# Return True or False
FC=lambda b,r,c,p,P=[]:\
any((
    # king
    any(FI(r+x,c+y) and b[r+x][c+y]-p==0 for x,y in Dq),
    # sliding pieces
    any(
        (any(
            # True to break
            FO(r+i*x,c+i*y)or P.clear()or P.append(b[r+i*x][c+i*y])or P[0]+1 and P[0]+p!=1
            for i in R7
        ),)and P and P.pop()-p in DM[x,y]
        for x,y in Dq
    ),
    # knights
    any(FI(r+x,c+y) and b[r+x][c+y]-p==8 for x,y in Dn),
    # pawns
    any(FI(r-Dp[p],C) and b[r-Dp[p]][C]-p==10 for C in (c-1,c+1))
))

# make_move
# board, (row,col), (newRow,newCol)
FM=lambda b,r,c,R,C:[[b[r][c] if (i,j)==(R,C)else -1 if (i,j)==(r,c)else b[i][j]for j in R8] for i in R8]

# generate king moves
# board, row, col, player,list of moves
# return False
# TODO Castling
Gk=lambda b,r,c,p,M:not[FO(R,C)or b[R][C]in PC[p]or FC(b,R,C,1-p)or M.append((FM(b,r,c,R,C),(r,c),(R,C)))for x,y in Dq for R,C in[(r+x,c+y)]]

# Generate sliding moves
# board, row, col, kingPos, player, Dirs, Moves, stop
# return False
Gs=lambda b,r,c,k,p,D,M,s=8,B=[]:\
    not[any( # search for each direction
        # True to break
        FO(R,C)or b[R][C]in PC[p]or B.append(FM(b,r,c,R,C))or 
        1-FC(B[0],*k,1-p)and M.append((B[0],(r,c),(R,C)))or B.clear()or ~b[R][C]
        for i in range(1,s)for R,C in[(r+i*x,c+i*y)]
    ) for x,y in D]

# Generate promotion moves if available and valid
# New board, row, col, new row, new col, kingPos, player, Moves
# Return Falsy
GP=lambda B,r,c,R,C,k,p,M:\
    1-FC(B,*k,1-p)and(R%7 or M.extend(([[P+p if (i,j)==(R,C)else B[i][j]for j in R8]for i in R8],(r,c),(R,C))for P in range(2,10,2))) and M.append((B,(r,c),(R,C)))

# generate_pawn_moves
# board, row, col, kingPos, plaer, Moves
# Return False
Gp=lambda b,r,c,k,p,M,B=[]:\
    not(
        GP(FM(b,r,c,r+Dp[p],c),r,c,r+Dp[p],c,k,p,M), # forward 1
        r!=P1[p]or b[P2[p]][c]>=0 or b[P3[p]][c]>=0 or B.append(FM(b,r,c,P3[p],c))or\
            FC(B[0],*k,1-p)and B.pop()or M.append((B.pop(),(r,c),(P3[p],c))), # forward 2
        any(GP(FM(b,r,c,R,C),r,c,R,C,k,p,M)for C in(c-1,c+1)for R in(r+Dp[p],) if 0<=C<8 and b[R][C]in PC[1-p]),
        # TODO En passant
    )

# Generate move
# board, player, temp to store kingPos, temp to store move list
GM=lambda b,p,K=[],M=[]:\
    K.append([(i,j)for i in R8 for j in R8 if b[i][j]==p][0])or M.append([])or\
    print("here")or any( 
        {
            0:lambda r,c:Gk(b,r,c,p,M[0]),
            2:lambda r,c:Gs(b,r,c,K[0],p,Dq,M[0]),
            4:lambda r,c:Gs(b,r,c,K[0],p,Dr,M[0]),
            6:lambda r,c:Gs(b,r,c,K[0],p,Db,M[0]),
            8:lambda r,c:Gs(b,r,c,K[0],p,Dn,M[0],2),
            10:lambda r,c:Gp(b,r,c,K[0],p,M[0]),
        }.get(b[i][j]-p,lambda r,c:0)(i,j) for i in R8 for j in R8
    )or print("here2")or K.clear()or M.pop()