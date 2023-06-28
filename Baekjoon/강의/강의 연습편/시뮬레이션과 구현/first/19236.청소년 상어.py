from copy import deepcopy

n=4
# 상하좌우, 대각선
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

num=[[0] * n for _ in range(n)]
direction=[[0] * n for _ in range(n)]

# 물고기 정보 insert
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(4):
        num[i][j] = row[2*j]
        direction[i][j] = row[2*j+1]
        direction[i][j]-=1

def inBoard(nx,ny):
    if 0<=nx<4 and 0<=ny<4:
        return True
    return False

def dfs(sx,sy,sd,num,direction):

    # 물고기 이동
    for fish in range(1,n*n+1):
        find=False
        for x in range(n):
            for y in range(n):
                if num[x][y]==fish:
                    find=True
                    d=direction[x][y]
                    for _ in range(8):
                        nx,ny=x+dx[d],y+dy[d]
                        if inBoard(nx,ny) and (nx,ny)!=(sx,sy):
                            num[x][y],num[nx][ny]=num[nx][ny],num[x][y]
                            direction[x][y],direction[nx][ny]=direction[nx][ny],direction[x][y]
                            break
                        else:
                            d=(d+1)%8
                            direction[x][y]=d
                if find:
                    break
            if find:
                break

    # 상어 이동
    ans=0

    nx=sx+dx[sd]
    ny=sy+dy[sd]
    while inBoard(nx,ny):
        if num[nx][ny]!=0:
            tmp=num[nx][ny]
            num[nx][ny]=0
            cur=tmp+dfs(nx,ny,direction[nx][ny],deepcopy(num),deepcopy(direction))
            ans=max(ans,cur)
            num[nx][ny]=tmp
        nx+=dx[sd]
        ny+=dy[sd]

    return ans

x,y=0,0
ans=num[x][y]
d=direction[x][y]
num[x][y],direction[x][y]=0,0
ans+=dfs(x,y,d,num,direction)
print(ans)