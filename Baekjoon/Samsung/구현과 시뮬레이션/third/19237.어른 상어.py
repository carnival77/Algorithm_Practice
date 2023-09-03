import sys
input=sys.stdin.readline

class Shark:
    def __init__(self,no,d,x,y):
        self.no=no
        self.d=d
        self.x=x
        self.y=y

#   상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m,l=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] # 상어
first_dirs=list(map(int,input().split())) # 초기 방향
smell_no=[[0]*n for _ in range(n)] # 냄새 번호
smell=[[0]*n for _ in range(n)] # 남은 냄새
sharks=[None]*(m+1) # 상어 객체 배열

for x in range(n):
    for y in range(n):
        if a[x][y]!=0:
            no=a[x][y]
            d=first_dirs[no-1]-1
            sharks[no]=Shark(no,d,x,y)

dirs=[[[[]] for _ in range(4)] for _ in range(m+1)] # 상어별 방향
for i in range(1,m+1):
    for j in range(4):
        dirs[i][j]=list(map(int,input().split()))
        for k in range(4):
            dirs[i][j][k]-=1

# 냄새 남기기
def leave():
    global smell,smell_no

    for x in range(n):
        for y in range(n):
            if a[x][y]!=0:
                smell[x][y]=l
                smell_no[x][y]=a[x][y]

# 냄새 줄이거나 제거
def remove():
    global smell,smell_no

    for x in range(n):
        for y in range(n):
            if smell[x][y] >0:
                smell[x][y]-=1
                if smell[x][y]==0:
                    smell_no[x][y]=0

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

# 상어 이동
# 각 상어가 이동 방향을 결정할 때는,
# 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
# 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
# 이때 가능한 칸이 여러 개일 수 있는데,
# 그 경우에는 특정한 우선순위를 따른다.
# 우선순위는 상어마다 다를 수 있고,
# 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다.
# 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고,
# 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.
# 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면,
# 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.
def move():
    global a,sharks

    for shark in sharks:
        if shark==None: continue

        x=shark.x
        y=shark.y
        no=shark.no
        cd=shark.d

        dir=dirs[no][cd]
        ok1=False # 움직이기
        ok2=False # 상대 존재
        for d in dir:
            nx,ny=x+dx[d],y+dy[d]
            if not inBoard(nx,ny): continue
            if smell[nx][ny]==0:
                ok1=True
                if a[nx][ny]!=0:
                    ok2=True
                    t_no=a[nx][ny]
                break
        if not ok1:
            for d in dir:
                nx, ny = x + dx[d], y + dy[d]
                if not inBoard(nx, ny): continue
                if smell_no[nx][ny] == no:
                    ok1 = True
                    if a[nx][ny] != 0:
                        ok2 = True
                        t_no = a[nx][ny]
                    break

        if ok1:
            a[x][y]=0
            if ok2:
                if no<t_no:
                    a[nx][ny]=no
                    shark.d=d
                    shark.x=nx
                    shark.y=ny
                    sharks[t_no]=None
                elif no>t_no:
                    sharks[no]=None
            else:
                a[nx][ny] = no
                shark.d = d
                shark.x = nx
                shark.y = ny

# 남은 상어 체크
def check():
    for no in range(2,m+1):
        if sharks[no] is not None:
            return False
    return True

# 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다
leave()

for turn in range(1,1001):
    # 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고,
    move()
    # 냄새는 상어가 k번 이동하고 나면 사라진다.
    remove()
    # 자신의 냄새를 그 칸에 뿌린다
    leave()
    # 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지
    if check():
        print(turn)
        sys.exit(0)

print(-1)