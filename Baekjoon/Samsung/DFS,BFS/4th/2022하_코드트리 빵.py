import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
a=[[[] for _ in range(n)] for _ in range(n)]
b=[list(map(int,input().split())) for _ in range(n)] #  베이스 캠프 맵.(0=빈 공간, 1=베이스캠프, -1=막힌 칸)
arrive=[False]*(m+1) # 사람 편의점 도착 여부
goal=[None]*(m+1) # 사람별 목표 편의점 위치
for no in range(1,m+1):
    x,y=map(int,input().split())
    x-=1
    y-=1
    goal[no]=(x,y)

#   상,좌,우,하
dx=[-1,0,0,1]
dy=[0,-1,1,0]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def bfs1(no,sx,sy):
    ex,ey=goal[no] # 목표 편의점 위치
    q=deque()
    q.append((sx,sy))
    visit=[[False]*n for _ in range(n)]
    visit[sx][sy]=True
    parent=dict() # (다음칸)=(현재칸)

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and not visit[nx][ny] and b[nx][ny]!=-1:
                visit[nx][ny]=True
                q.append((nx,ny))
                parent[(nx,ny)]=(x,y)

    end=(ex,ey)
    start=(sx,sy) # 사람의 현재 위치
    current=end
    route=[current] # 최단 루트
    while current!=start:
        current=parent[current]
        route.append(current)
    route.reverse() #

    return route[1]

# 만약 편의점에 도착한다면 해당 편의점에서 멈추게 되고,
# 이때부터 다른 사람들은 해당 편의점이 있는 칸을 지나갈 수 없게 됩니다.
# 격자에 있는 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없어짐에 유의합니다.
def finish(arrived):
    global b,arrive

    for x,y,no in arrived: # 편의점 도착한 사람들은 해당 칸 지나갈 수 없고, ㄷ착 정보 True로 변경
        b[x][y] = -1
        arrive[no] = True

# 격자에 있는 사람들 모두가 본인이 가고 싶은 편의점 방향을 향해서 1 칸 움직입니다.
# 최단거리로 움직이며 최단 거리로 움직이는 방법이 여러가지라면 ↑, ←, →, ↓ 의 우선 순위로 움직이게 됩니다.
# 여기서 최단거리라 함은 상하좌우 인접한 칸 중 이동가능한 칸으로만 이동하여 도달하기까지 거쳐야 하는 칸의 수가 최소가 되는 거리를 뜻합니다.
def move():
    global a

    arrived=[] # 도착한 사람들 정보 리스트
    tmp=[[[] for _ in range(n)] for _ in range(n)] # 사람 동시 이동할 맵
    for x in range(n):
        for y in range(n):
            if len(a[x][y])>0: # 해당 칸에 사람이 있다면
                for no in a[x][y]: # 사람별로
                    nx,ny=bfs1(no,x,y) # 다음 칸
                    if (nx,ny)==goal[no]: # 목표한 편의점 도착
                        arrived.append([nx,ny,no]) # 도착한 사람들 정보 리스트에 정보 삽입
                        # b[nx][ny]=-1
                        # arrive[no]=True
                    else:
                        tmp[nx][ny].append(no) # 동시 이동할 맵에 표시
    finish(arrived)
    a=tmp

def check():
    for i in range(1,m+1):
        if arrive[i] is False:
            return False
    return True

# 여기서 가장 가까이에 있다는 뜻 역시 1에서와 같이 최단거리에 해당하는 곳을 의미합니다.
# 가장 가까운 베이스캠프가 여러 가지인 경우에는 그 중 행이 작은 베이스캠프, 행이 같다면 열이 작은 베이스 캠프로 들어갑니다.
def bfs2(sx,sy):

    q=deque()
    q.append((sx,sy))
    d=[[-1]*n for _ in range(n)]
    d[sx][sy]=0
    cand=[] # 베이스 캠프 후보 정보 리스트

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and d[nx][ny]==-1 and b[nx][ny]!=-1:
                q.append((nx,ny))
                d[nx][ny]=d[x][y]+1
                if b[nx][ny]==1: # 베이스 캠프 발견했으면
                    cand.append([d[nx][ny],nx,ny]) # 후보 리스트에 정보 삽입

    cand.sort() # 거리,행,열 오름차순 정렬
    return [cand[0][1],cand[0][2]] # 행,열만 반환

# 현재 시간이 t분이고 t ≤ m를 만족한다면,
# t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프에 들어갑니다.
# t번 사람이 베이스 캠프로 이동하는 데에는 시간이 전혀 소요되지 않습니다.
def enter(time):
    global a,b

    if time<=m:
        sx,sy=goal[time] # 시작지점 : 해당 사람의 목표 편의점
        ex,ey=bfs2(sx,sy) # 도착지점 : 목표 편의점에서 가장 가까이 위치한 베이스캠프
        b[ex][ey]=-1 # 해당 베이스 캠프 막힘
        a[ex][ey].append(time) # 사람 맵에 추가

time=0
while True:
    time+=1
    # 편의점 향해 이동
    move()
    # 편의점 모두 도착 여부
    if check():
        break
    # 베이스캠프 입장
    enter(time)

print(time)