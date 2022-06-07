# solution 1. 참고 :  https://chelseashin.tistory.com/m/77
from collections import deque
import sys

move_types=[(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(0,0)]
a=deque(list(input()) for _ in range(8))
cx,cy=7,0
q=deque()
q.append((cx,cy))
time=0

# 큐에 값이 있는 동안
while q:
    # while문을 실행할 때 time 변수 활용을 위해 각 턴을 구분해야 한다.
    # 이를 위해 현재 큐의 길이만큼 for문을 돌리고 check 변수도 새로 선언한다.
    # 이를 통해, 각 초의 턴마다 이동 가능한 지점을 모두 방문하도록 한다.
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
    # 벽을 아래로 움직인다.
    a.pop()
    a.appendleft(['.', '.', '.', '.', '.', '.', '.', '.'])

    time+=1
    if time==9: # 8초 후에는 맵에 벽이 없으므로 탈출 가능 1을 리턴
        print(1)
        sys.exit(0)

print(0)

# solution 2.
# 지도를 총 9개 준비해서, 0초 후, 1초 후, ... , 8초 후의 지도를 만들고 BFS를 수행한다.
# (x,y,t) : t초 시점에 (x,y) 위치
# 실제로 지도를 9개나 만들 필요가 없다. 왜냐하면, 특정 시점인 t초 후에 해당 위치에 벽이 있는지 알 수 있기 때문.
# t초 후에 (x,y)에 벽이 있다면, 그 벽은 현재 시점에는 (x-t,y)에 있던 벽이다.
# (t+1)초 후에 (x,y)에 벽이 내려온다면,그 벽은 현재 시점에는 (x-(t+1),y)에 있던 벽이다.
# 위와 같이 t초 후에 이동할 곳에 벽이 있거나, 이동한 직후, 즉 (t+1)초 후에 벽이 내려올 곳을 제외하면, 빈 칸만 탐색하는 것이 된다.
from collections import deque
dx = [0,0,1,-1,1,-1,1,-1,0]
dy = [1,-1,0,0,1,1,-1,-1,0]
n = 8
a = [input() for _ in range(n)]
q = deque()
check = [[[False]*(n+1) for j in range(n)] for i in range(n)] # 0~8초 시점까지의 (x,y) 위치
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