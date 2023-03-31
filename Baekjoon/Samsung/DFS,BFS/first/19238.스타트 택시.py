import sys
from collections import deque
import heapq
input=sys.stdin.readline

n,m,e=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(n)]
pboard=[[-1]*n for _ in range(n)]
tx,ty=map(int,input().split())
tx-=1
ty-=1
dx=[-1,0,1,0]
dy=[0,-1,0,1]

class Psg:
    def __init__(self,x,y,ex,ey):
        self.x=x
        self.y=y
        self.ex=ex
        self.ey=ey

psgs=[]
for no in range(m):
    x,y,ex,ey=map(int,input().split())
    psgs.append(Psg(x-1,y-1,ex-1,ey-1))
    pboard[x-1][y-1]=no

def bfs(sx,sy,ex,ey):
    global psgs,board,n

    q=deque()
    q.append([sx,sy])
    d=[[-1]*n for _ in range(n)]
    d[sx][sy]=0

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if (0<=nx<n and 0<=ny<n) and board[nx][ny]==0 and d[nx][ny]==-1:
                q.append([nx,ny])
                d[nx][ny]=d[x][y]+1
                if (nx,ny)==(ex,ey):
                    return d[nx][ny]

    return -1

def bfs2(sx,sy):
    global pboard,board,n

    if pboard[sx][sy]!=-1:
        return 0,pboard[sx][sy]

    min_dist=-1
    q=deque()
    q.append([sx,sy])
    d=[[-1]*n for _ in range(n)]
    d[sx][sy]=0
    cands=[]
    heapq.heapify(cands)

    while q:
        x,y=q.popleft()
        dist=d[x][y]
        if min_dist!=-1 and dist>=min_dist:
            continue
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if (0<=nx<n and 0<=ny<n) and board[nx][ny]==0 and d[nx][ny]==-1:
                q.append([nx,ny])
                d[nx][ny]=d[x][y]+1
                if pboard[nx][ny]!=-1:
                    min_dist=d[nx][ny]
                    heapq.heappush(cands,[min_dist,nx,ny,pboard[nx][ny]])

    if len(cands)>0:
        res=heapq.heappop(cands)
    else:
        print(-1)
        sys.exit(0)

    return [res[0],res[3]]

def terminate(e,dist):
    if e<dist:
        print(-1)
        sys.exit(0)

def terminate2(dist):
    if dist==-1:
        print(-1)
        sys.exit(0)

for _ in range(m):
    # 택시 -> 승객
    dist,no=bfs2(tx,ty)
    now=psgs[no]
    terminate(e,dist)
    e-=dist
    tx,ty=now.x,now.y

    # 승객 -> 목적지
    dist=bfs(tx,ty,now.ex,now.ey)
    terminate2(dist)
    terminate(e,dist)
    e+=dist
    tx,ty=now.ex,now.ey
    pboard[now.x][now.y]=-1

print(e)