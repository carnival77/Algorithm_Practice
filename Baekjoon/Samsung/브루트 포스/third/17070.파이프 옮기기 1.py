import sys
input=sys.stdin.readline

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def check(nx,ny):
    if inBoard(nx,ny) and a[nx][ny]!=1:
        return True
    return False

def dfs(hx,hy,kind):

    ans=0
    if (hx,hy)==(n-1,n-1):
        return 1

    if kind==1 or kind==3:
        # 가로
        nx,ny=hx,hy+1
        if check(nx,ny):
            ans+=dfs(nx,ny,1)
    if kind==2 or kind==3:
        #세로
        nx,ny=hx+1,hy
        if check(nx,ny):
            ans += dfs( nx, ny,2)
    #대각선
    nx,ny=hx+1,hy+1
    if check(nx,ny) and check(hx+1,hy) and check(hx,hy+1):
        ans += dfs(nx, ny,3)

    return ans

if a[n-1][n-1]==1:
    print(0)
    sys.exit(0)
print(dfs(0,1,1))