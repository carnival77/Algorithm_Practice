from collections import deque

n,k = map(int,input().split())

board=[]
virus = []
for i in range(n):
    board.append(list(map(int,input().split())))
    for j in range(n):
        if board[i][j] != 0:
            virus.append((board[i][j],0,i,j))

q=deque(sorted(virus))

tg_s,tg_x,tg_y= map(int,input().split())

dy = [0,0,-1,1]
dx = [-1,1,0,0]

while q:
    virus,s,x,y = q.popleft()

    if s == tg_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >=0 and nx <= (n-1) and ny <= (n-1):
            if board[nx][ny] == 0:
                board[nx][ny] = virus
                q.append((board[nx][ny],(s+1),nx,ny))

print(board[tg_x-1][tg_y-1])