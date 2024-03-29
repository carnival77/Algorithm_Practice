import sys
from collections import deque

input=sys.stdin.readline

class Person:
    def __init__(self,sx,sy,ex,ey):
        self.sx=sx
        self.sy=sy
        self.ex=ex
        self.ey=ey

n,m,ans=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] # 0 : 빈칸, -1 : 벽, 1 이상 : 승객
for x in range(n):
    for y in range(n):
        if a[x][y]==1:
            a[x][y]=-1
cx,cy=map(int,input().split())
cx-=1
cy-=1
# ps,pe=[],[]
people=[None]
done=[None]+[False]*m
no=0
for pno in range(1,m+1):
    sx,sy,ex,ey=map(int,input().split())
    people.append(Person(sx-1,sy-1,ex-1,ey-1))
    a[sx-1][sy-1]=pno
    # ps.append((sx-1,sy-1))
    # pe.append((ex-1,ey-1))

# 그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객을, 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다
#  상,좌,하,우
dx=[-1,0,1,0]
dy=[0,-1,0,1]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def bfs(sx,sy):

    q=deque()
    q.append((sx,sy))
    d=[[-1]*n for _ in range(n)]
    d[sx][sy]=0
    cand=[]

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and d[nx][ny]==-1 and a[nx][ny]!=-1:
                q.append((nx,ny))
                d[nx][ny]=d[x][y]+1
                if a[nx][ny]>=1:
                    cand.append([d[nx][ny],nx,ny])
                # for pno in range(m):
                #     if done[pno]: continue
                #     if ps[pno]==(nx,ny):
                #         cand.append([d[nx][ny],nx,ny,pno])

    return cand

def bfs2(sx,sy,ex,ey):

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

    return d[ex][ey]

# 이동하는 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝난다.
def move(kind):
    global cx,cy,ans,no,done

    # 백준이 태울 승객을 고를 때는 현재 위치에서 최단거리가 가장 짧은 승객을 고른다.
    # 그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객을, 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다.
    # 택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0이다.
    # 연료는 한 칸 이동할 때마다 1만큼 소모된다
    if kind==1:
        # for pno in range(m):
        #     if done[pno]: continue
        #     if ps[pno] == (cx, cy):
        #         no=pno
        #         return True
        if a[cx][cy]>=1:
            no=a[cx][cy]
            return True
        cand=bfs(cx,cy)
        if len(cand)==0: return False
        cand.sort()
        d,sx,sy=cand[0]
        ans-=d
        if ans<=0:
            return False
        else:
            cx,cy=sx,sy
            no=a[sx][sy]
            return True
    # 한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전된다.
    # 승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.
    else:
        ex,ey=people[no].ex,people[no].ey
        d=bfs2(cx,cy,ex,ey)
        if d==-1:
            return False
        else:
            ans-=d
            if ans < 0:
                return False
            else:
                ans+=2*d
                done[no]=True
                a[cx][cy]=0
                cx,cy=ex,ey
                return True

ok=True
for round in range(m):

    # 승객에게 이동
    ok=move(1)

    if not ok:
        break

    # 승객 목적지까지 태워주기
    ok=move(2)

    if not ok:
        break

if not ok:
    ans=-1
print(ans)