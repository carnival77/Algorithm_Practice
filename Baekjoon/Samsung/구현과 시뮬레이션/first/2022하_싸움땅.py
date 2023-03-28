import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
pmap=[[[] for _ in range(n)] for _ in range(n)]
gmap=[[[] for _ in range(n)] for _ in range(n)]
pos=[]
points=[]

class Player:
    def __init__(self,no,x,y,d,s,g=0):
        self.no=no
        self.x=x
        self.y=y
        self.d=d
        self.s=s
        self.g=g

dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(n):
    row=list(map(int,input().split()))
    for j in range(n):
        gmap[i][j].append(row[j])

for no in range(m):
    x,y,d,s=map(int,input().split())
    x,y=x-1,y-1
    pos.append([x,y])
    pmap[x][y].append(Player(no,x,y,d,s))
    points.append(0)

def move(nx,ny,player):
    global pmap,pos
    pmap[nx][ny].append(player)
    pmap[player.x][player.y].remove(player)
    player.x,player.y=nx,ny
    pos[player.no]=[player.x,player.y]
    return player

def lose(x,y,player):
    global gmap
    if player.g!=0:
        gmap[x][y].append(player.g)
    player.g=0
    return player

def get(x,y,player):
    global gmap
    lost_player=lose(x,y,player)
    tg=max(gmap[x][y])
    lost_player.g=tg
    gmap[x][y].remove(tg)
    return lost_player

for _ in range(k):
    for ax,ay in pos:
        me=pmap[ax][ay][0]
        me_nx=ax+dx[me.d]
        me_ny=ay+dy[me.d]
        if not (0<=me_nx<n and 0<=me_ny<n):
            me.d=(me.d+2)%4
            me_nx=ax+dx[me.d]
            me_ny=ay+dy[me.d]
        me = move(me_nx, me_ny, me)
        if pmap[me_nx][me_ny][0]==me:
            if len(gmap[me.x][me.y])>=1:
                me=get(me.x,me.y,me)
        else:
            bx,by=me.x,me.y
            other=pmap[bx][by][0]
            me_sum=me.s+me.g
            other_sum=other.s+other.g
            if me_sum>other_sum:
                winner=me
                loser=other
            elif me_sum<other_sum:
                winner=other
                loser=me
            else:
                if me.s>other.s:
                    winner=me
                    loser=other
                else:
                    winner=other
                    loser=me
            points[winner.no]+=abs(me_sum-other_sum)
            loser=lose(loser.x,loser.y,loser)
            loser_nx,loser_ny=loser.x+dx[loser.d],loser.y+dy[loser.d]
            ok=False
            if not (0 <= loser_nx < n and 0 <= loser_ny < n):
                ok=True
            else:
                if len(pmap[loser_nx][loser_ny]) != 0:
                    ok=True
            if ok:
                while True:
                    loser.d=(loser.d+1)%4
                    loser_nx,loser_ny=loser.x+dx[loser.d],loser.y+dy[loser.d]
                    if 0<=loser_nx<n and 0<=loser_ny<n:
                        if len(pmap[loser_nx][loser_ny])==0:
                            break
            loser=move(loser_nx,loser_ny,loser)
            if len(gmap[loser.x][loser.y])>=1:
                loser=get(loser.x,loser.y,loser)
            winner=get(bx,by,winner)
print(*points)