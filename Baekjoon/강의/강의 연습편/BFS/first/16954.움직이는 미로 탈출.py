# solution 1. 참고 :  https://chelseashin.tistory.com/m/77
from collections import deque
import sys

move_types=[(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(0,0)]
a=deque(list(input()) for _ in range(8))
cx,cy=7,0
q=deque()
q.append((cx,cy))
time=0

while q:
    check = [[False] * 8 for _ in range(8)]

    for _ in range(len(q)):
        x,y=q.popleft() # 캐릭터 현재 위치
        if x==0 and y==7:
            print(1)
            sys.exit(0)
        if a[x][y]=='#':
            continue
        for k in range(9):
            nx,ny=x+move_types[k][0],y+move_types[k][1]
            if 0<=nx<8 and 0<=ny<8 and a[nx][ny]=='.' and not check[nx][ny]:
                q.append((nx,ny))
                check[nx][ny]=True

    a.pop()
    a.appendleft(['.', '.', '.', '.', '.', '.', '.', '.'])

    time+=1
    if time==9:
        print(1)
        sys.exit(0)

print(0)

# solution 2.
from collections import deque
dx = [0,0,1,-1,1,-1,1,-1,0]
dy = [1,-1,0,0,1,1,-1,-1,0]
n = 8
a = [input() for _ in range(n)]
q = deque()
check = [[[False]*(n+1) for j in range(n)] for i in range(n)]
check[7][0][0] = True
q.append((7,0,0))
ans = False

while q:
    x,y,t = q.popleft()
    if x == 0 and y == 7:
        ans = True
    for k in range(9):
        nx,ny = x+dx[k],y+dy[k]
        nt = min(t+1, 8)
        if 0 <= nx < n and 0 <= ny < n:
            if nx-t >= 0 and a[nx-t][ny] == '#':
                continue
            if nx-t-1 >= 0 and a[nx-t-1][ny] == '#':
                continue
            if check[nx][ny][nt] == False:
                check[nx][ny][nt] = True
                q.append((nx,ny,nt))

print(1 if ans else 0)