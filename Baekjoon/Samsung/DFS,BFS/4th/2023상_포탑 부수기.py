from collections import deque

n,m,K=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] # 공격력
b=[[0]*m for _ in range(n)] # 공격시점
c=[[False]*m for _ in range(n)] # 공격관여

ax,ay=-1,-1
tx,ty=-1,-1

#  우,하,좌,상
dx=[0,1,0,-1]
dy=[1,0,-1,0]

# 대각선
dx1=[-1,-1,-1,0,0,1,1,1]
dy1=[-1,0,1,-1,1,-1,0,1]

def selectAttacker(round):
    global ax,ay,a,b,c

    # 공격자 선정
    arr=[]
    for x in range(n):
        for y in range(m):
            if a[x][y]==0:continue
            arr.append([a[x][y],b[x][y],x+y,y,x])
    arr.sort(key=lambda x:(x[0],-x[1],-x[2],-x[3]))
    ax,ay=arr[0][-1],arr[0][-2]

    # 공격력 증가
    a[ax][ay]+=n+m
    # 공격관여와 공격시점 업데이트
    c[ax][ay]=True
    b[ax][ay]=round

def selectAttacked(round):
    global tx,ty,a,b,c

    # 공격대상 선정
    arr=[]
    for x in range(n):
        for y in range(m):
            if a[x][y]==0:continue
            if (x,y)==(ax,ay): continue
            arr.append([a[x][y],b[x][y],x+y,y,x])
    arr.sort(key=lambda x:(-x[0],x[1],x[2],x[3]))
    tx,ty=arr[0][-1],arr[0][-2]

    # 공격관여 업데이트
    c[tx][ty] = True


def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<m:
        return True
    return False

def outBoard(nx,ny):
    if nx==-1:
        nx=n-1
    if nx==n:
        nx=0
    if ny==-1:
        ny=m-1
    if ny==m:
        ny=0
    return [nx,ny]

def bfs():

    # 공격자 - 공격대상까지의 최단 루트 탐색
    q=deque()
    q.append((ax,ay))
    visit=[[False]*m for _ in range(n)]
    visit[ax][ay]=True
    parent=dict()
    ok=False # 최단 루트 존재 여부

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if not inBoard(nx,ny):
                nx,ny=outBoard(nx,ny)
            if a[nx][ny]>0 and visit[nx][ny]==False:
                visit[nx][ny]=True
                q.append((nx,ny))
                parent[(nx,ny)]=(x,y)
                # 공격 대상 찾았으면 최단 경로 존재
                if (nx,ny)==(tx,ty):
                    ok=True
    # 최단 경로 존재하지 않으면 False 반환
    if ok==False:
        return [None,False]

    start=(ax,ay)
    end=(tx,ty)
    current=end
    route=[current]
    while current!=start:
        current=parent[current]
        route.append(current)
    route.reverse() # 최단 루트

    return [route,True]

def laser(route):
    global a,c

    # 공격대상 공격력 감소
    a[tx][ty]-=a[ax][ay]
    # 최단 루트에서 공격자, 공격대상 제외
    route=route[1:-1]
    # 공격 대상 제외한 경로에 있는 포탑들 공격력 절반만큼 피해, 공격관여 업데이트
    for x,y in route:
        a[x][y]-=a[ax][ay]//2
        c[x][y]=True

def canon():
    global a,c

    # 공격대상 공격력 감소
    a[tx][ty]-=a[ax][ay]
    # 공격대상 주위 8개 공격 - 공격력 절반만큼(공격자 해당X), 공격관여 업데이트
    x,y=tx,ty
    for k in range(8):
        nx,ny=x+dx1[k],y+dy1[k]
        if not inBoard(nx, ny):
            nx, ny = outBoard(nx, ny)
        if a[nx][ny] > 0 and (nx,ny)!=(ax,ay):
            a[nx][ny]-=a[ax][ay]//2
            c[nx][ny]=True

def attack():
    route,ok = bfs()
    # 최단 경로 존재하면 레이저 공격
    if ok:
        laser(route)
    # 최단 경로 존재하지 않으면 포탄 공격
    else:
        canon()

def zeroCheck():
    global a

    for x in range(n):
        for y in range(m):
            if a[x][y]<=0:
                a[x][y]=0

def stop():
    cnt=0
    for x in range(n):
        for y in range(m):
            if a[x][y]>0:
                cnt+=1
    if cnt==1:
        return True
    return False

def fix():
    global a

    for x in range(n):
        for y in range(m):
            if a[x][y]==0 or c[x][y]:continue
            a[x][y]+=1

for round in range(1,K+1):
    # 공격자 선정
    selectAttacker(round)
    # 공격대상 선정
    selectAttacked(round)
    # 공격 시도
    attack()
    # 포탑 부서짐
    zeroCheck()
    # 포탑 수 확인 - 부서지지 않은 포탑 1개만 남아있을 경우 중지
    ok=stop()
    if ok:
        break
    # 포탑 정비
    fix()
    # 공격 관여 초기화
    c=[[False]*m for _ in range(n)] # 공격관여

max_val=-1
for x in range(n):
    for y in range(m):
        max_val=max(max_val,a[x][y])

print(max_val)