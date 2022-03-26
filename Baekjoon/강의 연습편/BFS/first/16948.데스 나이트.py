from collections import deque
n=int(input())
data = list(map(int,input().split()))
r1,c1,r2,c2 = data
move_type = [(-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)]

d=list([-1] * n for _ in range(n))
d[r1][c1]=0
q=deque()
q.append((r1,c1))

while q:
    x,y = q.popleft()
    for move in move_type:
        nx=x+move[0]
        ny=y+move[1]
        if 0<=nx<n and 0<=ny<n and d[nx][ny]==-1:
            q.append((nx,ny))
            d[nx][ny] = d[x][y] + 1

print(d[r2][c2])