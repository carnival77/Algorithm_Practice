import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())
a=[[0]*n for _ in range(n)] # 사람 위치 맵
arrive=[None]+[False]*m # 사람별 도착 여부
pos=[None] # 사람별 현재 위치
goal=[None] # 사람별 목표 편의점 위치
b=[list(map(int,input().split())) for _ in range(n)] # 장소 위치 맵. 0 : 빈 공간, -1 : 베이스캠프. 1~30 : 사람별 목표 편의점, -2 : 출입금지
for x in range(n):
    for y in range(n):
        if b[x][y]==1:
            b[x][y]=-1
for no in range(1,m+1):
    x,y=map(int,input().split())
    x-=1
    y-=1
    b[x][y]=no
    pos.append([-1,-1])
    goal.append([x,y])

#  상,좌,우,하
dx=[-1,0,0,1]
dy=[0,-1,1,0]

def check():
    if False not in arrive:
        return True
    return False

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def bfs1(sx,sy,tx,ty):

    q=deque()
    q.append((sx,sy))
    d=[[-1]*n for _ in range(n)]
    d[sx][sy]=0

    parent=dict()

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and d[nx][ny]==-1 and b[nx][ny]!=-2:
                q.append((nx,ny))
                d[nx][ny]=d[x][y]+1
                parent[(nx,ny)]=(x,y)

    start=(sx,sy)
    end=(tx,ty)
    current=end
    route=[current]
    while current!=start:
        current=parent[current]
        route.append(current)
    route.reverse()

    return route[1]

def bfs2(sx,sy):

    q=deque()
    q.append((sx,sy))
    d=[[-1]*n for _ in range(n)]
    d[sx][sy]=0

    cand=[]

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and d[nx][ny]==-1 and b[nx][ny]!=-2:
                q.append((nx,ny))
                d[nx][ny]=d[x][y]+1
                if b[nx][ny]==-1:
                    cand.append([d[nx][ny],[nx,ny]])

    cand.sort()
    return cand[0][1]

def move(kind,t):
    global a,pos

    if kind==1:
        for no in range(1,m+1):
            if arrive[no] or pos[no]==[-1,-1]:
                continue
            x,y=pos[no]
            tx,ty=goal[no]
            nx,ny=bfs1(x,y,tx,ty)
            a[x][y]=0
            pos[no]=[nx,ny]
            a[nx][ny]=no
    else:
        if t<=m:
            no=t
            x,y=goal[no]
            tx,ty=bfs2(x,y)
            b[tx][ty]=-2
            a[tx][ty] = no
            pos[no]=[tx,ty]

def finish():
    global arrive

    for x in range(n):
        for y in range(n):
            if a[x][y]==b[x][y] and 1<=b[x][y]<=m:
                b[x][y]=-2
                no=a[x][y]
                arrive[no]=True

time=0
while True:

    time += 1

    # 편의점으로 이동
    move(1,time)
    # 편의점 도착 여부
    finish()
    # 베이스 캠프 입장
    move(2,time)

    if check():
        break

print(time)