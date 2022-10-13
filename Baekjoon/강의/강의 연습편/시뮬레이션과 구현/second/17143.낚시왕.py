import sys
input=sys.stdin.readline

class Fish:
    def __init__(self,speed=0,direction=0,size=0):
        self.speed=speed
        self.direction=direction
        self.size=size
#  상,하,우,좌
dx=[-1,1,0,0]
dy=[0,0,1,-1]
n,m,k=map(int,input().split())
fish=[[Fish() for _ in range(m)] for _ in range(n)]
nfish=[[Fish() for _ in range(m)] for _ in range(n)]
ans=0

for _ in range(k):
    r,c,speed,direction,size=map(int,input().split())
    r-=1
    c-=1
    direction-=1
    fish[r][c]=Fish(speed,direction,size)

def change_direction(d):
    if d==0:return 1
    elif d==1: return 0
    elif d==2: return 3
    else: return 2

# 1
for j in range(m):
    # 2
    for i in range(n):
        if fish[i][j].size!=0:
            ans+=fish[i][j].size
            fish[i][j]=Fish()
            break
    for x in range(n):
        for y in range(m):
            if fish[x][y].size!=0:
                dir=fish[x][y].direction
                nx,ny=0,0
                ex,ey=x,y
                for _ in range(fish[x][y].speed):
                    nx=ex+dx[dir]
                    ny=ey+dy[dir]
                    if not (0<=nx<n and 0<=ny<m):
                        dir=change_direction(dir)
                        nx=ex+dx[dir]
                        ny=ey+dy[dir]
                    ex,ey=nx,ny
                fish[x][y].direction=dir
                if nfish[ex][ey].size==0:
                    nfish[ex][ey]=fish[x][y]
                else:
                    if nfish[ex][ey].size<fish[x][y].size:
                        nfish[ex][ey]=fish[x][y]
    fish=nfish
    nfish = [[Fish() for _ in range(m)] for _ in range(n)]

    # print("time : ",j)
    # for tx in range(n):
    #     for ty in range(m):
    #         print((tx,ty),fish[tx][ty].size)
    # print()

print(ans)