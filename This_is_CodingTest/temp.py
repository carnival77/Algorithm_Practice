from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
m, n = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
q = deque()
dist = [[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            dist[i][j] = 0
            q.append((i,j))
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 0 and dist[nx][ny] == -1:
                q.append((nx,ny))
                dist[nx][ny] = dist[x][y] + 1

for i in range(n):
    print(dist[i])

ans = max([max(row) for row in dist])
for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and dist[i][j] == -1:
            ans = -1
print(ans)
