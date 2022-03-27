# 안전 거리의 최댓값은, 각 0의 위치에서 상어가 나올 때까지 bfs를 전개하는 것이다.
#!/usr/bin/python3
import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

a=[]

for _ in range(n):
    a.append(list(map(int,input().split())))

dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]

# bfs

def bfs(x,y):
    # 거리
    d = [[-1] * m for _ in range(n)]
    d[x][y] = 0
    q=deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for k in range(8):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if d[nx][ny] == -1:
                    if a[nx][ny] == 1:
                        return d[x][y]+1
                    else:
                        q.append((nx,ny))
                        d[nx][ny] = d[x][y]+1
    return 0

ans=-1

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            dist = bfs(i,j)
            if dist > ans:
                ans = dist

print(ans)