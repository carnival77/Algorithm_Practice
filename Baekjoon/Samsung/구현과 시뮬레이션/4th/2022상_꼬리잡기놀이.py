import sys
from collections import deque
input=sys.stdin.readline

n,m,K=map(int,input().split())
# 0은 빈칸, 1은 머리사람, 2는 머리사람과 꼬리사람이 아닌 나머지, 3은 꼬리사람, 4는 이동 선
a=[list(map(int,input().split())) for _ in range(n)] # 사람 구분 맵
ans=0
team_no=5 # 팀 번호는 5부터 시작
b=[[0]*n for _ in range(n)] # 팀 번호 맵
teams=dict()
visit=[]

#  우,상,좌,하
dx=[0,-1,0,1]
dy=[1,0,-1,0]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

# 머리사람 기준 팀 파악
def bfs(sx,sy,team_no):
    global visit,teams,b

    q=deque()
    q.append((sx,sy))
    visit[sx][sy]=True
    b[sx][sy]=team_no
    team=deque()
    team.append([sx,sy])

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            # 네방향, 범위내, 미방문, 조건: 2 또는 출발지 아닌곳에서 온 3
            if not inBoard(nx,ny) or visit[nx][ny]:continue
            if a[nx][ny]==2 or (a[nx][ny]==3 and (sx,sy)!=(x,y)):
                q.append((nx,ny))
                visit[nx][ny]=True
                team.append([nx,ny])
                b[nx][ny]=team_no

    teams[team_no]=team

# 초기 팀 정보 파악
def init():
    global visit,team_no

    visit=[[False]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visit[x][y] and a[x][y]==1:# 머리위치인 경우
                bfs(x,y,team_no)
                team_no+=1
# 먼저 각 팀은 머리사람을 따라서 한 칸 이동합니다.
def move():
    global teams,a,b

    for team_no,team in teams.items():
        tx,ty=team.pop()
        a[tx][ty]=4
        b[tx][ty]=0
        new_tx,new_ty=team[-1]
        a[new_tx][new_ty]=3
        b[new_tx][new_ty]=team_no
        sx,sy=team[0]
        a[sx][sy]=2
        for k in range(4):
            nx,ny=sx+dx[k],sy+dy[k]
            if not inBoard(nx,ny):continue
            if a[nx][ny]==4:
                team.appendleft([nx,ny])
                a[nx][ny]=1
                b[nx][ny]=team_no
                break
# [2] 라운드 번호에 맞게 (방향, 시작위치) 계산
# 각 라운드마다 공이 정해진 선을 따라 던져집니다.
# 4n번째 라운드를 넘어가는 경우에는 다시 1번째 라운드의 방향으로 돌아갑니다.
def throw(round):

    dir=(round//n)%4
    offset=round%n

    if dir==0:
        sx=offset
        sy=0
    elif dir==1:
        sx=n-1
        sy=offset
    elif dir==2:
        sx=n-1-offset
        sy=n-1
    else:
        sx=0
        sy=n-1-offset

    return [dir,sx,sy]

# 공이 던져지는 경우에 해당 선에 사람이 있으면 최초에 만나게 되는 사람만이 공을 얻게 되어 점수를 얻게 됩니다.
# 점수는 해당 사람이 머리사람을 시작으로 팀 내에서 k번째 사람이라면 k의 제곱만큼 점수를 얻게 됩니다.
# 아무도 공을 받지 못하는 경우에는 아무 점수도 획득하지 못합니다
# 공을 획득한 팀의 경우에는 머리사람과 꼬리사람이 바뀝니다. 즉 방향을 바꾸게 됩니다.
def getScore(info):
    global ans,teams,b

    dir,sx,sy=info

    for i in range(n):
        nx,ny=sx+dx[dir]*i,sy+dy[dir]*i
        if inBoard(nx,ny) and b[nx][ny]>=5:# 특정 팀이 공 받았음
            team_no=b[nx][ny]
            team=teams[team_no]
            ans+=(team.index([nx,ny])+1)**2
            team.reverse()
            teams[team_no]=team
            for no,[x,y] in enumerate(team):
                if no==0:
                    a[x][y]=1
                elif no==len(team)-1:
                    a[x][y]=3
                else:
                    a[x][y]=2
            break

# 초기 팀 정보 파악
init()

for round in range(K):
    # 팀 이동
    move()
    # 공 던지기
    info=throw(round)
    # 공 맞으면 점수 획득 및 해당 팀 반대로
    getScore(info)

print(ans)

# [해설]
# 영상 : https://www.youtube.com/watch?v=y1_lca5hJHY
# 코드 : https://doctor-moon.notion.site/4800e49d779146d48a40a7af533d52c9
