import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
ans=0
c=[[False]*m for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<m:
        return True
    return False

def dfs(x,y,sum,cnt):
    global ans

    if not inBoard(x,y):
        return

    if c[x][y]:
        return

    if cnt==4:
        ans=max(ans,sum)
        return

    c[x][y]=True

    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        dfs(nx,ny,sum+a[x][y],cnt+1)

    c[x][y]=False

for x in range(n):
    for y in range(m):
        dfs(x,y,0,0)
        if y+2<=m-1:
            tmp=a[x][y]+a[x][y+1]+a[x][y+2]
            if x+1<=n-1:
                ans=max(ans,tmp+a[x+1][y+1])
            if x-1>=0:
                ans=max(ans,tmp+a[x-1][y+1])
        if x+2<=n-1:
            tmp = a[x][y] + a[x+1][y] + a[x+2][y]
            if y + 1 <= m - 1:
                ans = max(ans, tmp + a[x + 1][y + 1])
            if y - 1 >= 0:
                ans = max(ans, tmp + a[x + 1][y - 1])

print(ans)