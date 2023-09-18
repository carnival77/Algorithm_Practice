import sys
input=sys.stdin.readline

n,m,r=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
tboard=[[-1]*n for _ in range(n)] # 팀별 번호 및 위치 상태 보드
visit=[[False]*n for _ in range(n)]
ans=0

teams=[[] for _ in range(m)] # 팀별 머리사람부터 시작하는 칸 위치 배열
team_cnt=[0]*m # 팀별 팀원 수

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def inBoard(nx,ny):
    return 0<=nx<n and 0<=ny<n

def dfs(x,y,tno):

    visit[x][y]=True
    tboard[x][y]=tno
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if not inBoard(nx,ny):
            continue
        # 이미 지나간 경로거나 경로가 아니면 넘어갑니다.
        if board[nx][ny]==0 or visit[nx][ny]:
            continue

        # 가장 처음 탐색할 때 2가 있는 방향으로 dfs를 진행합니다.
        # 머리사람 하나만 있고 다음 칸이 일반 사람이 아니면 넘어간다.
        if len(teams[tno]) == 1 and board[nx][ny] != 2:
            continue

        teams[tno].append([nx,ny])
        if board[nx][ny]==3:
            team_cnt[tno]=len(teams[tno])
        dfs(nx,ny,tno)

# 포인트 합산
def calculate(x,y):

    tno=tboard[x][y]
    dist=teams[tno].index([x,y])+1
    return dist**2

# 공 던지고 포인트 획득
def cycle(inx,a,kind):
    global ans

    if kind==1:
        row = inx % n
        for y in range(n):
            if 1 <= a[row][y] <= 3:
                ans += calculate(row, y)
                return tboard[row][y]

    elif kind==2:
        col = inx % n
        for x in range(n - 1, -1, -1):
            if 1 <= a[x][col] <= 3:
                ans += calculate(x, col)
                return tboard[x][col]

    elif kind==3:
        row = (n - 1) - inx % n
        for y in range(n - 1, -1, -1):
            if 1 <= a[row][y] <= 3:
                ans += calculate(row, y)
                return tboard[row][y]

    else:
        col = (n - 1) - inx % n
        for x in range(n):
            if 1 <= a[x][col] <= 3:
                ans += calculate(x, col)
                return tboard[x][col]

    # 공이 그대로 지나간다면 -1을 반환합니다.
    return -1

# 보드에서 팀 이동 적용
def change_board():
    for tno in range(m):
        for j,[x,y] in enumerate(teams[tno]):
            if j==0:
                board[x][y]=1
            elif j<team_cnt[tno]-1:
                board[x][y]=2
            elif j==team_cnt[tno]-1:
                board[x][y]=3
            else:
                board[x][y]=4

# 각 팀을 이동시키는 함수
def move_all():
    global teams,board,team_cnt

    for tno in range(m):
        # 각 팀에 대해 레일을 한 칸씩 뒤로 이동시킨다. 즉 맨 뒤 레일을 맨 앞으로 가져온다. 이것은 머리사람을 따라 한 칸 이동한 것과 같다.
        teams[tno]=[teams[tno][-1]]+teams[tno][:-1]

    change_board()

def reverse(tno):
    if tno==-1:
        return

    cnt=team_cnt[tno]
    teams[tno]=teams[tno][:cnt][::-1]+teams[tno][cnt:][::-1]

    change_board()

# 각 팀별 레일 위치 배열 저장. 머리사람 위치부터 시작.
i=0
for x in range(n):
    for y in range(n):
        if board[x][y]==1:
            teams[i].append([x,y])
            i+=1

# dfs를 통해 머리사람 위치 이후의 레일을 배열에 순서대로 삽입.
for i in range(m):
    x,y=teams[i][0]
    dfs(x,y,i)

cnt=1
inx=1

while cnt<=r:
    # 각 팀을 머리사람을 따라 한 칸씩 이동
    move_all()
    # 공 던지기 및 점수 획득
    if 1<=inx<=n:
        tno=cycle(inx-1,board,1)
    elif n+1<=inx<=2*n:
        tno=cycle(inx-1,board,2)
    elif 2*n+1<=inx<=3*n:
        tno=cycle(inx-1,board,3)
    else:
        tno=cycle(inx-1,board,4)
    # 공을 획득한 팀의 방향을 바꿉니다.
    reverse(tno)
    inx+=1
    cnt+=1
    if inx>4*n:
        inx-=4*n
print(ans)