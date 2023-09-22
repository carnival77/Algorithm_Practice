import sys
input=sys.stdin.readline

class Player:
    def __init__(self,no,x,y,d,s,g=0):
        self.no=no
        self.x=x
        self.y=y
        self.d=d
        self.s=s
        self.g=g

n,m,K=map(int,input().split())

#  상,우,하,좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]

a=[[[] for _ in range(n)] for _ in range(n)] # 플레이어 맵
b=[[[] for _ in range(n)] for _ in range(n)]
gdata=[list(map(int,input().split())) for _ in range(n)] # 총 데이터
for x in range(n):
    for y in range(n):
        if gdata[x][y]!=0:
            b[x][y].append(gdata[x][y])

players=[]
points=[0]*m
for no in range(m):
    x,y,d,s=map(int,input().split())
    x-=1
    y-=1
    player=Player(no,x,y,d,s)
    a[x][y].append(player)
    players.append(player)

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def leave(p,nx,ny):
    global b

    if p.g!=0:
        b[nx][ny].append(p.g)
        p.g=0

def get(nx,ny,p):
    global b

    if len(b[nx][ny])>0:
        b[nx][ny].sort(reverse=True)
        p.g = b[nx][ny].pop(0)

def battle(p1,p2):
    global points

    # 해당 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합을 비교하여 더 큰 플레이어가 이기게 됩니다.
    winner,loser=None,None
    s1=p1.s
    s2=p2.s
    t1=s1+p1.g
    t2=s2+p2.g

    if t1>t2:
        winner=p1
        loser=p2
    elif t1<t2:
        winner=p2
        loser=p1
    # 만일 이 수치가 같은 경우에는 플레이어의 초기 능력치가 높은 플레이어가 승리하게 됩니다.
    else:
        if s1>s2:
            winner=p1
            loser=p2
        elif s1<s2:
            winner=p2
            loser=p1

    # 이긴 플레이어는 각 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합의 차이만큼을 포인트로 획득하게 됩니다.
    points[winner.no]+=abs(t1-t2)

    return [winner,loser]

def move(x,y,nx,ny,p):
    global a

    a[x][y].remove(p)
    a[nx][ny].append(p)
    p.x, p.y = nx, ny

for round in range(1,K+1):
    # 첫 번째 플레이어부터 순차적으로
    for p in players:
        no, x, y, s, g = p.no, p.x, p.y, p.s, p.g
        nx, ny = x + dx[p.d], y + dy[p.d]
        # 본인이 향하고 있는 방향대로 한 칸만큼 이동합니다. 만약 해당 방향으로 나갈 때 격자를 벗어나는 경우에는 정반대 방향으로 방향을 바꾸어서 1만큼
        if not inBoard(nx, ny):
            p.d=(p.d+2)%4
            nx, ny = x+dx[p.d],y+dy[p.d]
        # 이동
        move(x, y, nx, ny, p)
        # 만약 이동한 방향에 플레이어가 없다면, 즉 움직인 플레이어 하나만 있다면
        if len(a[nx][ny]) == 1:
            # 해당 칸에 총이 있는지 확인합니다.
            # 총이 있는 경우, 해당 플레이어는 총을 획득합니다.
            if len(b[nx][ny]) != 0:
                # 플레이어가 이미 총을 가지고 있는 경우에는 놓여있는 총들과 플레이어가 가지고 있는 총 가운데 공격력이 더 쎈 총을 획득하고, 나머지 총들은 해당 격자에 둡니다.
                leave(p, nx, ny)
                get(nx, ny, p)
        # 만약 이동한 방향에 플레이어가 있는 경우에는 두 플레이어가 싸우게 됩니다
        elif len(a[nx][ny])>=2:
            winner, loser = battle(a[nx][ny][0], a[nx][ny][1])
            # 진 플레이어는 본인이 가지고 있는 총을 해당 격자에 내려놓고,
            leave(loser, nx, ny)
            # 해당 플레이어가 원래 가지고 있던 방향대로 한 칸 이동합니다.
            loser_x, loser_y, loser_d = loser.x, loser.y, loser.d
            loser_nx, loser_ny = loser_x + dx[loser_d], loser_y + dy[loser_d]
            # 만약 이동하려는 칸에 다른 플레이어가 있거나 격자 범위 밖인 경우에는
            if not inBoard(loser_nx, loser_ny) or len(a[loser_nx][loser_ny]) != 0:
                # 오른쪽으로 90도씩 회전하여 빈 칸이 보이는 순간 이동합니다.
                for _ in range(4):
                    loser_d = (loser_d + 1) % 4
                    loser_nx, loser_ny = loser_x + dx[loser_d], loser_y + dy[loser_d]
                    if inBoard(loser_nx, loser_ny) and len(a[loser_nx][loser_ny]) == 0:
                        break
                loser.d = loser_d
            # 패배자 이동
            move(loser_x, loser_y, loser_nx, loser_ny, loser)
            # 만약 해당 칸에 총이 있다면, 해당 플레이어는 가장 공격력이 높은 총을 획득하고 나머지 총들은 해당 격자에 내려 놓습니다.
            get(loser_nx, loser_ny, loser)
            # 이긴 플레이어는 승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려 놓습니다.
            leave(winner,nx,ny)
            get(nx, ny, winner)

print(*points)