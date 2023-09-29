from collections import deque

n,m,K=map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)] # 0은 빈칸, 1은 머리사람, 2는 머리사람과 꼬리사람이 아닌 나머지, 3은 꼬리사람, 4는 이동 선
b=[[0]*n for _ in range(n)] # 팀별 이동 선
heads=[None]+[0]*m
tails=[None]+[0]*m
teams=[None]+[0]*m # 각 팀별 머리사람부터 꼬리사람까지의 위치를 담은 큐
count=[None] # 팀별 인원수
ans=0

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def bfs(sx,sy,no,visit):
    global b

    q=deque()
    q.append((sx,sy))
    visit[sx][sy]=True
    team=deque()
    team.append([sx,sy])
    b[sx][sy]=no

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and not visit[nx][ny] and 2<=a[nx][ny]<=4:
                visit[nx][ny]=True
                b[nx][ny] = no
                if a[nx][ny]==2 or a[nx][ny]==4:
                    q.append((nx, ny))
                    if a[nx][ny]==2:
                        team.append([nx, ny])
                elif a[nx][ny]==3:
                    tx,ty=nx,ny

    team.append([tx,ty])

    return [visit,tx,ty,team]

def init():
    global heads,tails,teams,count

    visit=[[False]*n for _ in range(n)]
    no = 1
    for x in range(n):
        for y in range(n):
            if visit[x][y]:continue
            if a[x][y]==1:
                heads[no]=[x,y]
                visit,tx,ty,team=bfs(x,y,no,visit)
                tails[no]=[tx,ty]
                teams[no]=team
                count.append(len(team))
                no+=1

def getNext(sx,sy):

    x,y=sx,sy
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if not inBoard(nx,ny) or a[nx][ny]==0: continue
        if a[nx][ny]==4:
            return [nx,ny]

# 각 팀은 머리사람을 따라서 한 칸 이동
def move():
    global a,heads,tails,teams

    for tno in range(1,m+1):
        px,py=teams[tno].pop()
        a[px][py]=4
        tx,ty=teams[tno][-1]
        tails[tno]=[tx,ty]
        a[tx][ty]=3
        hx,hy=heads[tno]
        nx,ny=getNext(hx,hy)
        heads[tno]=[nx,ny]
        teams[tno].appendleft([nx,ny])
        a[hx][hy]=2
        a[nx][ny]=1

# 각 라운드마다 공이 정해진 선을 따라 던져집니다
# 4n번째 라운드를 넘어가는 경우에는 다시 1번째 라운드의 방향으로 돌아갑니다.
# 공이 던져지는 경우에 해당 선에 사람이 있으면 최초에 만나게 되는 사람만이 공을 얻게 되어 점수를 얻게 됩니다
def throw():

    share,remain=divmod(round,4*n)
    if remain!=0:
        r=remain
    else:
        r=4*n
    r-=1

    if 0<=r<n:
        x=r
        for y in range(n):
            if 1<=a[x][y]<=3:
                return [b[x][y],x,y]
    elif n<=r<2*n:
        y=r-n
        for x in range(n-1,-1,-1):
            if 1 <= a[x][y] <= 3:
                return [b[x][y], x, y]
    elif 2*n<=r<3*n:
        x=n-1-(r-2*n)
        for y in range(n-1,-1,-1):
            if 1 <= a[x][y] <= 3:
                return [b[x][y], x, y]
    else:
        y=n-1-(r-3*n)
        for x in range(n):
            if 1 <= a[x][y] <= 3:
                return [b[x][y], x, y]

    return -1

# 점수는 해당 사람이 머리사람을 시작으로 팀 내에서 k번째 사람이라면 k의 제곱만큼 점수를 얻게 됩니다
# 공을 획득한 팀의 경우에는 머리사람과 꼬리사람이 바뀝니다. 즉 방향을 바꾸게 됩니다.
def getPoint(tno,x,y):
    global ans,heads,tails,teams,a

    order=teams[tno].index([x,y])+1
    ans+=order**2
    teams[tno].reverse()
    team=teams[tno]
    heads[tno],tails[tno]=tails[tno],heads[tno]
    cnt=count[tno]
    for inx in range(cnt):
        x,y=team[inx]
        if inx==0:
            a[x][y]=1
        elif inx==cnt-1:
            a[x][y]=3
        else:
            a[x][y]=2

# 팀 정보 파악
init()

for round in range(1,K+1):

    # 팀 이동
    move()
    # 공 던지기
    res=throw()
    if res==-1:
        continue
    tno, ax, ay=res
    # 점수 획득
    getPoint(tno,ax,ay)

print(ans)