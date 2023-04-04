import sys
from collections import deque
input=sys.stdin.readline

n,m,r=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
tboard=[[-1]*n for _ in range(n)]
visit=[[False]*n for _ in range(n)]
ans=0

class Team:
    def __init__(self,no,cnt,head=None,tail=None):
        self.no=no
        self.cnt=cnt
        self.head=head
        self.tail=tail
teams=[]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def inBoard(nx,ny):
    return 0<=nx<n and 0<=ny<n

def classify(x,y,team):
    global board

    if board[x][y]==1:
        team.head=[x,y]
    elif board[x][y]==3:
        team.tail=[x,y]
    return team

def bfs(sx,sy):
    global board,tboard,visit,teams

    q=deque()
    q.append([sx,sy])
    visit[sx][sy]=True
    no=len(teams)
    team=Team(no,1)
    team=classify(sx,sy,team)
    tboard[sx][sy]=no

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny):
                if board[nx][ny]!=0 and not visit[nx][ny]:
                    visit[nx][ny]=True
                    q.append([nx,ny])
                    tboard[nx][ny]=no
                    team=classify(nx,ny,team)
                    if 1<=board[nx][ny]<=3:
                        team.cnt += 1

    return team

def move(team,a):
    first=team.head
    x,y=first
    moved=None
    b=[[-1]*n for _ in range(n)]
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if not inBoard(nx,ny): continue
        if 3<=a[nx][ny]<=4:
            b[nx][ny]=a[x][y]
            # a[x][y]=4
            team.head=[nx,ny]
            moved=[x,y]
        elif a[nx][ny]==2:
            first=[nx,ny]

    for _ in range(team.cnt-1):
        fx,fy=first
        mx,my=moved
        b[mx][my]=a[fx][fy]
        # a[mx][my]=4
        if first==team.tail:
            a[fx][fy]=4
            team.tail=moved
            break
        moved = first
        for k in range(4):
            nx,ny=fx+dx[k],fy+dy[k]
            if not inBoard(nx,ny):continue
            # if 2<=a[nx][ny]<=3:
            if (nx,ny)!=(mx,my) and a[nx][ny]!=0:
                first=[nx,ny]
        # moved = first

    for x in range(n):
        for y in range(n):
            if b[x][y]!=-1:
                a[x][y]=b[x][y]

    return [team,a]

def bfs2(sx,sy,a):
    q=deque()
    q.append([sx,sy])
    d=[[-1]*n for _ in range(n)]
    d[sx][sy]=1

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if not inBoard(nx,ny):continue
            if 1<=a[nx][ny]<=3:
                d[nx][ny]=d[x][y]+1
                if a[nx][ny]==1:
                    return (d[nx][ny])**2
                elif a[nx][ny]==2:
                    q.append([nx,ny])

def calculate(x,y,a):
    global tboard,teams
    if a[x][y]==1:
        return 1
    elif a[x][y]==3:
        no=tboard[x][y]
        team=teams[no]
        return team.cnt**2
    else:
        return bfs2(x,y,a)

def changeHeadTail(x,y):
    global tboard,teams,board
    no=tboard[x][y]
    team=teams[no]
    hx,hy=team.head
    tx,ty=team.tail
    board[hx][hy],board[tx][ty]=board[tx][ty],board[hx][hy]
    team.head,team.tail=team.tail,team.head
    teams[no]=team

def cycle1n(inx,a):
    global ans
    row=inx%n
    for y in range(n):
        if 1<=a[row][y]<=3:
            ans += calculate(row, y, a)
            changeHeadTail(row, y)
            break

def cycle2n(inx,a):
    global ans
    col=inx%n
    for x in range(n-1,-1,-1):
        if 1<=a[x][col]<=3:
            ans += calculate(x, col, a)
            changeHeadTail(x, col)
            break

def cycle3n(inx,a):
    global ans
    row=(n-1)-inx%n
    for y in range(n-1,-1,-1):
        if 1<=a[row][y]<=3:
            ans += calculate(row, y, a)
            changeHeadTail(row, y)
            break

def cycle4n(inx,a):
    global ans
    col=(n-1)-inx%n
    for x in range(n):
        if 1<=a[x][col]<=3:
            ans += calculate(x, col, a)
            changeHeadTail(x, col)
            break

for x in range(n):
    for y in range(n):
        if board[x][y]!=0 and not visit[x][y]:
            team=bfs(x,y)
            teams.append(team)

cnt=1
inx=1

while cnt<=r:
    # 팀 이동
    for team in teams:
        team,board=move(team,board)
    # 공 던지기 및 점수 획득
    if 1<=inx<=n:
        cycle1n(inx-1,board)
    elif n+1<=inx<=2*n:
        cycle2n(inx-1,board)
    elif 2*n+1<=inx<=3*n:
        cycle3n(inx-1,board)
    else:
        cycle4n(inx-1,board)
    inx+=1
    cnt+=1
    if inx>4*n:
        inx-=4*n
print(ans)