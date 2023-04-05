import sys
input=sys.stdin.readline

#  우,하,좌,상
dx=[0,1,0,-1]
dy=[1,0,-1,0]

n,m=map(int,input().split())
a=[[False]*m for _ in range(n)]
ans=0

x,y=0,0
d=0
a[x][y]=True

for _ in range(n*m-1):
    nx,ny=x+dx[d],y+dy[d]
    if not (0<=nx<n and 0<=ny<m) or a[nx][ny]==True:
        d=(d+1)%4
        nx, ny = x + dx[d], y + dy[d]
        ans+=1
    a[nx][ny] = True
    x, y = nx, ny

print(ans)