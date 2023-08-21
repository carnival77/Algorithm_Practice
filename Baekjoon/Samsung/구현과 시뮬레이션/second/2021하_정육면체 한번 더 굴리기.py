import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
ans=0

#  우,하,좌,상
dx=[0,1,0,-1]
dy=[1,0,-1,0]
sx,sy,d=0,0,0 # 주사위는 항상 초기에 격자판의 1행 1열에 놓여져 있고, 처음에는 항상 오른쪽으로 움직입니다.

dice=[0,1,5,3,4,2,6]

# 주사위 굴리기
def roll(a,d):
    b=[0]*7
    # 우
    if d == 0:
        b[4] = a[6]
        b[3] = a[1]
        b[1] = a[4]
        b[6] = a[3]
        b[5] = a[5]
        b[2] = a[2]
    # 하
    elif d == 1:
        b[2] = a[6]
        b[1] = a[2]
        b[5] = a[1]
        b[6] = a[5]
        b[3] = a[3]
        b[4] = a[4]
    # 좌
    elif d == 2:
        b[6] = a[4]
        b[1] = a[3]
        b[4] = a[1]
        b[3] = a[6]
        b[5] = a[5]
        b[2] = a[2]
    # 상
    else:
        b[6] = a[2]
        b[2] = a[1]
        b[1] = a[5]
        b[5] = a[6]
        b[3] = a[3]
        b[4] = a[4]

    return b

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

# 주사위의 아랫면이 보드의 해당 칸에 있는 숫자보다 크면
# 현재 진행방향에서 90' 시계방향으로 회전하여 다시 이동을 진행하게 되고,
# 주사위의 아랫면의 숫자가 더 작다면 현재 진행방향에서 90' 반시계방향으로 회전하게 되며,
# 동일하다면 현재 방향으로 계속 진행하게 됩니다.
# 하지만 만약 진행 도중 다음과 같이 격자판을 벗어나게 된다면,
# 반사되어 방향이 반대로 바뀌게 된 뒤 한 칸 움직이게 됩니다.
def move(turn):
    global sx,sy,d,dice

    if turn==1:
        pass
    else:
        x = dice[6]
        y = a[sx][sy]

        if x > y:
            d = (d + 1) % 4
        elif x < y:
            d = (d - 1) % 4

    nx, ny = sx + dx[d], sy + dy[d]
    if not inBoard(nx,ny):
        d=(d+2)%4
        nx, ny = sx + dx[d], sy + dy[d]
    dice=roll(dice,d)
    sx,sy=nx,ny

# 격자판 위 주사위가 놓여있는 칸에 적혀있는 숫자와 상하좌우로 인접하며
# 같은 숫자가 적혀있는 모든 칸의 합만큼 점수를 얻게 됩니다.
def bfs():
    global ans

    num=a[sx][sy]
    q=deque()
    q.append((sx,sy))
    visited=[[False]*n for _ in range(n)]
    visited[sx][sy]=True
    cnt=1

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and not visited[nx][ny] and a[nx][ny]==num:
                q.append((nx,ny))
                visited[nx][ny]=True
                cnt+=1

    ans+=cnt*num

for turn in range(1,m+1):
    # 주사위 이동
    move(turn)
    # BFS
    bfs()

print(ans)