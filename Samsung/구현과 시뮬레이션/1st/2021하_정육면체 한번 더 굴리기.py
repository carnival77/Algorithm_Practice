import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]

#  우,하,좌,상
dx=[0,1,0,-1]
dy=[1,0,-1,0]

a=[0,1,5,3,4,2,6]
ans=0
d=0
sx,sy=0,0

def move(d):
    global sx,sy,a
    
    b=[0]*7
    
    # 우
    if d==0:
        b[4]=a[6]
        b[3]=a[1]
        b[1]=a[4]
        b[6]=a[3]
        b[5]=a[5]
        b[2]=a[2]
    # 하
    elif d==1:
        b[2] = a[6]
        b[1] = a[2]
        b[5] = a[1]
        b[6] = a[5]
        b[3] = a[3]
        b[4] = a[4]
    # 좌
    elif d==2:
        b[6] = a[4]
        b[1] = a[3]
        b[4] = a[1]
        b[3] = a[6]
        b[5] = a[5]
        b[2] = a[2]
    # 상
    else:
        b[6] = a[2]
        b[2] = a[1]
        b[1] = a[5]
        b[5] = a[6]
        b[3] = a[3]
        b[4] = a[4]
    
    a=b
    sx,sy=sx+dx[d],sy+dy[d]

def inBoard(nx,ny):
    return 0<=nx<n and 0<=ny<n

def bfs(sx,sy,tg):
    global ans

    visit=[[False]*n for _ in range(n)]
    q=deque()
    q.append([sx,sy])
    visit[sx][sy]=True
    ans+=tg

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and not visit[nx][ny] and board[nx][ny]==tg:
                visit[nx][ny]=True
                q.append([nx,ny])
                ans+=tg

for t in range(m):
    # 주사위 이동
    if t==0:
        pass
    else:
        if a[6]>board[sx][sy]:
            d=(d+1)%4
        elif a[6]<board[sx][sy]:
            d=(d-1)%4
    nx,ny=sx+dx[d],sy+dy[d]
    if not inBoard(nx,ny):
        d=(d+2)%4
    move(d)
    
    # 점수 획득
    bfs(sx,sy,board[sx][sy])

print(ans)