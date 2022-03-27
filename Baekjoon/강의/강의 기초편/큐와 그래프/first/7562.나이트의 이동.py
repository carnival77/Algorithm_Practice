from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]

for _ in range(t):
    n = int(input())
    board=[[0]*n for _ in range(n)]
    dist = [[-1] * n for _ in range(n)]
    a,b = map(int,input().split())
    start = (a,b)
    dist[a][b] = 0
    tg_x,tg_y = map(int,input().split())

    q=deque()
    q.append(start)


    while q:
        x,y = q.popleft()
        for i in range(8):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))

    print(dist[tg_x][tg_y])