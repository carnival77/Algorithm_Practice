# 가능한 방법의 수가 제한이 없다.
# 따라서, 32x32 모양의 격자이므로 칸의 최대 개수는 1024에,
# (0,0),(0,1)칸을 제외하고 각 칸에 (x,y)가 오는 경우/아닌 경우 2가지를 곱하여 구해지는
# 모든 경우의 수는 대략 2^1022 일 것 같다.
# 따라서, 브루트 포스가 아닌 dp를 사용한 백트랙킹을 적용하여 탐색 경우의 수 가짓수를 줄여야 한다.
# d는 [x][y][direction] 의 3차원 배열로, 파이프 헤드가 (x,y) 칸에 있고 파이프 방향이 direction인 칸에서 (n,n)칸까지 탐색 성공하는 경우의 수를 저장한다.

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
# d: (n,n) 칸까지의 성공적인 탐색 루트에, 포함되지 않아 탐색이 필요한 칸 = -1,
# 이미 포함되어 해당 칸부터의 탐색에 의해 도출될 수 있는 정답의 수가 이미 저장되어 더 이상의 탐색이 무의미한 칸 != -1
d=[[[-1]*3 for j in range(n)] for i in range(n)]
x,y=0,1

# 파이프 헤드가 (x,y) 칸에 있고 파이프 방향이 direction인 칸에서 (n,n)칸까지 탐색 성공하는 경우의 수 ans 반환
def dfs(x,y,direction):
    global a,n
    if (x,y)==(n-1,n-1):
        return 1
    ok=d[x][y][direction]
    # (n,n) 칸까지의 성공적인 탐색 루트에
    # 이미 포함되어 해당 칸부터의 탐색에 의해 도출될 수 있는 정답의 수가 이미 저장되어 더 이상의 탐색이 무의미하면 -1,
    # 그렇지 않으면 -1이 아님.
    if ok!=-1:
        return ok
    ans = 0
    # 가로
    if direction==0:
        # 가로
        if 0<=y+1<n and a[x][y+1]!=1:
            ans+=dfs(x,y+1,0)
        # 대각선
        if 0<=x+1<n and 0<=y+1<n and a[x+1][y+1]!= 1 and a[x][y+1]!=1 and a[x+1][y]!=1:
            ans+=dfs(x+1,y+1,2)
    # 세로
    elif direction==1:
        # 세로
        if 0 <= x+1 < n and a[x+1][y]!=1:
            ans+=dfs(x+1, y,1)
        # 대각선
        if 0 <= x + 1 < n and 0 <= y + 1 < n and a[x+1][y+1]!= 1 and a[x][y+1]!=1 and a[x+1][y]!=1:
            ans+=dfs(x + 1, y + 1,2)
    # 대각선
    elif direction==2:
        # 가로
        if 0<=y+1<n and a[x][y+1]!=1:
            ans+=dfs(x,y+1,0)
        # 세로
        if 0 <= x+1 < n and a[x+1][y]!=1:
            ans+=dfs(x+1, y,1)
        # 대각선
        if 0 <= x + 1 < n and 0 <= y + 1 < n and a[x+1][y+1]!= 1 and a[x][y+1]!=1 and a[x+1][y]!=1:
            ans+=dfs(x + 1, y + 1,2)
    d[x][y][direction]=ans
    return ans
print(dfs(x,y,0))