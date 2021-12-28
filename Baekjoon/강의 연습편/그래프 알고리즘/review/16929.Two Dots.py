# solution 1. 각 칸을 방문했을 때, 시작점으로부터의 거리(개수)를 기록해서 4이상이면 사이클 존재.

import sys

n,m = map(int,input().split())

dx=[1,-1,0,0]
dy=[0,0,1,-1]

a=[input() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]

def dfs(x,y,cnt,color):
    if visited[x][y]:
        return cnt-dist[x][y] >= 4
    visited[x][y]=True
    dist[x][y] = cnt
    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if a[nx][ny] == color:
                if dfs(nx,ny,cnt+1,color):
                    return True

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        dist = [[0] * m for _ in range(n)]
        if dfs(i,j,1,a[i][j]):
            print('Yes')
            sys.exit(0)
print('No')

# solution 2.
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