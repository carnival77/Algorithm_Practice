dx = [0,0,1,-1]
dy = [1,-1,0,0]
LIMIT = 10
class Result:
    def __init__(self, moved, hole, x, y):
        self.moved = moved
        self.hole = hole
        self.x = x
        self.y = y

# 비트 연산 사용하여 정수 k를 (2진법으로 나타난 후) 4진법으로 변환하여 반환
def gen(k):
    a = [0]*LIMIT
    for i in range(LIMIT):
        a[i] = (k&3)
        k >>= 2
    return a

# simulate = 보드 a에서 k 방향으로 R 혹은 B 구슬을 이동 시킴
# 반환값 : 1. 이동했는가? 2. 구멍에 빠졌는가?
def simulate(a, k, x, y):
    n = len(a)
    m = len(a[0])
    if a[x][y] == '.': # 이미 구슬이 구멍에 빠졌다는 것을 표현하기 위해 구멍이었던 칸을 빈 칸으로 바꾼 결과. 이것일 때는 시뮬레이션할 필요가 없기에 return
        return Result(False, False, x, y)
    moved = False
    while True:
        nx, ny = x+dx[k], y+dy[k]
        # 구슬이 범위를 벗어남
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return Result(moved, False, x, y)
        # 이동할 다음 칸이
        ch = a[nx][ny]
        # 벽일 때
        if ch == '#':
            return Result(moved, False, x, y)
        # 구슬일 때
        elif ch in 'RB':
            return Result(moved, False, x, y)
        # 빈 칸일 때
        elif ch == '.':
            a[x][y],a[nx][ny] = a[nx][ny],a[x][y]
            x,y = nx,ny
            moved = True
        # 구멍일 때
        elif ch == 'O':
            a[x][y] = '.' # 이미 구슬이 구멍에 빠졌다는 것을 표현하기 위해 구멍이었던 칸을 빈 칸으로 바꾼다. 그럼 구슬이 들어간 후 다른 구슬이 들어갈 수 없게 된다.
            moved = True
            return Result(moved, True, x, y)

# 보드 a를 그 방향(dirs)으로 이동 시켜서, 빨간 구슬만 구멍에 빠지는 횟수를 반환 받는다.
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

    # cnt = 기울임 횟수
    cnt = 0
    # dirs = 이동시키려는 방향이 순서대로 저장되어 있는 집합
    for k in dirs:
        # k = 이동시키려는 방향
        cnt += 1
        hole1 = hole2 = False
        while True:
            # simulate = 보드 a에서 k 방향으로 R 혹은 B 구슬을 이동 시킴
            p1 = simulate(a, k, rx, ry)
            rx,ry = p1.x, p1.y
            p2 = simulate(a, k, bx, by)
            bx,by = p2.x, p2.y

            # 이동 안 했으면 break
            if not p1.moved and not p2.moved:
                break
            # 구슬이 구멍에 빠졌는가?
            if p1.hole:
                hole1 = True
            if p2.hole:
                hole2 = True

        # 어떤 구슬이 구멍에 빠졌는 지에 따라 다른 값 반환
        if hole2:
            return -1
        if hole1:
            return cnt

    return -1

# 이전과 반대 방향인 경우, 이전과 같은 방향인 경우를 제외
def valid(dirs):
    l = len(dirs)
    for i in range(l-1):
        # 이전과 반대 방향
        if dirs[i] == 0 and dirs[i+1] == 1:
            return False
        if dirs[i] == 1 and dirs[i+1] == 0:
            return False
        if dirs[i] == 2 and dirs[i+1] == 3:
            return False
        if dirs[i] == 3 and dirs[i+1] == 2:
            return False
        # 이전과 같은 방향
        if dirs[i] == dirs[i+1]:
            return False
    return True

n,m = map(int,input().split())
original = [input() for _ in range(n)]
ans = -1

# 모든 이동 방법을 만든다. 여기서 k는 정수(비트마스크)이다.
# 모든 이동 방법의 경우의 수는,  2의 20승이다.
# 하지만 이것은 의미 있는 모든 이동 방법의 수와 다르다.
# 그 이유는, 10번의 각 횟수에 4가지 방향으로 이동하는 방법에서, 첫 번째는 4가지 방향 모두 이동 가능하지만, 그 이후 2번째부터는 이전 방향의 방향과 반대 방향으로 가는 것을 제외해도 무방하기 때문이다.
# 즉, 4 x (2의 9승) 이 의미 있는 모든 이동 방법의 수다.
for k in range(1<<(LIMIT*2)):
    # gen 함수를 통해, 정수 k를 0,1,2,3 으로 이뤄진 4진법 수로 바꾼다. 0,1,2,3은 위,아래,오른쪽,왼쪽 4가지 방향을 가리킨다.
    # 즉, dirs 는 10번 안에 가능한 모든 4가지 방향들의 집합이다.
    dirs = gen(k)
    # valid 함수를 통해 의미 있는 올바른 방법이 아니면 건너 뛴다.
    if not valid(dirs):
        continue
    a = [list(row) for row in original]
    # check 함수로 보드 a를 그 방향(dirs)으로 이동 시켜서, 빨간 구슬만 구멍에 빠지는 횟수를 반환 받는다.
    cur = check(a, dirs)
    # 불가능하면 건너 뛰고
    if cur == -1:
        continue
    # 가능한 결과들 중 최솟값을 얻는다.
    if ans == -1 or ans > cur:
        ans = cur

print(ans)
