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

#   상,우,하,좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m,r=map(int,input().split())
a=[[[] for _ in range(n)] for _ in range(n)] # 총 맵
for i in range(n):
    row=list(map(int,input().split()))
    for j in range(n):
        if row[j]==0: continue
        a[i][j].append(row[j])
b=[[0]*n for _ in range(n)] # 플레이어 맵
players=[]
for no in range(m):
    x,y,d,s=map(int,input().split())
    x-=1
    y-=1
    player=Player(no,x,y,d,s)
    b[x][y]=player
    players.append(player)
ans=[0]*m # 플레이어별 점수

def inBoard(nx1,ny1):
    if 0<=nx1<n and 0<=ny1<n:
        return True
    return False

# 총이 있는 경우, 해당 플레이어는 총을 획득합니다.
# 플레이어가 이미 총을 가지고 있는 경우에는 놓여있는 총들과 플레이어가 가지고 있는 총 가운데 공격력이 더 쎈 총을 획득하고, 나머지 총들은 해당 격자에 둡니다.
def get(p,x,y):
    global a

    if p.g!=0:
        a[x][y].append(p.g)
    a[x][y].sort(reverse=True)
    p.g=a[x][y].pop(0)

# 해당 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합을 비교하여 더 큰 플레이어가 이기게 됩니다.
# 만일 이 수치가 같은 경우에는 플레이어의 초기 능력치가 높은 플레이어가 승리하게 됩니다.
# 이긴 플레이어는 각 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합의 차이만큼을 포인트로 획득하게 됩니다.
def fight(p1,p2):
    global ans

    winner,loser=0,0
    s1=p1.s+p1.g
    s2=p2.s+p2.g
    if s1>s2:
        winner=p1
        loser=p2
    elif s1<s2:
        winner=p2
        loser=p1
    else:
        if p1.s>p2.s:
            winner = p1
            loser = p2
        elif p1.s<p2.s:
            winner = p2
            loser = p1

    ans[winner.no]+=(winner.s+winner.g)-(loser.s+loser.g)
    return [winner,loser]

for round in range(r):
    # 플레이어 이동
    for p in players:
        x,y=p.x,p.y
        b[x][y] = 0
        # 본인이 향하고 있는 방향대로 한 칸만큼 이동합니다.
        nx1,ny1=x+dx[p.d],y+dy[p.d]
        # 만약 해당 방향으로 나갈 때 격자를 벗어나는 경우에는 정반대 방향으로 방향을 바꾸어서 1만큼 이동
        if not inBoard(nx1,ny1):
            p.d=(p.d+2)%4
            nx1,ny1=x+dx[p.d],y+dy[p.d]
        # 만약 이동한 방향에 플레이어가 없다면 해당 칸에 총이 있는지 확인합니다.
        if b[nx1][ny1]==0:
            # 총이 있는 경우, 해당 플레이어는 총을 획득합니다.
            if len(a[nx1][ny1])>0:
                get(p,nx1,ny1)
            p.x,p.y=nx1,ny1
            b[nx1][ny1]=p
        # 만약 이동한 방향에 플레이어가 있는 경우에는 두 플레이어가 싸우게 됩니다.
        else:
            winner,loser=fight(p,b[nx1][ny1])
            # 진 플레이어는 본인이 가지고 있는 총을 해당 격자에 내려놓고, 해당 플레이어가 원래 가지고 있던 방향대로 한 칸 이동합니다.
            if loser.g!=0:
                a[nx1][ny1].append(loser.g)
            loser.g=0
            nx2,ny2=0,0
            # 만약 이동하려는 칸에 다른 플레이어가 있거나 격자 범위 밖인 경우에는 오른쪽으로 90도씩 회전하여 빈 칸이 보이는 순간 이동합니다.
            for k in range(4):
                nx2, ny2 = nx1 + dx[loser.d], ny1 + dy[loser.d]
                if not inBoard(nx2, ny2) or b[nx2][ny2] != 0:
                    loser.d = (loser.d + 1)%4
                else:
                    break
            loser.x,loser.y=nx2,ny2
            b[nx2][ny2]=loser
            # 만약 해당 칸에 총이 있다면, 해당 플레이어는 가장 공격력이 높은 총을 획득하고 나머지 총들은 해당 격자에 내려 놓습니다.
            if len(a[nx2][ny2])>0:
                get(loser,nx2,ny2)
            # 이긴 플레이어는 승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려 놓습니다.
            if len(a[nx1][ny1]) > 0:
                get(winner,nx1,ny1)
            winner.x,winner.y=nx1,ny1
            b[nx1][ny1]=winner

print(*ans)