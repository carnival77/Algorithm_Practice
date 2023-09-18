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
def go_next(a, where, x, y, nx, ny, index):
    # index 다음부터 맨 윗 말까지만
    for p in a[x][y][index:]:
        a[nx][ny].append(p)
        where[p.no] = (nx, ny,len(a[nx][ny])-1)
    # a[x][y].clear()
    a[x][y]=a[x][y][:index]

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
a = [[[] for j in range(n)] for i in range(n)]
where = [None] * m # 각 말의 위치와 올려놓아져 있는 순서 저장

for no in range(m):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    d -= 1
    a[x][y].append(Piece(no, d))
    # where 에 말의 (위치, 인덱스)를 저장
    where[no] = (x, y,len(a[x][y])-1)

for turn in range(1, 1001):
    # where 에 있는 첫 번째 말부터
    for k in range(m):
        # 해당 말의 위치와 인덱스
        x, y, index= where[k]
        direction = a[x][y][index].direction
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 체스판 내
        if 0 <= nx < n and 0 <= ny < n:  # in
            # 파란 칸
            if board[nx][ny] == 2:
                a[x][y][index].direction = opposite(direction)
        # 체스판 외
        else:
            a[x][y][index].direction = opposite(direction)
        direction = a[x][y][index].direction
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 체스판 내
        if 0 <= nx < n and 0 <= ny < n:  # in
            # 하얀 칸
            if board[nx][ny] == 0:
                go_next(a, where, x, y, nx, ny,index)
            # 빨간 칸
            elif board[nx][ny] == 1:
                a[x][y] = a[x][y][:index]+a[x][y][index:][::-1]
                go_next(a, where, x, y, nx, ny,index)
            # 종료 조건
            if len(a[nx][ny]) >= 4:
                print(turn)
                sys.exit(0)
        else:  # out
            pass
print(-1)