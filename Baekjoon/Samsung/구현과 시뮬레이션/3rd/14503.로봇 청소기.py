import sys
input=sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m=map(int,input().split())
x,y,d=map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)]
ans=0

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<m:
        return True
    return False

while True:
    if a[x][y]==0:
        a[x][y]=2
        ans+=1
    cnt=0
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if inBoard(nx,ny) and a[nx][ny]==0:
            cnt+=1
    if cnt>0:
        while True:
            d=(d-1)%4
            nx,ny=x+dx[d],y+dy[d]
            if a[nx][ny]==0:
                x,y=nx,ny
                break
    else:
        nx,ny=x-dx[d],y-dy[d]
        if a[nx][ny]!=1:
            x,y=nx,ny
        else:
            break

print(ans)