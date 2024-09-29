import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] # 검은색 블록은 -1, 무지개 블록은 0, 빈 칸은 -2, 일반 블록은 M가지 색상이 있고, 색은 M이하의 자연수
ans=0
visited=[]

#  상,좌,하,우
dx=[-1,0,1,0]
dy=[0,-1,0,1]

def rotateCounterClockwise(a):
    return list(map(list,zip(*a)))[::-1]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

# 블록 그룹은 연결된 블록의 집합이다.
# 그룹에는 일반 블록이 적어도 하나 있어야 하며, 일반 블록의 색은 모두 같아야 한다.
# 검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다.
# 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며,
# 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다.
# 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.
def bfs(sx,sy,num):
    global visited

    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=True

    all=[[sx,sy]]
    cand=[] # 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.
    rainbow=0
    normal=0
    if a[sx][sy]==0:
        rainbow=1
    else:
        normal=1
        cand.append([sx,sy])

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if not inBoard(nx,ny) or visited[nx][ny]:continue
            # 일반 블록의 색은 모두 같아야 한다. 검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다.
            if a[nx][ny]==0 or a[nx][ny]==num:
                q.append((nx,ny))
                visited[nx][ny]=True
                all.append([nx,ny])
                if a[nx][ny]==0:
                    rainbow+=1
                else:
                    cand.append([nx, ny])
                    normal+=1

    total=normal+rainbow
    # 그룹에는 일반 블록이 적어도 하나 있어야 하며
    # 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며,
    if total>=2 and normal>=1:
        if len(cand) > 0:
            cand.sort()
            ex, ey = cand[0]
        return [total, rainbow, ex, ey, all]
    else:
        return None

# 크기가 가장 큰 블록 그룹을 찾는다.
# 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹,
# 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을,
# 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
def search():
    global visited

    blockGroups = []
    # 컬러별 탐색
    for color in range(1, m + 1):
        # 컬러별 방문 블록 맵을 설정한다. 이를 통해, 위치가 다르고 컬러가 같은 블록이 격자 내 무지개 블록을 활용하여 각각 그룹을 형성할 수 있도록 한다.
        visited = [[False] * n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if a[x][y]==color and not visited[x][y]:
                    res=bfs(x,y,a[x][y])
                    if res!=None:
                        blockGroups.append(res)

    if len(blockGroups)>0:
        blockGroups.sort(key=lambda x:(-x[0],-x[1],-x[2],-x[3]))
        return blockGroups[0][-1]
    else:
        return None

def remove(all):
    global a,ans

    for x,y in all:
        if a[x][y]!=-1:
            a[x][y]=-2

    ans+=len(all)**2

# 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동한다.
# 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속 된다.
def move():
    global a

    ok=True
    while ok:
        ok=False
        for x in range(n-1):
            for y in range(n):
                if 0<=a[x][y]<=m and a[x+1][y]==-2:
                    a[x][y],a[x+1][y]=a[x+1][y],a[x][y]
                    ok=True

while True:
    # 블록 그룹 찾기
    blockGroup = search()
    # 블록 그룹이 존재하는 동안 계속해서 반복
    if blockGroup==None:
        break
    # 블록 그룹 제거
    remove(blockGroup)
    # 중력 작용
    move()
    # 반시계 방향 90도 회전
    a=rotateCounterClockwise(a)
    # 중력 작용
    move()

print(ans)