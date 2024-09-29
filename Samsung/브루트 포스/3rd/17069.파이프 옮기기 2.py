import sys
input=sys.stdin.readline

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
d=[[[-1]*3 for _ in range(n)] for _ in range(n)]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def check(nx,ny):
    if inBoard(nx,ny) and a[nx][ny]!=1:
        return True
    return False

def dfs(x,y,k):
    global d

    if d[x][y][k]!=-1:
        return d[x][y][k]

    ans=0
    if (x,y)==(n-1,n-1):
        return 1

    if k==0 or k==2:
        # 가로
        nx,ny=x,y+1
        if check(nx,ny):
            ans+=dfs(nx,ny,0)
    if k==1 or k==2:
        #세로
        nx,ny=x+1,y
        if check(nx,ny):
            ans += dfs( nx, ny,1)
    #대각선
    nx,ny=x+1,y+1
    if check(nx,ny) and check(x+1,y) and check(x,y+1):
        ans += dfs(nx, ny,2)

    d[x][y][k]=ans
    return ans

if a[n-1][n-1]==1:
    print(0)
    sys.exit(0)
print(dfs(0,1,0))