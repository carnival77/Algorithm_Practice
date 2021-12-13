from itertools import combinations

board=[]
spaces=[]
qs=[]
n=0

def watch(x,y,direction):
    # 왼쪽
    if direction == 0:
        while y>=0:
            if board[x][y] == 2:
                return True
            y-=1

    # 오른쪽
    if direction == 1:
        while y<n:
            if board[x][y] == 2:
                return True
            y+=1

    # 위쪽
    if direction == 2:
        while x>=0:
            if board[x][y] == 2:
                return True
            x-=1

    # 아래쪽
    if direction == 3:
        while x<n:
            if board[x][y] == 2:
                return True
            x+=1

    # 대각선 오른쪽 아래
    if direction == 4:
        while y<n and x<n:
            if board[x][y] == 2:
                return True
            x+=1
            y+=1

    # 대각선 오른쪽 위
    if direction == 5:
        while y<n and x>=0:
            if board[x][y] == 2:
                return True
            y+=1
            x-=1

    # 대각선 왼쪽 위
    if direction == 6:
        while x>=0 and y>=0:
            if board[x][y] == 2:
                return True
            x-=1
            y-=1

    # 대각선 왼쪽 아래
    if direction == 7:
        while y>=0 and x<n:
            if board[x][y] == 2:
                return True
            y-=1
            x+=1

    return False

def process():

    for x,y in qs:

        for i in range(8):
            if watch(x,y,i):
                return False

    return True

def solution(input):
    global board,spaces,qs,n
    answer = 0

    n=input

    board=[[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            spaces.append((i,j))

    for comb in combinations(spaces,n):

        # Q 설치
        for x,y in comb:
            # Q를 설치했으면 2, 아니면 0
            board[x][y] = 2
            qs.append((x,y))

        if process():
           answer+=1

        # Q 제거
        for x,y in comb:
            board[x][y] = 0
            qs.remove((x,y))

    return answer

input=4

print(solution(input))