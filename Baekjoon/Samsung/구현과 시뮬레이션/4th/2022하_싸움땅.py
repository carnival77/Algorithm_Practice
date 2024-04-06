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
    if p1.s + p1.g > p2.s + p2.g:
        winner = p1
        loser = p2
    elif p1.s + p1.g < p2.s + p2.g:
        winner = p2
        loser = p1
    else:
        if p1.s > p2.s:
            winner = p1
            loser = p2
        else:
            winner = p2
            loser = p1
    winner.p += (winner.s + winner.g) - (loser.s + loser.g)

    return [winner, loser]

def lose(p):
    x, y, d = p.x, p.y, p.d
    if p.g!=0:
        drop(p, x, y)
    nx, ny = x + dx[d], y + dy[d]
    while True:
        if inBoard(nx, ny) and len(b[nx][ny]) == 0:
            break
        d = changeDirection(d)
        nx, ny = x + dx[d], y + dy[d]
    p.d = d
    move(p, x, y, nx, ny)
    if len(a[p.x][p.y]) > 0:
        get(p, p.x, p.y)

def win(p):
    drop(p, p.x, p.y)
    get(p, p.x, p.y)

for round in range(1, K + 1):
    # 전체 과정
    for p in ps[1:]:
        x, y, d = p.x, p.y, p.d
        nx, ny = x + dx[d], y + dy[d]
        if not inBoard(nx, ny):
            d = (d+2)%4
            nx, ny = x + dx[d], y + dy[d]
            p.d = d
        move(p, x, y, nx, ny)
        if len(b[p.x][p.y]) == 1:
            # move(p, x, y, nx, ny)
            if len(a[p.x][p.y]) > 0:
                if p.g != 0:
                    drop(p, p.x, p.y)
                get(p, p.x, p.y)
        else:
            winner, loser = fight(ps[b[p.x][p.y][0]], ps[b[p.x][p.y][1]])
            lose(loser)
            win(winner)

answer = []
for p in ps[1:]:
    answer.append(p.p)
print(*answer)