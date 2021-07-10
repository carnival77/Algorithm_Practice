n = int(input())

board = [list(input()) for _ in range(n)]

# 보드에서 모두 같은 색으로 이루어져 있는 가장 긴 행 또는 열을 고르고, 그 개수를 반환한다.
def check(board):
    n = len(board)
    max_cnt = 1
    for x in range(n):
        cnt = 1
        for y in range(1,n):
            # 행 검사
            if board[x][y] == board[x][y-1]:
                cnt += 1
            else:
                cnt=1
            if max_cnt < cnt:
                max_cnt = cnt
        cnt=1
        for y in range(1,n):
            # 열 검사
            if board[y][x] == board[y-1][x]:
                cnt += 1
            else:
                cnt=1
            if max_cnt < cnt:
                max_cnt = cnt
    return max_cnt

answer = 0
# 보드를 모두 순차 탐색. 각 칸에서 오른쪽과 아래쪽을 서로 바꾼다.
for x in range(n):
    for y in range(n):
        # 오른쪽 change
        if y+1 < n:
            board[x][y],board[x][y+1] = board[x][y+1],board[x][y]
            if answer < check(board):
                answer = check(board)
            board[x][y+1],board[x][y] = board[x][y],board[x][y+1]
        if x+1 < n:
            board[x][y],board[x+1][y] = board[x+1][y],board[x][y]
            if answer < check(board):
                answer = check(board)
            board[x+1][y],board[x][y] = board[x][y],board[x+1][y]


print(answer)