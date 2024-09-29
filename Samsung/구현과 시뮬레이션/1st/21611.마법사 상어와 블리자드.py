import sys
input=sys.stdin.readline

n,m=map(int,input().split())
ans=[0]*4
route=[]
marr=[]
#  우,하,좌,상
dx=[0,1,0,-1]
dy=[1,0,-1,0]

#  상,하,좌,우
dx_=[-1,1,0,0]
dy_=[0,0,-1,1]

px,py=(n-1)//2,(n-1)//2

def inBoard(nx,ny):
    return 0<=nx<n and 0<=ny<n

def makeRoute():
    global route

    x,y,d=0,0,0
    visit=[[False]*n for _ in range(n)]
    route.append((x,y))
    visit[x][y]=True

    for _ in range(n**2-2):
        nx,ny=x+dx[d],y+dy[d]
        if not inBoard(nx,ny) or visit[nx][ny]:
            d=(d+1)%4
            nx,ny=x+dx[d],y+dy[d]
        route.append((nx,ny))
        visit[nx][ny]=True
        x,y=nx,ny

    route.reverse()

def attack(d,p,px,py):
    global board

    x,y=px,py
    for _ in range(1,p+1):
        nx,ny=x+dx_[d],y+dy_[d]
        if board[nx][ny]!=0:
            board[nx][ny]=0
        x,y=nx,ny

def move(kind):
    global marr,board

    if kind==1:
        tmp=[]
        for i in range(len(marr)):
            x,y=route[i]
            if board[x][y]!=0:
                tmp.append(marr[i])
                # marr=marr[:i]+marr[i+1:]
        marr=tmp

    if kind==2:
        tmp=[]
        for i in marr:
            if i!=0:
                tmp.append(i)
        marr=tmp

    board = [[0] * n for _ in range(n)]
    for i in range(len(marr)):
        x, y = route[i]
        board[x][y] = marr[i]

def remove():
    global marr,board,ans

    while True:
        marr.append(0)
        ok=False
        start=0
        pre=marr[0]
        for i in range(1,len(marr)):
            now=marr[i]
            if pre!=now:
                end = i - 1
                cnt=end-start+1
                if cnt>=4:
                    no=marr[end]
                    ans[no]+=cnt
                    ok=True
                    for j in range(start,end+1):
                        marr[j]=0
                start=i
            pre=now
        move(2)
        if not ok:
            break

def add():
    global marr,board

    marr.append(0) # 마지막에 임의의 수 삽입
    temp=[]
    pre=marr[0]
    start=0
    for i in range(1,len(marr)):
        now=marr[i]
        if pre!=now:
            end=i-1
            no=marr[end]
            cnt=end-start+1
            temp.append(cnt)
            temp.append(no)
            start=i
        pre=now
    marr=temp[:n**2-1]
    for i in range(len(marr)):
        x,y=route[i]
        board[x][y]=marr[i]

# 이동경로 생성
makeRoute()

# 몬스터 값 입력
board=[list(map(int,input().split())) for _ in range(n)]
for i,(x,y) in enumerate(route):
    if board[x][y]!=0:
        marr.append(board[x][y])

# 라운드 진행
for _ in range(m):
    # 공격
    d,p = map(int,input().split())
    attack(d-1,p,px,py)
    # 몬스터 이동
    move(1)
    # 몬스터 소멸
    remove()
    # 몬스터 증식
    add()
print(ans[1]*1+ans[2]*2+ans[3]*3)