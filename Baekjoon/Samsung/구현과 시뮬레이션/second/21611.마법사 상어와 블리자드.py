import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] # 구슬 맵
ans=[0]*4

#  상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def getRoutes():
    #  하,우,상,좌
    dx1 = [1, 0, -1, 0]
    dy1 = [0, 1, 0, -1]

    routes=[]
    x,y=n//2,n//2

    for size in range(3,n+1,2):
        x+=dx1[3]
        y+=dy1[3]
        routes.append([x, y])
        for k in range(4):
            loop = size - 1
            if k==0:
                loop-=1
            for i in range(loop):
                x+=dx1[k]
                y+=dy1[k]
                routes.append([x, y])

    return routes

# 상어는 di 방향으로 거리가 si 이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴한다.
# 구슬이 파괴되면 그 칸은 구슬이 들어있지 않은 빈 칸이 된다
def destroy(d,s):
    global a

    for i in range(1,s+1):
        nx,ny=sx+dx[d]*i,sy+dy[d]*i
        a[nx][ny]=0

# 보드맵으로 배열 만들기
def makeArr():
    global arr

    for x, y in routes:
        if a[x][y]!=0:
            arr.append(a[x][y])

# 배열로 보드맵 만들기
def makeBoard():
    global a

    b=[[0]*n for _ in range(n)]
    
    for route,value in zip(routes,arr):
        x,y=route
        try:
            b[x][y]=value
        except:
            break

    a=b

# 어떤 칸 A의 번호보다 번호가 하나 작은 칸이 빈 칸이면, A에 있는 구슬은 그 빈 칸으로 이동한다.
# 이 이동은 더 이상 구슬이 이동하지 않을 때까지 반복
def move():
    global a,arr

    l=len(arr)
    b=[]
    for i in range(l):
        if arr[i]!=0:
            b.append(arr[i])
    arr=b

    makeBoard()

def search():

    res=[]
    tmp=arr[:]
    tmp.append(0)
    l=len(tmp)
    start=0
    cnt=1
    for i in range(1,l):
        if tmp[start]==tmp[i]:
            cnt+=1
        else:
            if cnt>=4:
                res.append([tmp[start],start,cnt])
            start=i
            cnt=1

    if len(res)==0:
        return None
    else:
        return res

# 폭발하는 구슬은 4개 이상 연속하는 구슬이 있을 때 발생
# 구슬이 폭발해 빈 칸이 생겼으니 다시 구슬이 이동한다.
# 구슬이 이동한 후에는 다시 구슬이 폭발하는 단계이고,
# 이 과정은 더 이상 폭발하는 구슬이 없을때까지 반복
def explode():
    global ans,a,arr

    while True:
        res=search()
        if res==None:
            break
        for no,start,cnt in res:
            for i in range(cnt):
                arr[start+i]=0
            ans[no]+=cnt
        move()

def search2():

    res=[]
    tmp=arr[:]
    tmp.append(0)
    l=len(tmp)
    start=0
    cnt=1
    for i in range(1,l):
        if tmp[start]==tmp[i]:
            cnt+=1
        else:
            res.append([tmp[start],cnt])
            start=i
            cnt=1

    return res

# 연속하는 구슬은 하나의 그룹이라고 한다.
# 하나의 그룹은 두 개의 구슬 A와 B로 변한다.
# 구슬 A의 번호는 그룹에 들어있는 구슬의 개수이고, B는 그룹을 이루고 있는 구슬의 번호이다.
# 구슬은 다시 그룹의 순서대로 1번 칸부터 차례대로 A, B의 순서로 칸에 들어간다.
# 만약, 구슬이 칸의 수보다 많아 칸에 들어가지 못하는 경우 그러한 구슬은 사라진다.
def change():
    global arr

    res=search2()
    b=[]
    for no,cnt in res:
        b.append(cnt)
        b.append(no)
    arr=b[:n*n-1]

    makeBoard()

routes=getRoutes()
sx=sy=n//2

for round in range(1,m+1):
    d,s=map(int,input().split())
    d-=1
    arr = []  # 구슬 배열
    # 파괴
    destroy(d,s)
    makeArr()
    # 이동
    move()
    # 폭발
    explode()
    # 변화
    change()

print(ans[1]+ans[2]*2+ans[3]*3)