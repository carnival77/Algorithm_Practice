from collections import deque
import sys
m,n = map(int,input().split())

board = []

for i in range(n):
    board.append(list(map(int,input().split())))

dist = [[-1] * m for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
ans=0
q=deque()

ok = False
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 :
            ok = True
if ok==False:
    print(0)
    sys.exit(0)

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            dist[i][j]=0
            q.append((i,j))

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] +1
                board[nx][ny] = 1
                q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(-1)
            sys.exit(0)

ans = max([max(row) for row in dist])
print(ans)