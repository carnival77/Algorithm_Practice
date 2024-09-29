import sys
input=sys.stdin.readline

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

class Wind:
    def __init__(self,x,y,ratio):
        self.x=x
        self.y=y
        self.ratio=ratio

#   하,우,상,좌
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def makeRoute():
    route=[]
    b=[[0]*n for _ in range(n)]
    x = (n - 1) // 2
    y = (n - 1) // 2
    # 가운데 칸 채우기
    b[x][y] = 1

    # 각 레이어는 3~n 범위의 홀수들만큼의 변의 길이를 가진다.
    for size in range(3, n + 1, 2):
        # 다음 레이어로 갈 때 좌로 한 칸
        d=3
        x += dx[d]
        y += dy[d]
        # 값 채우기
        b[x][y] = 1
        route.append((x,y,d))
        # 이번 레이어를 하,우,상,좌 순서로 탐색
        for k in range(4):
            # (size-1)만큼 loop를 돌며 값을 채울 텐데,
            loop = size - 1
            # 첫 번째 방향으로는 (loop-1)만큼 loop를 돈다.
            if k == 0:
                loop -= 1
            # 해당 loop 만큼 이동하며 값을 채운 후 값을 증가시킨다.
            for i in range(loop):
                x += dx[k]
                y += dy[k]
                b[x][y] = 1
                route.append((x,y,k))

    return route

# 시계 방향 90도 회전
def rotate(points):
    res=[]

    for p in points:
        nx=-p.y
        ny=p.x
        res.append(Wind(nx,ny,p.ratio))

    return res

def makeSpread():
    spread=[0]*4
    points=[]
    points.append(Wind(-1,-1,10))
    points.append(Wind(1,-1,10))
    points.append(Wind(-2,0,2))
    points.append(Wind(2,0,2))
    points.append(Wind(-1,0,7))
    points.append(Wind(1,0,7))
    points.append(Wind(-1,1,1))
    points.append(Wind(1,1,1))
    points.append(Wind(0,-2,5))
    points.append(Wind(0,-1,'a'))

    spread[3]=points

    for i in range(3):
        points=rotate(points)
        spread[i]=points

    return spread

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

routes=makeRoute()
spreads=makeSpread()
ans=0

for x,y,d in routes:
    spread=spreads[d]
    o=a[x][y]
    remain = o
    for p in spread:
        nx=x+p.x
        ny=y+p.y
        ratio=p.ratio
        if ratio!='a':
            sand=o*ratio//100
            remain -= sand
            if inBoard(nx,ny):
                a[nx][ny]+=sand
            else:
                ans+=sand
        else:
            if inBoard(nx, ny):
                a[nx][ny]+=remain
            else:
                ans+=remain
    a[x][y]=0

print(ans)