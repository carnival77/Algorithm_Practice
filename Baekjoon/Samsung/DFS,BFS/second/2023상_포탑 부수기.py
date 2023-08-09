import sys
from collections import deque
input=sys.stdin.readline

n,m,turn=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] # 공격력
b = [[0] * m for _ in range(n)] # 최근 공격 시점
ans=0

# 우/하/좌/상의 우선순위대로 먼저 움직인 경로가 선택됩니다.
#  우,하,좌,상
dx=[0,1,0,-1]
dy=[1,0,-1,0]

# 중앙과 대각선 4개 방향
dx1=[0,-1,1,-1,1]
dy1=[0,-1,1,1,-1]

# 만약 부서지지 않은 포탑이 1개가 된다면 그 즉시 중지됩니다.
def check():
    cnt=0
    for x in range(n):
        for y in range(m):
            if a[x][y]>0:
                cnt+=1
    if cnt==1:
        return True
    return False

# 부서지지 않은 포탑 중 가장 약한 포탑이 공격자로 선정됩니다.
# 공격자로 선정되면 가장 약한 포탑이므로, 핸디캡이 적용되어 N+M만큼의 공격력이 증가됩니다.
# 가장 약한 포탑은 다음의 기준으로 선정됩니다.
# 공격력이 가장 낮은 포탑이 가장 약한 포탑입니다.
# 만약 공격력이 가장 낮은 포탑이 2개 이상이라면, 가장 최근에 공격한 포탑이 가장 약한 포탑입니다. (모든 포탑은 시점 0에 모두 공격한 경험이 있다고 가정하겠습니다.)
# 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 행과 열의 합이 가장 큰 포탑이 가장 약한 포탑입니다.
# 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 큰 포탑이 가장 약한 포탑입니다.
# 선정된 공격자는 자신을 제외한 가장 강한 포탑을 공격합니다.
# 가장 강한 포탑은 위에서 정한 가장 약한 포탑 선정 기준의 반대이며, 다음과 같습니다.
# 공격력이 가장 높은 포탑이 가장 강한 포탑입니다.
# 만약 공격력이 가장 높은 포탑이 2개 이상이라면, 공격한지 가장 오래된 포탑이 가장 강한 포탑입니다. (모든 포탑은 시점 0에 모두 공격한 경험이 있다고 가정하겠습니다.)
# 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 행과 열의 합이 가장 작은 포탑이 가장 강한 포탑입니다.
# 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 작은 포탑이 가장 강한 포탑입니다.
def select(t):
    global sx,sy,ex,ey,a,b,c

    cand=[]
    for x in range(n):
        for y in range(m):
            if a[x][y]==0:continue
            cand.append([a[x][y],b[x][y],(x+y),y])

    cand.sort(key=lambda x:(x[0],-x[1],-x[2],-x[3]))
    sy=cand[0][-1]
    sx=cand[0][-2]-sy
    a[sx][sy]+=(n+m)
    b[sx][sy]=t
    ey=cand[-1][-1]
    ex=cand[-1][-2]-ey
    c[sx][sy]=c[ex][ey]=True

# def inBoard(nx,ny):
#     if 0<=nx<n and 0<=ny<m:
#         return True
#     return False

def beyondBoundary(nx,ny):
    if nx < 0:
        nx = n - 1
    if nx >= n:
        nx = 0
    if ny < 0:
        ny = m - 1
    if ny >= m:
        ny = 0
    return nx,ny

# 레이저는 다음의 규칙으로 움직입니다.
# 상하좌우의 4개의 방향으로 움직일 수 있습니다.
# 부서진 포탑이 있는 위치는 지날 수 없습니다.
# 가장자리에서 막힌 방향으로 진행하고자 한다면, 반대편으로 나옵니다.
# (예를 들어, 위의 예시에서 (2,3)에서 오른쪽으로 두번 이동한다면, (2,3) -> (2,4) -> (2,1) 순으로 이동합니다.)
# 레이저 공격은 공격자의 위치에서 공격 대상 포탑까지의 최단 경로로 공격합니다.
# 만약 그러한 경로가 존재하지 않는다면 (2) 포탄 공격을 진행합니다.
# 만약 경로의 길이가 똑같은 최단 경로가 2개 이상이라면, 우/하/좌/상의 우선순위대로 먼저 움직인 경로가 선택됩니다.
def bfs():

    q=deque()
    q.append((sx,sy))
    visited=[[False]*m for _ in range(n)]
    visited[sx][sy]=True
    parent=dict()

    while q:
        x,y=q.popleft()
        # 상하좌우의 4개의 방향으로 움직일 수 있습니다.
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            # 가장자리에서 막힌 방향으로 진행하고자 한다면, 반대편으로 나옵니다.
            nx,ny=beyondBoundary(nx,ny)
            # 부서진 포탑이 있는 위치는 지날 수 없습니다.
            if a[nx][ny]==0:
                continue
            if visited[nx][ny]:
                continue
            q.append((nx,ny))
            visited[nx][ny]=True
            parent[(nx,ny)]=(x,y)

    if visited[ex][ey]:
        start = (sx, sy)
        end = (ex, ey)
        current = end
        trace = []
        while current != start:
            trace.append(current)
            current = parent[current]
        # trace.append(start)
        trace.reverse()
        return trace
    else:
        return None

# 최단 경로가 정해졌으면, 공격 대상에는 공격자의 공격력 만큼의 피해를 입히며,
# 피해를 입은 포탑은 해당 수치만큼 공격력이 줄어듭니다.
# 또한 공격 대상을 제외한 레이저 경로에 있는 포탑도 공격을 받게 되는데,
# 이 포탑은 공격자 공격력의 절반 만큼의 공격을 받습니다.
# (절반이라 함은 공격력을 2로 나눈 몫을 의미합니다.)
def laser(trace):
    global a,c

    for x,y in trace:
        if a[x][y]==0:continue
        if (x,y)==(ex,ey):
            a[x][y]-=a[sx][sy]
        else:
            a[x][y]-=a[sx][sy]//2
        # 공격을 받아 공격력이 0 이하가 된 포탑은 부서집니다.
        if a[x][y]<0:
            a[x][y]=0
        c[x][y]=True

# 공격 대상에 포탄을 던집니다.
# 공격 대상은 공격자 공격력 만큼의 피해를 받습니다.
# 추가적으로 주위 8개의 방향에 있는 포탑도 피해를 입는데, 공격자 공격력의 절반 만큼의 피해를 받습니다.
# (절반이라 함은 공격력을 2로 나눈 몫을 의미합니다.)
# 공격자는 해당 공격에 영향을 받지 않습니다.
# 만약 가장자리에 포탄이 떨어졌다면, 위에서의 레이저 이동처럼 포탄의 추가 피해가 반대편 격자에 미치게 됩니다.
def canon():
    global a,c

    x,y=ex,ey
    dx2=dx+dx1
    dy2=dy+dy1
    for k in range(9):
        nx,ny=x+dx2[k],y+dy2[k]
        # 가장자리에서 막힌 방향으로 진행하고자 한다면, 반대편으로 나옵니다.
        nx, ny = beyondBoundary(nx, ny)
        if a[nx][ny]==0 or (nx,ny)==(sx,sy): continue
        if (nx, ny) == (ex, ey):
            a[nx][ny] -= a[sx][sy]
        else:
            a[nx][ny] -= a[sx][sy] // 2
        # 공격을 받아 공격력이 0 이하가 된 포탑은 부서집니다.
        if a[nx][ny]<0:
            a[nx][ny]=0
        c[nx][ny]=True

def attack():

    trace=bfs()
    if trace is not None:
        laser(trace)
    else:
        canon()

# 부서지지 않은 포탑 중 공격과 무관했던 포탑은 공격력이 1씩 올라갑니다.
# 공격과 무관하다는 뜻은 공격자도 아니고, 공격에 피해를 입은 포탑도 아니라는 뜻입니다.
def fix():
    for x in range(n):
        for y in range(m):
            if c[x][y] or a[x][y]==0:
                continue
            a[x][y]+=1

for t in range(1,turn+1):
    c = [[False] * m for _ in range(n)]  # 공격 관여
    sx, sy = 0, 0  # 공격자
    ex, ey = 0, 0  # 공격 대상

    if check():
        break
    # 공격자, 공격 대상 선정
    select(t)
    # 공격
    attack()
    # 정비
    fix()

for x in range(n):
    for y in range(m):
        ans=max(ans,a[x][y])
print(ans)