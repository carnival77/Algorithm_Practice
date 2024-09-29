import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
b=[[0]*m for _ in range(n)]
ans=0

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<m:
        return True
    return False

# def copyBoard(a):
#     return [row[:] for row in a]

def process(x,y):

    ans=0
    s=a[x][y]

    if inBoard(x,y-1) and inBoard(x,y+1) and inBoard(x+1,y):
        ans=max(ans,s+a[x][y-1]+a[x][y+1]+a[x+1][y])
    if inBoard(x,y-1) and inBoard(x,y+1) and inBoard(x-1,y):
        ans = max(ans, s + a[x][y - 1] + a[x][y + 1] + a[x - 1][y])
    if inBoard(x,y-1) and inBoard(x+1,y) and inBoard(x-1,y):
        ans = max(ans, s + a[x][y - 1] + a[x+1][y] + a[x - 1][y])
    if inBoard(x,y+1) and inBoard(x+1,y) and inBoard(x-1,y):
        ans = max(ans, s + a[x][y + 1] + a[x+1][y] + a[x - 1][y])

    return ans

def dfs(x,y,cnt,s,b):

    ans=0

    if cnt==4:
        return s

    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if not inBoard(nx,ny) or b[nx][ny]==1:continue
        b[nx][ny]=1
        cnt+=1
        s+=a[nx][ny]
        ans=max(ans,dfs(nx,ny,cnt,s,b))
        cnt-=1
        s-=a[nx][ny]
        b[nx][ny]=0

    return ans

for x in range(n):
    for y in range(m):
        b[x][y]=1
        ans=max(ans,dfs(x,y,1,a[x][y],b),process(x,y))
        b[x][y]=0

print(ans)