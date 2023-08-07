import sys
from collections import deque
input=sys.stdin.readline

class Person:
    def __init__(self,no,x,y,ex,ey):
        self.no=no
        self.x=x
        self.y=y
        self.ex=ex
        self.ey=ey

n,m,e=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] # 0은 빈칸, -1은 벽, 1 이상은 택시를 기다리는 승객
for x in range(n):
    for y in range(n):
        if a[x][y]==1:
            a[x][y]=-1
cx,cy=map(int,input().split())
cx-=1
cy-=1
people=[None]
done=[None]+[False]*m
for no in range(1,m+1):
    x,y,ex,ey=map(int,input().split())
    people.append(Person(no,x-1,y-1,ex-1,ey-1))
    a[x-1][y-1]=no
ans=0
# 행 번호가 가장 작은 승객을, 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다
#  상,좌,우,하
dx=[-1,0,0,1]
dy=[0,-1,1,0]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def check():
    if False not in done:
        return True
    return False

# 현재 위치에서 최단거리가 가장 짧은 승객을 고른다.
# 그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객을,
# 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다.
# 택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0이다
def choose():

    sx,sy=cx,cy
    q=deque()
    q.append((sx,sy))
    d=[[-1]*n for _ in range(n)]
    d[sx][sy]=0
    cand=[]
    # 택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0이다
    if a[sx][sy]>=1:
        return [people[a[sx][sy]],0]

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and d[nx][ny]==-1 and a[nx][ny]!=-1:
                q.append((nx,ny))
                d[nx][ny]=d[x][y]+1
                if a[nx][ny]>=1:
                    cand.append([d[nx][ny],nx,ny])

    if len(cand)>0:
        cand.sort()
        dist,x,y=cand[0]
        return [people[a[x][y]],dist]
    return None

# 승객 위치에서 목적지까지의 최단거리
def bfs(sx,sy,ex,ey):

    q=deque()
    q.append((sx,sy))
    d=[[-1]*n for _ in range(n)]
    d[sx][sy]=0

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and d[nx][ny]==-1 and a[nx][ny]!=-1:
                q.append((nx,ny))
                d[nx][ny]=d[x][y]+1

    dist=d[ex][ey]
    if dist==-1:
        return None
    else:
        return d[ex][ey]

# 한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전된다.
# 이동하는 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝난다.
# 승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.
def deliver(person):
    global e,cx,cy,people,a

    p,d=person
    x,y,ex,ey=p.x,p.y,p.ex,p.ey
    # 승객 위치에서 목적지까지의 최단거리
    d2=bfs(x,y,ex,ey)
    if d2==None:
        return False
    else:
        if e-(d+d2)>=0:
            e=e-d+d2
            done[p.no]=True
            cx,cy=ex,ey
            a[x][y]=0
            return True
        else:
            return False

while True:
    # 모든 승객 운송 완료
    if check():
        ans=e
        break
    # 다음 승객 선정
    person=choose()
    # 모든 손님을 이동시킬 수 없는 경우에도 -1을 출력
    if person==None:
        ans = -1
        break
    # 승객 운송
    if not deliver(person):
        ans = -1
        break

print(ans)