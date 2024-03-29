import sys
from collections import deque
input=sys.stdin.readline

#  우,하,좌,상
dx=[0,1,0,-1]
dy=[1,0,-1,0]
#  좌상,좌하,우상,우하
dx_=[-1,1,-1,1]
dy_=[-1,-1,1,1]

n,m,T=map(int,input().split())
board=[[[0,0,False] for _ in range(m)] for _ in range(n)]
ax,ay,bx,by,damage=0,0,0,0,0

# input 받기
for x in range(n):
    row=list(map(int,input().split()))
    for y,v in enumerate(row):
        if v==0:
            continue
        board[x][y][0]=v

def select(R):
    global ax,ay,bx,by,damage

    arr=[]
    for x in range(n):
        for y in range(m):
            if board[x][y][0]>0:
                arr.append([board[x][y][0],-board[x][y][1],-(x+y),-y,x])
    arr.sort()
    tmp=arr[0]
    ax,ay=[tmp[-1],-tmp[-2]]
    board[ax][ay][0]+=(n+m)
    board[ax][ay][1]=R
    board[ax][ay][2]=True
    damage=board[ax][ay][0]
    tmp=arr[-1]
    bx,by=[tmp[-1],-tmp[-2]]
    board[bx][by][2]=True

def jump(nx,ny):
    if nx==-1:
        nx=n-1
    elif nx==n:
        nx=0
    if ny==-1:
        ny=m-1
    elif ny==m:
        ny=0
    return [nx,ny]

def bfs():
    d=[[-1]*m for _ in range(n)]
    d[ax][ay]=0
    parent=dict()
    q=deque()
    q.append([ax,ay])
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            nx,ny=jump(nx,ny)
            if board[nx][ny][0]>0 and d[nx][ny]==-1:
                q.append([nx,ny])
                d[nx][ny]=d[x][y]+1
                parent[(nx,ny)]=(x,y)
    if not (bx,by) in parent.keys():
        return -1
    trace=[]
    current=(bx,by)
    start=(ax,ay)
    while current!=start:
        trace.append(current)
        current=parent[current]
    trace.append(start)
    trace.reverse()
    return trace[1:-1]

def laserAttack():
    res=bfs()
    if res==-1:
        return False
    else:
        for x,y in res:
            if board[x][y][0]>0:
                board[x][y][0]-=damage//2
                board[x][y][2]=True
        board[bx][by][0]-=damage
        return True

def cannonAttack():
    board[bx][by][0]-=damage
    x,y=bx,by
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        nx,ny=jump(nx,ny)
        if board[nx][ny][0]>0 and (nx,ny)!=(ax,ay):
            board[nx][ny][0]-=damage//2
            board[nx][ny][2]=True
        nx,ny=x+dx_[k],y+dy_[k]
        nx,ny=jump(nx,ny)
        if board[nx][ny][0]>0 and (nx,ny)!=(ax,ay):
            board[nx][ny][0]-=damage//2
            board[nx][ny][2] = True

def removeAndRepair():
    cnt,ans=0,0
    for x in range(n):
        for y in range(m):
            if board[x][y][0]<=0:
                board[x][y][0]=0
            else:
                if not board[x][y][2]:
                    board[x][y][0]+=1
                cnt+=1
                ans=max(ans,board[x][y][0])
            board[x][y][2]=False
    if cnt==1:
        return [True,ans]
    else:
        return [False,ans]

res=None
for R in range(1,T+1):
    # 1. 공격자,공격대상 선정
    select(R)
    # 2. 공격
    done=laserAttack()
    if not done:
        cannonAttack()
    # 3. 포탑 부서짐, 4. 포탑 정비, 종료 조건
    res=removeAndRepair()
    # 종료 조건
    if res[0]:
        print(res[1])
        sys.exit(0)

print(res[1])