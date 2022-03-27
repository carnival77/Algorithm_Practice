# 이전에 방문했던 점을 다음으로 갈 점으로 도달하게 된다면 사이클이 존재한다.

dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m = map(int,input().split())
a = [input() for _ in range(n)]
check = [[False]*m for _ in range(n)]
def go(x, y, px, py, color):
    # 이전에 방문했던 점을 다음으로 갈 점으로 도달하게 된다면 사이클이 존재한다.
    if check[x][y]:
        return True
    check[x][y] = True
    # 상하좌우
    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        # 범위 내
        if 0 <= nx < n and 0 <= ny < m:
            # 이전에 방문했던 점은 제외
            if (nx,ny) == (px,py):
                continue
            # 다음 갈 점이 같은 색이라면 dfs에 넣고 이동
            if a[nx][ny] == color:
                if go(nx,ny,x,y,color):
                    return True
    # 그 외엔 False. 사이클 존재 X
    return False
for i in range(n):
    for j in range(m):
        if check[i][j]:
            continue
        ok = go(i, j, -1, -1, a[i][j])
        if ok:
            print('Yes')
            exit()
print('No')