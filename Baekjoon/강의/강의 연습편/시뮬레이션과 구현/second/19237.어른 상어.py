import sys
input=sys.stdin.readline

n,m,l=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] # 상어 위치

ans=0
#   0,상,하,좌,우
dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]

bno=[[0]*n for _ in range(n)] # 냄새 번호
bcnt=[[0]*n for _ in range(n)] # 냄새 수치
pr=[[[0]*4 for _ in range(5)] for _ in range(m+1)] # 상어별 우선순위

cd=[0]+list(map(int,input().split())) # 상어 현재 방향

for i in range(1,m+1):
    for j in range(1,5):
        pr[i][j]=list(map(int,input().split()))

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

# a에 1번 상어만 있는지
def check():
    for x in range(n):
        for y in range(n):
            if a[x][y]>=2:
                return False
    return True

def leave():
    for x in range(n):
        for y in range(n):
            if a[x][y]>=1:
                bno[x][y]=a[x][y]
                bcnt[x][y]=l

# 상어별 방향별 우선순위 기준 방향 설정
def choose(res,no,d):
    result = []
    arr = pr[no][d]
    for r in res:
        inx = arr.index(r[0])
        result.append([inx, r])
    result.sort()

    return result[0][1]

def decide(no,d,x,y):
    res = []

    # 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향
    for k in range(1,5):
        nx,ny=x+dx[k],y+dy[k]
        if inBoard(nx,ny) and bno[nx][ny]==0:
            res.append([k,[nx,ny]])

    if len(res)==1:
        return res[0]
    # 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다
    elif len(res)>1:
        return choose(res,no,d)

    # 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다
    for k in range(1,5):
        nx,ny=x+dx[k],y+dy[k]
        if inBoard(nx,ny) and bno[nx][ny]==no:
            res.append([k,[nx,ny]])

    if len(res)==1:
        return res[0]
    # 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다
    elif len(res)>1:
        return choose(res, no, d)

    return [d,[x,y]]

def decrease():
    global bcnt

    for x in range(n):
        for y in range(n):
            # 현재 상어가 없고 냄새 있는 칸은 냄새 감소
            if bcnt[x][y]>=1 and a[x][y]==0:
                bcnt[x][y]-=1
            # 냄새 수치가 0인 곳은 냄새 제거
            if bcnt[x][y]==0:
                bno[x][y]=0

def move():
    global a,cd

    b=[[0]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if a[x][y]==0:continue
            no=a[x][y]
            d=cd[no]
            nd,[nx,ny]=decide(no,d,x,y)
            if b[nx][ny]==0:
                b[nx][ny]=a[x][y]
            # 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다
            elif b[nx][ny]>a[x][y]:
                b[nx][ny]=a[x][y]
            elif b[nx][ny]<a[x][y]:
                pass
            cd[no]=nd

    a=b

# 상어 냄새 남기기
leave()

while True:
    if check() or ans>1000:
        break
    # 상어 이동 -
    # 각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
    # 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다.
    # 우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다.
    # 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.
    move()
    # 상어 냄새 남기기
    leave()
    # 상어 냄새 감소 및 제거
    decrease()

    ans+=1

# 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력
if ans>1000:
    print(-1)
else:
    print(ans)