import sys
input=sys.stdin.readline

#  하,우,상,좌
dx=[1,0,-1,0]
dy=[0,1,0,-1]

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
ans=0

# 4가지 방향별 바람에 의해 모래 흩날리는 포인트
w=[[-1,-1],[-1,1],[0,-2],[0,2],[0,-1],[0,1],[1,-1],[1,1],[2,0],[1,0]]
wind=[w]
for _ in range(3):
    tmp=[]
    for x,y in w:
        nx=-y
        ny=x
        tmp.append([nx,ny])
    w=tmp
    wind.append(w)

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def scatter(x,y,d):
    global a,ans

    v=a[x][y]
    s=0
    w=wind[d]
    for i in range(10):
        nx, ny = x + w[i][0], y + w[i][1]
        if 0<=i<=8:
            if 0<=i<=1:
                p=1
            elif 2<=i<=3:
                p=2
            elif 4<=i<=5:
                p=7
            elif 6<=i<=7:
                p=10
            elif i==8:
                p=5
            z = v * p // 100
            s += z
        else:
            z=v-s
        if not inBoard(nx,ny):
            ans+=z
        else:
            a[nx][ny]+=z
    a[x][y]=0

    pass

x,y=n//2,n//2
for size in range(3,n+1,2):
    x+=dx[3]
    y+=dy[3]
    scatter(x,y,3)
    for k in range(4):
        loop=size-1
        if k==0:
            loop-=1
        for i in range(loop):
            x+=dx[k]
            y+=dy[k]
            scatter(x,y,k)

print(ans)