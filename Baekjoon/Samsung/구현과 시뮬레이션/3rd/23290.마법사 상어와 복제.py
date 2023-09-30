m,s=map(int,input().split())

# 물고기 방향
dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]

# 상어 방향
#  상,좌,하,우
dx1=[-1,0,1,0]
dy1=[0,-1,0,1]

n=4
a=[[[] for _ in range(n)] for _ in range(n)] # 물고기 맵
b=[] # 복제 물고기 맵
c=[[0]*n for _ in range(n)] # 냄새 맵
route=[] # 상어 이동 루트
prod=[]

for _ in range(m):
    x,y,d=map(int,input().split())
    x-=1
    y-=1
    d-=1
    a[x][y].append(d)

ax,ay=map(int,input().split()) # 상어 위치
ax-=1
ay-=1

ans=0

def dfs(index,nums,arr,used,n,m):
    global prod

    if index==m:
        prod.append(arr[:])
        return

    for i in range(n):
        arr[index]=nums[i]
        used[i]=True
        dfs(index+1,nums,arr,used,n,m)
        used[i]=False

def product(nums,m):
    n=len(nums)
    arr=[0]*m
    used=[False]*n
    index=0
    dfs(index,nums,arr,used,len(nums),m)

def copyBoard(a):
    b=[[[] for _ in range(4)] for _ in range(4)]
    for x in range(n):
        for y in range(n):
            b[x][y]=a[x][y][:]
    return b

# 상어가 모든 물고기에게 복제 마법을 시전한다
def doDuplicate():
    global b

    b=copyBoard(a)

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

# 모든 물고기가 한 칸 이동한다.
# 상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다.
# 각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
# 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다.
# 그 외의 경우에는 그 칸으로 이동을 한다.
def moveFish():
    global a,c

    tmp=[[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if len(a[x][y])==0:continue
            for d in a[x][y]:
                ok = False
                nd=d
                for k in range(8):
                    nx,ny=x+dx[nd],y+dy[nd]
                    if not inBoard(nx,ny) or (nx,ny)==(ax,ay) or c[nx][ny]>0:
                        nd=(nd-1)%8
                    else:
                        ok=True
                        break
                if ok:
                    tmp[nx][ny].append(nd)
                else:
                    tmp[x][y].append(d)
    a=tmp

def check(prod):

    x,y=ax,ay
    dx,dy=dx1,dy1
    cnt=0

    tmp=copyBoard(a)

    for d in prod:
        nx,ny=x+dx[d],y+dy[d]
        if not inBoard(nx,ny):
            return None
        if len(tmp[nx][ny])>0:
            cnt+=len(tmp[nx][ny])
            tmp[nx][ny].clear()
        x,y=nx,ny

    return cnt

# 상어가 연속해서 3칸 이동한다.
# 상어는 현재 칸에서 상하좌우로 인접한 칸으로 이동할 수 있다.
# 연속해서 이동하는 칸 중에 격자의 범위를 벗어나는 칸이 있으면, 그 방법은 불가능한 이동 방법이다.
# 연속해서 이동하는 중에 상어가 물고기가 있는 같은 칸으로 이동하게 된다면, 그 칸에 있는 모든 물고기는 격자에서 제외되며, 제외되는 모든 물고기는 물고기 냄새를 남긴다.
# 가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며, 그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용한다
def moveShark(round):
    global a,c,ax,ay,route

    x,y=ax,ay
    dx,dy=dx1,dy1

    cand=[]
    for p in prod:
        cnt=check(p)
        if cnt is None:
            continue
        cand.append([cnt,p])

    cand.sort(key=lambda x:(-x[0],x[1]))
    route=cand[0][1]

    for d in route:
        nx, ny = x + dx[d], y + dy[d]
        if len(a[nx][ny])>0:
            c[nx][ny]=round
            a[nx][ny].clear()
        x, y = nx, ny

    ax,ay=x,y

# 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
def remove(round):
    global c

    for x in range(n):
        for y in range(n):
            if c[x][y]==round-2:
                c[x][y]=0

# 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.
def doneDuplicate():
    global a,b

    for x in range(n):
        for y in range(n):
            if len(b[x][y])>0:
                for d in b[x][y]:
                    a[x][y].append(d)

product([0,1,2,3],3)
for round in range(1,s+1):

    # 복제 마법 시전
    doDuplicate()
    # 물고기 이동
    moveFish()
    # 상어 이동
    moveShark(round)
    # 물고기 냄새 제거
    remove(round)
    # 복제 마법 완료
    doneDuplicate()

for x in range(n):
    for y in range(n):
        ans+=len(a[x][y])
print(ans)