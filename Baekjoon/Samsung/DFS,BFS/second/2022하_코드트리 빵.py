import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] # 0 : 빈 칸, 1 : 베이스캠프, -1 : 지나갈 수 없는 공간(베이스캠프 및 편의점)
g=[] # 사람별 목표 편의점 위치
for i in range(m):
    x,y=map(int,input().split())
    x-=1
    y-=1
    g.append([x,y])
p=[[-1,-1]]*m # 사람별 위치

#  상,좌,우,하
dx=[-1,0,0,1]
dy=[0,-1,1,0]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

# 최단거리로 움직이며 최단 거리로 움직이는 방법이 여러가지라면 ↑, ←, →, ↓ 의 우선 순위로 움직이게 됩니다.
# 여기서 최단거리라 함은 상하좌우 인접한 칸 중 이동가능한 칸으로만 이동하여
# 도달하기까지 거쳐야 하는 칸의 수가 최소가 되는 거리를 뜻합니다.
def getNext(start,end):

    sx, sy=start
    q=deque()
    q.append((sx,sy))
    visited=[[False]*n for _ in range(n)]
    visited[sx][sy]=True
    parent=dict()

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and not visited[nx][ny] and a[nx][ny]!=-1:
                q.append((nx,ny))
                visited[nx][ny]=True
                parent[(nx,ny)]=(x,y)

    # 최단 경로
    trace=[]
    current=tuple(end)
    start=tuple(start)
    while current!=start:
        trace.append(current)
        current=parent[current]
    trace.append(start)
    trace.reverse()

    return trace[1]

# 격자에 있는 사람들 모두가 본인이 가고 싶은 편의점 방향을 향해서 1 칸 움직입니다.
# 만약 편의점에 도착한다면 해당 편의점에서 멈추게 되고,
# 이때부터 다른 사람들은 해당 편의점이 있는 칸을 지나갈 수 없게 됩니다.
# 격자에 있는 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없어짐에 유의합니다.
def move():
    global p,a

    block=[]
    for no,person_pos in enumerate(p):
        goal = g[no]
        # 격자 내에 없거나 이미 목표 편의점에 도달한 사람은 제외
        if person_pos==[-1,-1] or person_pos==goal:
            continue
        nx,ny=getNext(person_pos,goal)
        p[no]=[nx,ny]
        if goal==p[no]:
            block.append([nx,ny])

    for x,y in block:
        a[x][y]=-1

# 여기서 가장 가까이에 있다는 뜻 역시 1에서와 같이 최단거리에 해당하는 곳을 의미합니다.
# 가장 가까운 베이스캠프가 여러 가지인 경우에는
# 그 중 행이 작은 베이스캠프, 행이 같다면 열이 작은 베이스 캠프로 들어갑니다.
# t번 사람이 베이스 캠프로 이동하는 데에는 시간이 전혀 소요되지 않습니다.
def bfs(start): # start = 가고 싶은 편의점 위치

    sx,sy=start
    q=deque()
    q.append((sx,sy))
    d=[[-1]*n for _ in range(n)]
    d[sx][sy]=0
    cand=[] # 베이스캠프 후보

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and d[nx][ny]==-1 and a[nx][ny]!=-1:
                q.append((nx,ny))
                d[nx][ny]=d[x][y]+1
                if a[nx][ny]==1:
                    cand.append([d[nx][ny],nx,ny])

    cand.sort()
    return cand[0][1:]

# 이때부터 다른 사람들은 해당 베이스 캠프가 있는 칸을 지나갈 수 없게 됩니다.
# t번 사람이 편의점을 향해 움직이기 시작했더라도
# 해당 베이스 캠프는 앞으로 절대 지나갈 수 없음에 유의합니다.
# 마찬가지로 격자에 있는 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없어짐에 유의합니다.
def enter(time):
    global p,a

    p[time]=bfs(g[time])
    x,y=p[time]
    a[x][y]=-1

def check():
    for no,person_pos in enumerate(p):
        if person_pos!=g[no]:
            return False
    return True

time=0
while True:
    time += 1
    # 1,2
    move()
    # 3
    # 현재 시간이 t분이고 t ≤ m를 만족한다면,
    # t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프에 들어갑니다.
    if time<=m:
        enter(time-1)
    # 사람들이 모두 목표 편의점에 도착하였는지
    if check():
        break

print(time)