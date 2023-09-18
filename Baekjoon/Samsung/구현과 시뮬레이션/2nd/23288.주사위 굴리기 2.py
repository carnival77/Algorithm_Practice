import sys
from collections import deque
input=sys.stdin.readline

n,m,k=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]

ans,x,y,d=0,0,0,0
dice=[1,2,3,4,5,6]

#  우,하,좌,상
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<m:
        return True
    return False

def bfs(sx,sy,tg):
    res=1
    q=deque()
    q.append((sx,sy))
    visited=[[False]*m for _ in range(n)]
    visited[sx][sy]=True

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if not inBoard(nx,ny) or a[nx][ny]!=tg or visited[nx][ny]:
                continue
            visited[nx][ny]=True
            q.append((nx,ny))
            res+=1

    return res

for _ in range(k):

    # 1. 주사위 이동
    nx, ny = x + dx[d], y + dy[d]
    if not inBoard(nx, ny):
        d = (d + 2) % 4
        nx, ny = x + dx[d], y + dy[d]
    x, y = nx, ny

    if d == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif d == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif d == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

    # 2. 점수 획득
    ans+=bfs(x,y,a[x][y])*a[x][y]

    # 3. 이동방향 결정
    if dice[5]>a[x][y]:
        d=(d+1)%4
    elif dice[5]<a[x][y]:
        d=(d-1)%4

print(ans)