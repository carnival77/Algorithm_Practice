import sys
from collections import deque

input=sys.stdin.readline

class Player: # 플레이어 클래스
    def __init__(self,no,ex,ey,x=-1,y=-1): # 초기에는 격자 밖으로 위치 설정(x=-1,y=-1)
        self.no=no
        self.x=x
        self.y=y
        self.ex=ex
        self.ey=ey

n,m=map(int,input().split())
pvisit=[True]+[False]*m # 플레이어 도착 상태 배열
t=1 # 현재 시간
players=[None] # 플레이어 클래스 객체 배열
a=[list(map(int,input().split())) for _ in range(n)] # 맵. 편의점 + 베이스캠프. (0:빈 공간, 1:베이스캠프, 2:편의점, 3:출입금지)

for no in range(1,m+1):
    ex,ey=map(int,input().split())
    ex-=1
    ey-=1
    p=Player(no,ex,ey)
    players.append(p)
    a[ex][ey]=2

#  상,좌,우,하
dx=[-1,0,0,1]
dy=[0,-1,1,0]

# 용도 : 플레이어 현 위치 -> 편의점. 최단 경로
# input : 플레이어 현 위치, 향하는 편의점 위치
# output : 다음 좌표
def bfs1(x,y,ex,ey):
    global a
    # 경로 딕셔너리
    parent=dict()
    q=deque()
    start = [x, y]
    q.append(start)
    d=[[-1]*n for _ in range(n)]
    d[x][y]=0

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            # 격자 내, 출입 금지 아니며, 미탐색 지역이면 탐색
            if 0<=nx<n and 0<=ny<n and a[nx][ny]!=3 and d[nx][ny]==-1:
                d[nx][ny]=d[x][y]+1
                q.append([nx,ny])
                # 다음 위치 key 가 현재 위치를 value로 갖도록 경로 딕셔너리에 정보 추가
                parent[(nx,ny)]=(x,y)
    # 최단 경로
    trace = []
    current = (ex,ey)
    start=tuple(start)
    while current != start:
        trace.append(current)
        current = parent[current]
    trace.append(start)
    # 시작점부터 목적지까지
    trace.reverse()
    # 시작점 바로 다음 위치가 다음 갈 곳
    ans=trace[1]
    return ans

# 용도 : 편의점 -> 베이스캠프. 최단 경로
# input : 편의점 위치
# output : 베이스캠프 위치
def bfs2(x,y):
    global a
    ans = []
    q = deque()
    q.append([x, y])
    d = [[-1] * n for _ in range(n)]
    d[x][y] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and a[nx][ny] != 3 and d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                q.append([nx, ny])
                if a[nx][ny]==1:
                    ans.append([d[nx][ny],nx,ny])
    ans.sort()
    return ans[0][1:]

while True:
    # 각 플레이어들의 숫자를 순차 탐색하며
    for no in range(1,len(pvisit)):
        # 해당 숫자의 플레이어가 이미 도착 상태라면 다음 플레이어로
        if pvisit[no]:
            continue
        # 이번 플레이어 선정
        p=players[no]
        # 이번 플레이어가 아직 격자 밖이라면 다음 플레이어로
        if (p.x,p.y)==(-1,-1):
            continue
        # 플레이어가 갈 위치 선정
        nx,ny=bfs1(p.x,p.y,p.ex,p.ey)
        # 플레이어 위치 업데이트
        p.x,p.y=nx,ny
        # 만약 플레이어가 향하던 편의점에 도착했다면
        if (p.x,p.y)==(p.ex,p.ey):
            # 맵에서 해당 위치는 출입금지로
            a[p.x][p.y]=3
            # 해당 플레이어는 도착 완료로 업데이트
            pvisit[p.no]=True
    # 현재 시간이 t분이고 t ≤ m를 만족한다면
    if t<=m:
        p=players[t]
        # 플레이어가 갈 베이스캠프 위치 선정
        bx,by=bfs2(p.ex,p.ey)
        # 해당 위치는 출입 금지로
        a[bx][by]=3
        # 플레이어는 베이스캠프로 위치
        p.x,p.y=bx,by
    # 플레이어들이 모두 도착 상태라면 중지
    if False not in pvisit:
        break
    t+=1

print(t)