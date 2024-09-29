import sys
input=sys.stdin.readline

class Runaway:
    def __init__(self,no,x,y,d):
        self.no=no
        self.x=x
        self.y=y
        self.d=d

n,m,h,K=map(int,input().split())
ans=0
rs=[]
alive=[True]*m
a=[[0]*n for _ in range(n)] # 나무 맵. 1 : 나무 존재, 0 : 빈 칸
b=[[[] for _ in range(n)] for _ in range(n)] # 도망자 맵

#   상,우,하,좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for no in range(m):
    x,y,d=map(int,input().split())
    x-=1
    y-=1
    # 기준 : dx1,dy1 (우,하,좌,상)
    if d==1:
        d=1 # 우
    else:
        d=2 # 하
    rs.append(Runaway(no,x,y,d))
    b[x][y].append(no)

for _ in range(h):
    x,y=map(int,input().split())
    x-=1
    y-=1
    a[x][y]=1

# 술래의 현재 위치와 방향을 나타냅니다.
tx,ty=n//2,n//2
td=0
# 술래가 움직이는 방향이 정방향이면 1 / 아니라면 2.
kind=1

# 정방향 기준으로
# 현재 위치에서 술래가 움직여야 할 방향을 관리합니다.
next=[[0]*n for _ in range(n)]
# 역방향 기준으로
# 현재 위치에서 술래가 움직여야 할 방향을 관리합니다.
rev=[[0]*n for _ in range(n)]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

# 정중앙으로부터 끝까지 움직이는 경로를 계산해줍니다.
def setDirs():
    global next,rev

    # 시작 위치와 방향,
    # 해당 방향으로 이동할 횟수를 설정합니다.
    x=y=n//2
    d=0
    move_num=1

    while x or y:
        # move_num 만큼 이동합니다.
        for _ in range(move_num):
            next[x][y]=d
            x,y=x+dx[d],y+dy[d]
            rev[x][y]=(d+2)%4

            # 이동하는 도중 (0, 0)으로 오게 되면,
            # 움직이는 것을 종료합니다.
            if (x,y)==(0,0):
                break
        # 방향을 바꿉니다.
        d=(d+1)%4
        # 만약 현재 방향이 위 혹은 아래가 된 경우에는
        # 특정 방향으로 움직여야 할 횟수를 1 증가시킵니다.
        if d==0 or d==2:
            move_num+=1

    next[0][0]=2
    rev[n//2][n//2]=0

def fleeMove():
    global rs,b

    for no in range(m):
        if not alive[no] or rs[no] is None:continue
        r=rs[no]
        x,y,d=r.x,r.y,r.d
        dist=abs(x-tx)+abs(y-ty)
        if dist<=3:
            nx,ny=x+dx[d],y+dy[d]
            if not inBoard(nx,ny):
                d = (d + 2) % 4
                nx, ny = x + dx[d], y + dy[d]
                r.d=d
            if (nx,ny)!=(tx,ty):
                r.x,r.y=nx,ny
                b[x][y].remove(no)
                b[nx][ny].append(no)
# 현재 술래가 바라보는 방향을 가져옵니다.
def getTaggerDir():

    # 어느 방향으로 움직여야 하는지에 대한 정보를 가져옵니다.
    if kind==1:
        return next[tx][ty]
    else:
        return rev[tx][ty]

def checkFacing():
    global kind
    # Case 1. 정방향으로 끝에 다다른 경우라면, 방향을 바꿔줍니다.
    if kind==1 and (tx,ty)==(0,0):
        kind=2
    # Case 2. 역방향으로 끝에 다다른 경우여도, 방향을 바꿔줍니다.
    if kind==2 and (tx,ty)==(n//2,n//2):
        kind=1

def tagMove():
    global tx,ty,td

    td=getTaggerDir()
    # 술래를 한 칸 움직여줍니다.
    tx,ty=tx+dx[td],ty+dy[td]

    # 끝에 도달했다면 방향을 바꿔줘야 합니다.
    checkFacing()
    td = getTaggerDir()

def getScore():
    global b,alive,ans

    x,y,d=tx,ty,td
    cnt=0

    for k in range(3):
        nx,ny=x+dx[d]*k,y+dy[d]*k
        if inBoard(nx,ny) and a[nx][ny]==0 and len(b[nx][ny])>0:
            cnt+=len(b[nx][ny])
            for no in b[nx][ny]:
                alive[no]=False
                rs[no]=None
            b[nx][ny].clear()

    ans+=turn*cnt

setDirs()

for turn in range(1,K+1):
    # 도망자 이동
    fleeMove()
    # 술래 이동
    tagMove()
    # 점수 획득
    getScore()
    
print(ans)