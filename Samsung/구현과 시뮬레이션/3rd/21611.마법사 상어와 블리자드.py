n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] # 맵
b=[] # 구슬 배열
ax=ay=n//2
a[ax][ay]=4 # 상어 칸
route=[] # 구슬 경로

# 구슬 파괴 방향
#  상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 구슬 파악 방향
#   하,우,상,좌
dx1=[1,0,-1,0]
dy1=[0,1,0,-1]

ans=[0]*4

def getRoute():

    route=[]
    x=y=n//2
    for size in range(3,n+1,2):
        d=3
        x+=dx1[d]
        y+=dy1[d]
        route.append([x,y])
        for d in range(4):
            loop=size-1
            if d==0:
                loop-=1
            for i in range(loop):
                x+=dx1[d]
                y+=dy1[d]
                route.append([x,y])

    return route

def init():
    global b,route

    route=getRoute()

    for x,y in route:
        b.append(a[x][y])

# 상어는 di 방향으로 거리가 si 이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴한다.
# 구슬이 파괴되면 그 칸은 구슬이 들어있지 않은 빈 칸이 된다.
def destroy(d,s):
    global a

    x,y=ax,ay
    for i in range(1,s+1):
        nx,ny=x+dx[d]*i,y+dy[d]*i
        a[nx][ny]=0

def arrToMap():
    global a

    a=[[0]*n for _ in range(n)]
    a[ax][ay] = 4  # 상어 칸
    for i in range(len(b)):
        x,y=route[i]
        a[x][y]=b[i]

# 만약 어떤 칸 A의 번호보다 번호가 하나 작은 칸이 빈 칸이면, A에 있는 구슬은 그 빈 칸으로 이동한다.
# 이 이동은 더 이상 구슬이 이동하지 않을 때까지 반복된다.
def move():
    global a,b

    c=[]
    for x,y in route:
        if a[x][y]!=0:
            c.append(a[x][y])
    b=c

    arrToMap()

# 폭발하는 구슬은 4개 이상 연속하는 구슬이 있을 때 발생한다.
def explode():
    global a,b,ans

    ok=False
    for i in range(len(b)-1):
        x,y=route[i]
        num=a[x][y]
        if a[x][y]==0: continue
        cnt=1
        if b[i]==b[i+1]:
            cnt+=1
            j=i+2
            while j<len(b):
                if b[i]==b[j]:
                    cnt+=1
                else:
                    break
                j+=1
            if cnt>=4:
                ok=True
                for k in range(cnt):
                    x,y=route[i+k]
                    a[x][y]=0
                ans[num]+=cnt

    return ok

# 하나의 그룹은 두 개의 구슬 A와 B로 변한다.
# 구슬 A의 번호는 그룹에 들어있는 구슬의 개수이고, B는 그룹을 이루고 있는 구슬의 번호이다.
# 구슬은 다시 그룹의 순서대로 1번 칸부터 차례대로 A, B의 순서로 칸에 들어간다.
# 만약, 구슬이 칸의 수보다 많아 칸에 들어가지 못하는 경우 그러한 구슬은 사라진다.
def change():
    global a,b

    c=[]
    i=0
    while i<len(b):
        x,y=route[i]
        num=a[x][y]
        cnt=1
        if i<len(b)-1 and b[i]==b[i+1]:
            cnt+=1
            j=i+2
            while j<len(b):
                if b[i]==b[j]:
                    cnt+=1
                else:
                    break
                j+=1
        c.append(cnt)
        c.append(num)
        i+=cnt

    if len(c)>n*n-1:
        c=c[:n*n-1]
    b=c

    arrToMap()

# 초기 구슬 배열 파악
init()

for _ in range(1,m+1):
    d,s=map(int,input().split())
    d-=1

    # 구슬 파괴
    destroy(d,s)
    # 구슬 이동
    move()
    # 구슬 폭발
    # 구슬이 이동한 후에는 다시 구슬이 폭발하는 단계이고, 이 과정은 더 이상 폭발하는 구슬이 없을때까지 반복된다
    while explode():
        # 구슬 이동. 구슬이 폭발해 빈 칸이 생겼으니 다시 구슬이 이동한다
        move()
    # 구슬 변화
    change()

print(ans[1]+ans[2]*2+ans[3]*3)