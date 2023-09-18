import sys
from collections import deque
input=sys.stdin.readline

n,l,r=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
visited=[]
ans=0

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def bfs(sx,sy):
    global visited,a,ok

    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=True
    s=a[sx][sy]
    cnt=1
    union=[(sx,sy)]

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and not visited[nx][ny] and l<=abs(a[nx][ny]-a[x][y])<=r:
                q.append((nx,ny))
                visited[nx][ny]=True
                s+=a[nx][ny]
                cnt+=1
                union.append((nx,ny))
                ok=True

    for x,y in union:
        a[x][y]=s//cnt

for time in range(2001):
    ok=False
    visited=[[False]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if visited[x][y]:
                continue
            bfs(x,y)
    if not ok:
        ans=time
        break

print(ans)