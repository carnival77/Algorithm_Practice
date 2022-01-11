dx = [0,0,1,-1]
dy = [1,-1,0,0]
LIMIT = 10
class Result:
    def __init__(self, moved, hole, x, y):
        self.moved = moved
        self.hole = hole
        self.x = x
        self.y = y

def gen(k):
    a = [0]*LIMIT
    for i in range(LIMIT):
        a[i] = (k&3)
        k >>= 2
    return a
def simulate(a, k, x, y):
    n = len(a)
    m = len(a[0])
    if a[x][y] == '.':
        return Result(False, False, x, y)
    moved = False
    while True:
        nx, ny = x+dx[k], y+dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return Result(moved, False, x, y)
        ch = a[nx][ny]
        if ch == '#':
            return Result(moved, False, x, y)
        elif ch in 'RB':
            return Result(moved, False, x, y)
        elif ch == '.':
            a[x][y],a[nx][ny] = a[nx][ny],a[x][y]
            x,y = nx,ny
            moved = True
        elif ch == 'O':
            a[x][y] = '.'
            moved = True
            return Result(moved, True, x, y)

def check(a, dirs):
    n = len(a)
    m = len(a[0])
    hx,hy = 0,0
    rx,ry = 0,0
    bx,by = 0,0

    for i in range(n):
        for j in range(m):
            if a[i][j] == 'O':
                hx,hy = i,j
            elif a[i][j] == 'R':
                rx,ry = i,j
            elif a[i][j] == 'B':
                bx,by = i,j

    cnt = 0
    for k in dirs:
        cnt += 1
        hole1 = hole2 = False
        while True:
            p1 = simulate(a, k, rx, ry)
            rx,ry = p1.x, p1.y
            p2 = simulate(a, k, bx, by)
            bx,by = p2.x, p2.y

            if not p1.moved and not p2.moved:
                break
            if p1.hole:
                hole1 = True
            if p2.hole:
                hole2 = True

        if hole2:
            return -1
        if hole1:
            return cnt

    return -1

def valid(dirs):
    l = len(dirs)
    for i in range(l-1):
        if dirs[i] == 0 and dirs[i+1] == 1:
            return False
        if dirs[i] == 1 and dirs[i+1] == 0:
            return False
        if dirs[i] == 2 and dirs[i+1] == 3:
            return False
        if dirs[i] == 3 and dirs[i+1] == 2:
            return False
        if dirs[i] == dirs[i+1]:
            return False
    return True

n,m = map(int,input().split())
original = [input() for _ in range(n)]
ans = -1
for k in range(1<<(LIMIT*2)):
    dirs = gen(k)
    if not valid(dirs):
        continue
    a = [list(row) for row in original]
    cur = check(a, dirs)
    if cur == -1:
        continue
    if ans == -1 or ans > cur:
        ans = cur

print(ans)
