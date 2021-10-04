from itertools import combinations
from collections import deque

n,m = map(int,input().split())
board=[]
for i in range(n):
    board.append(map(int,input().split()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

zeros=[]
twos=[]

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            zeros.append((i,j))
        elif board[i][j] == 2:
            twos.append((i,j))

subs = combinations(zeros,3)

ans=0

def bfs(board,check):
    q = deque()
    x,y=0,0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                x,y = i,j
                break
        break
    q.append((x,y))
    check[x][y] = True
    while q:
        x,y = q.popleft()
        for dir in range(4):
            nx,ny = x+dx[dir],y+dy[dir]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny] == 0 and check[x][y] == False:
                    q.append((nx,ny))
                    check[nx][ny] = True

def dfs(board,x,y):


def safe(board,n,m,twos):
    for two in twos:
        x,y = two
        dfs(board,x,y)

for sub in subs:
    check = [[False] * m for _ in range(n)]
    x1,y1,x2,y2,x3,y3=sub
    board[x1][y1] = 1
    board[x2][y2] = 1
    board[x3][y3] = 1
    bfs(board,check)
    safe(board,n,m,twos)