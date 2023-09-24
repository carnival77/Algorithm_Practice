import sys
from collections import deque

input=sys.stdin.readline

#  상,좌,하,우
dx=[-1,0,1,0]
dy=[0,-1,0,1]

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] # 검은색 블록은 -1, 무지개 블록은 6, 일반 블록은 1~m(최대 5), 빈 칸은 0
for x in range(n):
    for y in range(n):
        if a[x][y]==0:
            a[x][y]=6
b=[row[:] for row in a] # 디버깅용. 블록 그룹 번호 맵
visit=[]
ans=0

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

# 블록 그룹은 연결된 블록의 집합이다. 그룹에는 일반 블록이 적어도 하나 있어야 하며, 일반 블록의 색은 모두 같아야 한다.
# 검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다.
# 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며, 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다.
# 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.
def bfs(sx,sy,color,no):
    global visit,b

    q=deque()
    q.append((sx,sy))
    cnt=1
    rainbow=0
    visited=[[sx,sy]]
    visit[sx][sy]=True
    rainbow_visited=[]
    cand=[[sx,sy]] # 기준 블록 후보. 일반 블록

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and not visit[nx][ny] and (a[nx][ny]==color or a[nx][ny]==6):
                q.append((nx,ny))
                visited.append([nx,ny])
                visit[nx][ny]=True
                if a[nx][ny]==6:
                    rainbow+=1
                    rainbow_visited.append([nx,ny])
                elif a[nx][ny]==color:
                    cnt+=1
                    cand.append([nx,ny])

    total=cnt+rainbow
    if cnt>=1 and total>=2:
        for x,y in visited:
            visit[x][y]=True
            b[x][y]=no
        for x,y in rainbow_visited:
            visit[x][y]=False
            b[x][y]=6
        cand.sort()
        tx,ty=cand[0]
        return [total,rainbow,tx,ty,visited]
    else:
        for x, y in visited:
            visit[x][y] = False
        return None

# 크기가 가장 큰 블록 그룹을 찾는다.
# 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
def check():
    global visit

    blocks=[]
    visit=[[False]*n for _ in range(n)]
    no=1
    for color in range(1,m+1):
        for x in range(n):
            for y in range(n):
                if visit[x][y]:continue
                if a[x][y]==color:
                    block=bfs(x,y,color,no)
                    if block is not None:
                        blocks.append(block)
                        no+=1

    if len(blocks)>0:
        blocks.sort(key=lambda x:(-x[0],-x[1],-x[2],-x[3]))
        return blocks[0]
    else:
        return None

def remove(block):
    global ans,a

    cnt=block[0]
    visited=block[-1]

    for x,y in visited:
        a[x][y]=0

    ans+=cnt**2

def gravity():
    global a

    ok=True
    while ok:
        ok=False
        for x in range(n-1):
            for y in range(n):
                if a[x+1][y]==0 and a[x][y]>=1:
                    a[x+1][y],a[x][y]=a[x][y],a[x+1][y]
                    ok=True

def rotateCounterClockwise(a):
    return list(map(list,zip(*a)))[::-1]

round=1
while True:
    # 블록 그룹 찾기
    block=check()
    if block is None:
        break
    # 블록 그룹 제거 및 점수 획득
    remove(block)
    # 중력 작용
    gravity()
    # 반시계 방향 90도 회전
    a=rotateCounterClockwise(a)
    # 중력 작용
    gravity()

    round+=1

print(ans)