import sys
input=sys.stdin.readline

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
ans=0

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def dfs(x,y,d):
    global ans

    if (x,y)==(n-1,n-1):
        ans+=1
        return

    # 가로
    if d == 0:
        # 가로
        if 0 <= y + 1 < n and a[x][y + 1] != 1:
            dfs(x, y + 1, 0)
        # 대각선
        if 0 <= x + 1 < n and 0 <= y + 1 < n and a[x + 1][y + 1] != 1 and a[x][y + 1] != 1 and a[x + 1][y] != 1:
            dfs(x + 1, y + 1, 2)
    # 세로
    elif d == 1:
        # 세로
        if 0 <= x + 1 < n and a[x + 1][y] != 1:
            dfs(x + 1, y, 1)
        # 대각선
        if 0 <= x + 1 < n and 0 <= y + 1 < n and a[x + 1][y + 1] != 1 and a[x][y + 1] != 1 and a[x + 1][y] != 1:
            dfs(x + 1, y + 1, 2)
    # 대각선
    elif d == 2:
        # 가로
        if 0 <= y + 1 < n and a[x][y + 1] != 1:
            dfs(x, y + 1, 0)
        # 세로
        if 0 <= x + 1 < n and a[x + 1][y] != 1:
            dfs(x + 1, y, 1)
        # 대각선
        if 0 <= x + 1 < n and 0 <= y + 1 < n and a[x + 1][y + 1] != 1 and a[x][y + 1] != 1 and a[x + 1][y] != 1:
            dfs(x + 1, y + 1, 2)

if a[n - 1][n - 1] == 1:
    print(0)
    sys.exit(0)
dfs(0,1,0)
print(ans)