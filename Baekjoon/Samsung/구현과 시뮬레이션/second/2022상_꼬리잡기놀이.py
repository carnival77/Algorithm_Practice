import sys
from collections import deque
input=sys.stdin.readline

n,m,R=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] # 0은 빈칸, 1은 머리사람, 2는 머리사람과 꼬리사람이 아닌 나머지, 3은 꼬리사람, 4는 이동 선
g=[[9]*n for _ in range(n)] # 팀별 번호 맵. 팀 넘버는 0~4로 표시
head=[] # 머리사람 위치
tail=[] # 꼬리사람 위치
ans=0

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

# 3명 이상이 한 팀이 됩니다.
# 모든 사람들은 자신의 앞 사람의 허리를 잡고 움직이게 되며,
# 맨 앞에 있는 사람을 머리사람, 맨 뒤에 있는 사람을 꼬리사람이라고 합니다.
# 각 팀은 게임에서 주어진 이동 선을 따라서만 이동합니다.
# 각 팀의 이동 선은 끝이 이어져있습니다.
# 각 팀의 이동 선은 서로 겹치지 않습니다.
def bfs(sx,sy,visited,no):
    global g

    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=True
    tx,ty=0,0
    g[sx][sy]=no

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and not visited[nx][ny] and a[nx][ny]!=0:
                q.append((nx, ny))
                visited[nx][ny] = True
                g[nx][ny]=no
                if a[nx][ny]==3:
                    tx,ty=nx,ny
    g[tx][ty]=no
    
    return [tx,ty,visited]

# 초기 팀 파악
def init():
    global head,tail

    visited = [[False] * n for _ in range(n)]

    no=0
    for x in range(n):
        for y in range(n):
            if visited[x][y]: continue
            if a[x][y]==1:
                head.append([x,y])
                tx,ty,visited=bfs(x,y,visited,no)
                tail.append([tx,ty])
                no+=1

def move(x,y,kind):
    global a, head, tail

    # 머리사람 이동
    if kind==0:
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if not inBoard(nx,ny):continue
            if 3<=a[nx][ny]<=4:
                return [nx,ny]

    # 꼬리사람 이동
    else:
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not inBoard(nx, ny): continue
            if a[nx][ny] == 2:
                return [nx,ny]

# 먼저 각 팀은 머리사람을 따라서 한 칸 이동
def teamMove():
    global head,tail,a

    b=[row[:] for row in a]

    for i in range(m):
        x, y=head[i]
        nx,ny=move(x,y,0)
        b[nx][ny] = 1
        head[i] = [nx, ny]
        b[x][y]=2
    for i in range(m):
        x, y = tail[i]
        nx, ny = move(x, y, 1)
        b[nx][ny] = 3
        tail[i] = [nx, ny]
        if b[x][y]!=1:
            b[x][y] = 4

    a=b

def dfs(x,y,checked,order):

    if a[x][y]==1:
        return order

    res=0
    cand=[]
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if inBoard(nx,ny) and not checked[nx][ny] and 1<=a[nx][ny]<=2:
            cand.append([a[nx][ny],nx,ny])
    if len(cand) > 0:
        cand.sort(reverse=True)
        for num,nx,ny in cand:
            checked[nx][ny]=True
            res=dfs(nx, ny, checked, order+1)
            checked[nx][ny] = False
            if res!=0:
                break
    return res

# 공을 획득한 팀의 경우에는 머리사람과 꼬리사람이 바뀝니다. 즉 방향을 바꾸게 됩니다.
def change(no):
    global head,tail,a

    hx,hy=head[no]
    tx,ty=tail[no]
    head[no],tail[no]=tail[no],head[no]
    a[hx][hy],a[tx][ty]=a[tx][ty],a[hx][hy]

# 공이 던져지는 경우에 해당 선에 사람이 있으면
# 최초에 만나게 되는 사람만이 공을 얻게 되어 점수를 얻게 됩니다.
# 점수는 해당 사람이 머리사람을 시작으로 팀 내에서 k번째 사람이라면 k의 제곱만큼 점수를 얻게 됩니다.
# 아무도 공을 받지 못하는 경우에는 아무 점수도 획득하지 못합니다
def process(kind,r):
    global ans

    ok=False
    order=0
    no=0
    checked = [[False] * n for _ in range(n)]

    if kind==1:
        x=r
        for y in range(n):
            if 1<=a[x][y]<=3:
                checked[x][y]=True
                order=dfs(x,y,checked,1)
                no = g[x][y]
                ok=True
                break

    elif kind==2:
        y=r
        for x in range(n-1,-1,-1):
            if 1<=a[x][y]<=3:
                checked[x][y] = True
                order=dfs(x,y,checked,1)
                no = g[x][y]
                ok = True
                break

    elif kind==3:
        x=n-1-r
        for y in range(n-1,-1,-1):
            if 1<=a[x][y]<=3:
                checked[x][y] = True
                order=dfs(x,y,checked,1)
                no = g[x][y]
                ok = True
                break

    else:
        y=n-1-r
        for x in range(n):
            if 1<=a[x][y]<=3:
                checked[x][y] = True
                order=dfs(x,y,checked,1)
                no = g[x][y]
                ok = True
                break

    if ok:
        ans += order ** 2
        change(no)

# 각 라운드마다 공이 정해진 선을 따라 던져집니다.
# 4n번째 라운드를 넘어가는 경우에는 다시 1번째 라운드의 방향으로 돌아갑니다.
def throw(round):

    round%=4*n
    r=(round-1)%n

    if 1<=round<=n:
        process(1,r)
    elif n+1<=round<=2*n:
        process(2,r)
    elif 2*n+1<=round<=3*n:
        process(3,r)
    else:
        process(4,r)

# 팀 파악
init()

for round in range(1,R+1):
    # 팀 이동
    teamMove()
    # 공 던지기
    throw(round)

print(ans)