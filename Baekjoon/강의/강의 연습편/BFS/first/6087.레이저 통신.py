# solution.
# BFS의 가중치를 직선의 개수로 설정한다.
# 즉, 시작점부터 해당점까지 도달하기 위해 필요한 직선의 개수를 dist 배열에 업데이트한다.
# 여기서 필요한 직선의 개수 -1 이 필요한 거울 개수의 최솟값이므로 dist 배열의 타겟 지점의 값에서 -1을 해주면 답을 구할 수 있다.
# 가중치가 다르므로, BFS 탐색을 할 때, 각 방향에서 벽을 만나거나 탐색 범위를 벗어나기 전까지의 모든 아직 탐색되지 않은 지점을 탐색하며 각 지점을 큐에 넣는다.

from collections import deque
m,n=map(int,input().split())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

a=[input() for _ in range(n)]

sx,sy,ex,ey=-1,-1,-1,-1

for i in range(n):
    for j in range(m):
        if a[i][j]=='C':
            if sx==-1:
                sx,sy=i,j
            else:
                ex,ey=i,j

q=deque()
q.append((sx,sy))
dist=[[-1]*m for _ in range(n)]
dist[sx][sy]=0

while q:
    x,y=q.popleft()
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        while 0<=nx<n and 0<=ny<m:
            if a[nx][ny]=='*':
                break
            if dist[nx][ny]==-1:
                dist[nx][ny]=dist[x][y]+1
                q.append((nx,ny))
            nx+=dx[k]
            ny+=dy[k]

print(dist[ex][ey]-1)