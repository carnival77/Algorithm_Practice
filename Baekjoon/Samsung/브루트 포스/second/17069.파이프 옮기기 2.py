import sys
input=sys.stdin.readline

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
# dp는 [x][y][direction] 의 3차원 배열로, 파이프 헤드가 (x,y) 칸에 있고 파이프 방향이 d인 칸에서 (n,n)칸까지 탐색 성공하는 경우의 수를 저장한다.
dp=[[[-1] * 3 for _ in range(n)] for _ in range(n)]

def dfs(x,y,d):

    if (x,y)==(n-1,n-1):
        return 1

    ok=dp[x][y][d]
    if ok!=-1:
        return ok

    ans=0

    # 가로
    if d == 0:
        # 가로
        if 0 <= y + 1 < n and a[x][y + 1] != 1:
            ans+=dfs(x, y + 1, 0)
        # 대각선
        if 0 <= x + 1 < n and 0 <= y + 1 < n and a[x + 1][y + 1] != 1 and a[x][y + 1] != 1 and a[x + 1][y] != 1:
            ans+=dfs(x + 1, y + 1, 2)
    # 세로
    elif d == 1:
        # 세로
        if 0 <= x + 1 < n and a[x + 1][y] != 1:
            ans+=dfs(x + 1, y, 1)
        # 대각선
        if 0 <= x + 1 < n and 0 <= y + 1 < n and a[x + 1][y + 1] != 1 and a[x][y + 1] != 1 and a[x + 1][y] != 1:
            ans+=dfs(x + 1, y + 1, 2)
    # 대각선
    elif d == 2:
        # 가로
        if 0 <= y + 1 < n and a[x][y + 1] != 1:
            ans+=dfs(x, y + 1, 0)
        # 세로
        if 0 <= x + 1 < n and a[x + 1][y] != 1:
            ans+=dfs(x + 1, y, 1)
        # 대각선
        if 0 <= x + 1 < n and 0 <= y + 1 < n and a[x + 1][y + 1] != 1 and a[x][y + 1] != 1 and a[x + 1][y] != 1:
            ans+=dfs(x + 1, y + 1, 2)

    dp[x][y][d]=ans
    return ans

if a[n - 1][n - 1] == 1:
    print(0)
    sys.exit(0)
ans=dfs(0,1,0)
print(ans)