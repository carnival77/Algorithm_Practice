import sys
input = sys.stdin.readline

class Piece:
    def __init__(self, no, direction):
        self.no = no
        self.direction = direction


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 방향 반대로
def opposite(direction):
    if direction == 0:
        return 1
    if direction == 1:
        return 0
    if direction == 2:
        return 3
    return 2

# 다음 칸으로 이동
def go_next(a, where, x, y, nx, ny):
    for p in a[x][y]:
        a[nx][ny].append(p)
        where[p.no] = (nx, ny)
    a[x][y].clear()


n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
a = [[[] for j in range(n)] for i in range(n)]
where = [None] * m

for no in range(m):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    d -= 1
    a[x][y].append(Piece(no, d))
    where[no] = (x, y)

for turn in range(1, 1001):
    # where 에 있는 첫 번째 말부터
    for k in range(m):
        # 해당 말의 위치
        x, y = where[k]
        # 해당 말이 맨 아래에 있으면
        if a[x][y][0].no == k:  # bottom
            # 맨 아래 있는 그 말 기준으로
            direction = a[x][y][0].direction
            nx = x + dx[direction]
            ny = y + dy[direction]
            # 체스판 내
            if 0 <= nx < n and 0 <= ny < n:  # in
                # 파란 칸
                if board[nx][ny] == 2:
                    a[x][y][0].direction = opposite(direction)
            # 체스판 외
            else:
                a[x][y][0].direction = opposite(direction)
            direction = a[x][y][0].direction
            nx = x + dx[direction]
            ny = y + dy[direction]

            # 체스판 내
            if 0 <= nx < n and 0 <= ny < n:  # in
                # 하얀 칸
                if board[nx][ny] == 0:
                    go_next(a, where, x, y, nx, ny)
                # 빨간 칸
                elif board[nx][ny] == 1:
                    a[x][y].reverse()
                    go_next(a, where, x, y, nx, ny)
                # 종료 조건
                if len(a[nx][ny]) >= 4:
                    print(turn)
                    sys.exit(0)
            else:  # out
                pass
print(-1)