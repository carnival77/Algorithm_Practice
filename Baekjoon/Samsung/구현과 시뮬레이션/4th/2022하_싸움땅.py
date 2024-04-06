import sys

input = sys.stdin.readline

class Player:
    def __init__(self, no, x, y, d, s, g=0, p=0):
        self.no = no
        self.x = x
        self.y = y
        self.d = d
        self.s = s
        self.g = g
        self.p = p

n, m, K = map(int, input().split())
a = [[[] for _ in range(n)] for _ in range(n)]  # 총 맵
b = [[[] for _ in range(n)] for _ in range(n)]  # 플레이어 맵
ps = [None] * (m + 1)  # 플레이어 리스트

#  상,우,하,좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for x in range(n):
    row = list(map(int, input().split()))
    for y, ele in enumerate(row):
        if ele == 0: continue
        a[x][y].append(ele)

for no in range(1, m + 1):
    x, y, d, s = map(int, input().split())
    x -= 1
    y -= 1
    p = Player(no, x, y, d, s)
    ps[no]=p
    b[x][y].append(no)

def inBoard(nx, ny):
    if 0 <= nx < n and 0 <= ny < n:
        return True
    return False

def changeDirection(d):
    return (d + 1) % 4

def move(p, x, y, nx, ny):
    global b

    p.x, p.y = nx, ny
    b[nx][ny].append(p.no)
    b[x][y].remove(p.no)

def drop(p, x, y):
    global a

    a[x][y].append(p.g)
    p.g = 0

def get(p, x, y):
    global a

    a[x][y].sort(reverse=True)
    p.g = a[x][y][0]
    a[x][y].remove(p.g)

def fight(p1, p2):
    # 해당 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합을 비교하여 더 큰 플레이어가 이기게 됩니다.
    if p1.s + p1.g > p2.s + p2.g:
        winner = p1
        loser = p2
    elif p1.s + p1.g < p2.s + p2.g:
        winner = p2
        loser = p1
    # 만일 이 수치가 같은 경우에는 플레이어의 초기 능력치가 높은 플레이어가 승리하게 됩니다.
    else:
        if p1.s > p2.s:
            winner = p1
            loser = p2
        else:
            winner = p2
            loser = p1
    # 이긴 플레이어는 각 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합의 차이만큼을 포인트로 획득하게 됩니다.
    winner.p += (winner.s + winner.g) - (loser.s + loser.g)

    return [winner, loser]

def lose(p):
    x, y, d = p.x, p.y, p.d
    # 진 플레이어는 본인이 가지고 있는 총을 해당 격자에 내려놓고,
    if p.g!=0:
        drop(p, x, y)
    # 해당 플레이어가 원래 가지고 있던 방향대로 한 칸 이동합니다.
    nx, ny = x + dx[d], y + dy[d]
    # 만약 이동하려는 칸에 다른 플레이어가 있거나 격자 범위 밖인 경우에는 오른쪽으로 90도씩 회전하여 빈 칸이 보이는 순간 이동합니다.
    while True:
        if inBoard(nx, ny) and len(b[nx][ny]) == 0:
            break
        d = changeDirection(d)
        nx, ny = x + dx[d], y + dy[d]
    p.d = d
    move(p, x, y, nx, ny)
    # 만약 해당 칸에 총이 있다면, 해당 플레이어는 가장 공격력이 높은 총을 획득하고 나머지 총들은 해당 격자에 내려 놓습니다.
    if len(a[p.x][p.y]) > 0:
        get(p, p.x, p.y)

def win(p):
    # 이긴 플레이어는 승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득하고,
    # 나머지 총들은 해당 격자에 내려 놓습니다.
    drop(p, p.x, p.y)
    get(p, p.x, p.y)

for round in range(1, K + 1):
    # 전체 과정
    # 첫 번째 플레이어부터 순차적으로 본인이 향하고 있는 방향대로 한 칸만큼 이동합니다.
    for p in ps[1:]:
        x, y, d = p.x, p.y, p.d
        nx, ny = x + dx[d], y + dy[d]
        # 만약 해당 방향으로 나갈 때 격자를 벗어나는 경우에는 정반대 방향으로 방향을 바꾸어서
        if not inBoard(nx, ny):
            d = (d+2)%4
            nx, ny = x + dx[d], y + dy[d]
            p.d = d
        # 1만큼 이동합니다.
        move(p, x, y, nx, ny)
        # 만약 이동한 방향에 플레이어가 없다면
        if len(b[p.x][p.y]) == 1:
            # move(p, x, y, nx, ny)
            # 해당 칸에 총이 있는지 확인합니다.
            if len(a[p.x][p.y]) > 0:
                # 플레이어가 이미 총을 가지고 있는 경우에는 놓여있는 총들과 플레이어가 가지고 있는 총 가운데 공격력이 더 쎈 총을 획득하고, 나머지 총들은 해당 격자에 둡니다.
                if p.g != 0:
                    drop(p, p.x, p.y)
                # 총이 있는 경우, 해당 플레이어는 총을 획득합니다.
                get(p, p.x, p.y)
        # 만약 이동한 방향에 플레이어가 있는 경우에는 두 플레이어가 싸우게 됩니다.
        else:
            winner, loser = fight(ps[b[p.x][p.y][0]], ps[b[p.x][p.y][1]])
            lose(loser)
            win(winner)

answer = []
for p in ps[1:]:
    answer.append(p.p)
print(*answer)