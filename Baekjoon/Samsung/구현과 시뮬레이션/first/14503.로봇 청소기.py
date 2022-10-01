# 피드백
# 1. 종료 조건의 경우의 수를 늘 먼저 쓰고, 그 나머지 경우에 프로세스를 전개하자.

n,m = map(int,input().split())

r,c,dir = map(int,input().split())

board=[]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(n):
    board.append(list(map(int,input().split())))

x,y = r,c

while True:
    #1
    if board[x][y] == 0:
        board[x][y]=2
    #2
    #c
    if board[x+1][y] !=0 and board[x-1][y] != 0 and board[x][y+1] != 0 and board[x][y-1] != 0:
        nx,ny=x-dx[dir],y-dy[dir]
        #d
        if board[nx][ny] == 1:
            break
        #방향 유지하며 후진
        else:
            x,y=nx,ny
    else:
        #a
        #왼쪽 방향 회전
        ndir = (dir+3) %4
        #회전한 방향 전방 칸
        nx,ny=x+dx[ndir],y+dy[ndir]
        #아직 청소 X
        if board[nx][ny] == 0:
            #회전
            dir=ndir
            #이동
            x, y = nx, ny
        #b
        else:
            dir=ndir
ans=0
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            ans = ans+1
print(ans)