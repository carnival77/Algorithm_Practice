from collections import deque

n,m,K=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] # 포탑 공격력 맵
b=[[0]*m for _ in range(n)] # 포탑 공격 관여 맵
c=[[0]*m for _ in range(n)] # 포탑 공격 시점 맵
ax,ay=-1,-1 # 공격자 위치
tx,ty=-1,-1 # 공격대상 위치
ans=0

#  우/하/좌/상의 우선순위
dx=[0,1,0,-1]
dy=[1,0,-1,0]

# 8개 방향
dx1=[0,1,0,-1,-1,1,1,-1]
dy1=[1,0,-1,0,-1,1,-1,1]

# 만약 부서지지 않은 포탑이 1개가 된다면 그 즉시 중지
def check():
    cnt=0
    for x in range(n):
        for y in range(m):
            if a[x][y]!=0:
                cnt+=1
    if cnt==1:
        return True
    return False

def choose():
    global ax,ay,tx,ty,a,c

    # 공격자 선정
    # 가장 약한 포탑은 다음의 기준으로 선정됩니다.
    # 공격력이 가장 낮은 포탑이 가장 약한 포탑입니다.
    # 만약 공격력이 가장 낮은 포탑이 2개 이상이라면, 가장 최근에 공격한 포탑이 가장 약한 포탑입니다. (모든 포탑은 시점 0에 모두 공격한 경험이 있다고 가정하겠습니다.)
    # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 행과 열의 합이 가장 큰 포탑이 가장 약한 포탑입니다.
    # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 큰 포탑이 가장 약한 포탑입니다.
    
    # 공격 대상 선정
    # 공격력이 가장 높은 포탑이 가장 강한 포탑입니다.
    # 만약 공격력이 가장 높은 포탑이 2개 이상이라면, 공격한지 가장 오래된 포탑이 가장 강한 포탑입니다. (모든 포탑은 시점 0에 모두 공격한 경험이 있다고 가정하겠습니다.)
    # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 행과 열의 합이 가장 작은 포탑이 가장 강한 포탑입니다.
    # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 작은 포탑이 가장 강한 포탑입니다.
    cand=[]
    for x in range(n):
        for y in range(m):
            if a[x][y]==0:continue
            cand.append([a[x][y],c[x][y],x+y,y,x])
    cand.sort(key=lambda x:(x[0],-x[1],-x[2],-x[3]))
    ay,ax=cand[0][-2],cand[0][-1]
    ty, tx = cand[-1][-2], cand[-1][-1]

    # N+M만큼의 공격력이 증가
    a[ax][ay]+=(n+m)
    c[ax][ay]=round # 공격 시점 업데이트

def outBoard(nx,ny):
    if nx==n:
        nx=0
    if nx==-1:
        nx=n-1
    if ny==m:
        ny=0
    if ny==-1:
        ny=m-1
    return [nx,ny]

# 상하좌우의 4개의 방향으로 움직일 수 있습니다.
# 부서진 포탑이 있는 위치는 지날 수 없습니다.
# 가장자리에서 막힌 방향으로 진행하고자 한다면, 반대편으로 나옵니다
# 만약 경로의 길이가 똑같은 최단 경로가 2개 이상이라면,
# 우/하/좌/상의 우선순위대로 먼저 움직인 경로가 선택됩니다.
def bfs(sx,sy,ex,ey):

    q=deque()
    q.append((sx,sy))
    d=[[-1]*m for _ in range(n)]
    d[sx][sy]=0
    parent=dict()

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            nx,ny=outBoard(nx,ny)
            if d[nx][ny]==-1 and a[nx][ny]>0:
                q.append((nx,ny))
                d[nx][ny]=d[x][y]+1
                parent[(nx,ny)]=(x,y)

    if d[ex][ey]==-1:
        return None
    else:
        start=(sx,sy)
        end=(ex,ey)
        route=[end]
        current=end
        while current!=start:
            current=parent[current]
            route.append(current)
        route.reverse()

        return route

# 레이저 공격은 공격자의 위치에서 공격 대상 포탑까지의 최단 경로로 공격
# 또한 공격 대상을 제외한 레이저 경로에 있는 포탑도 공격을 받게 되는데, 
# 이 포탑은 공격자 공격력의 절반 만큼의 공격을 받습니다
def laser():
    global a,b

    route=bfs(ax,ay,tx,ty)
    if route is None:
        return False
    else:
        for x,y in route:
            if (x,y)==(ax,ay) or (x,y)==(tx,ty): continue
            a[x][y]-=a[ax][ay]//2
            b[x][y]=round

        return True

# 주위 8개의 방향에 있는 포탑도 피해를 입는데, 공격자 공격력의 절반 만큼의 피해를 받습니다
# 공격자는 해당 공격에 영향을 받지 않습니다. 만약 가장자리에 포탄이 떨어졌다면,
# 위에서의 레이저 이동처럼 포탄의 추가 피해가 반대편 격자에 미치게 됩니다.
def cannon():
    global a,b

    x,y=tx,ty
    for k in range(8):
        nx,ny=x+dx1[k],y+dy1[k]
        nx,ny=outBoard(nx,ny)
        if a[nx][ny]>0 and (nx,ny)!=(ax,ay):
            a[nx][ny]-=a[ax][ay]//2
            b[nx][ny]=round

def attack():

    # 레이저 공격
    ok=laser()
    # 포탑 공격
    if not ok:
        cannon()

    # 공격 대상은 공격자 공격력 만큼의 피해를 받습니다
    a[tx][ty] -= a[ax][ay]
    b[ax][ay] = b[tx][ty] = round

def remove():
    global a,b

    for x in range(n):
        for y in range(m):
            if a[x][y]<=0:
                a[x][y]=b[x][y]=c[x][y]=0

def repair():

    for x in range(n):
        for y in range(m):
            if b[x][y]!=round and a[x][y]!=0:
                a[x][y]+=1

for round in range(1,K+1):
    # 포탑 파악
    if check():
        break
    # 공격자, 공격 대상 선정
    choose()
    # 공격
    attack()
    # 포탑 부서짐
    remove()
    # 포탑 정비
    repair()


ans=max([max(row) for row in a])
print(ans)