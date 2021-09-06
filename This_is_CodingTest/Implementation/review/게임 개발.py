n,m = map(int,input().split())
x,y,d = map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

ans=0

while(True):
    for dir in range(3,-1,-1):
        d = (dir+d)%4
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if board[nx][ny]== 0 :
                board[nx][ny] = 2
                x,y = nx,ny
                ans+=1
    nx = x - dx[d]
    ny = y - dy[d]
    if board[nx][ny] == 1:
        break
    elif board[nx][ny] == 2 or board[nx][ny] == 0:
        x,y = nx,ny

print(ans)