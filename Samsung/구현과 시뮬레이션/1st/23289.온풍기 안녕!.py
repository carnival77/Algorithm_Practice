n,m,K=map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)] # 온도 맵. # 1 : 오른쪽, 2 : 왼쪽, 3 : 위쪽, 4 : 아래쪽
heater=[] # 온풍기 위치
tg=[] # 조사 대상 칸
for x in range(n):
    for y in range(m):
        if a[x][y]==0:continue
        if 1<=a[x][y]<=4:
            heater.append([x,y,a[x][y]]) # 온풍기 방향 : (1 : 오른쪽, 2 : 왼쪽, 3 : 위쪽, 4 : 아래쪽)
        elif a[x][y]==5:
            tg.append([x,y])
        a[x][y]=0

c=[[[] for _ in range(m)] for _ in range(n)] # 벽 맵. [] : 빈 칸, t가 0인 경우 (x, y)와 (x-1, y) 사이에 벽이 있는 것이고, 1인 경우에는 (x, y)와 (x, y+1) 사이에 벽이 있는 것이다.
w=int(input())
for _ in range(w):
    x,y,t=map(int,input().split())
    x-=1
    y-=1
    c[x][y].append(t)

#   상,우,하,좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]

ans=0 # 초콜릿 개수

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<m:
        return True
    return False

# 일부 칸과 칸 사이에는 벽이 있어 온풍기 바람이 지나갈 수 없다.
# 바람이 오른쪽으로 불었을 때 어떤 칸 (x, y)에서 (x-1, y+1)로 바람이 이동할 수 있으려면,
# (x, y)와 (x-1, y) 사이에 벽이 없어야 하고, (x-1, y)와 (x-1, y+1) 사이에도 벽이 없어야 한다.
# (x, y)에서 (x, y+1)로 바람이 이동할 수 있으려면 (x, y)와 (x, y+1) 사이에 벽이 없어야 한다.
# 마지막으로 (x, y)에서 (x+1, y+1)로 바람이 이동할 수 있으려면, (x, y)와 (x+1, y), (x+1, y)와 (x+1, y+1) 사이에 벽이 없어야 한다.
def checkWall(x,y,dir,kind):
    # 우
    if dir==1:
        if kind==0:
            if 0 in c[x][y] or (inBoard(x-1,y) and 1 in c[x-1][y]):
                return False
        elif kind==1:
            if 1 in c[x][y]:
                return False
        elif kind==2:
            if (inBoard(x+1,y) and 0 in c[x+1][y]) or (inBoard(x+1,y) and 1 in c[x+1][y]):
                return False
    # 좌
    elif dir==2:
        if kind==0:
            if (inBoard(x-1,y-1) and 1 in c[x-1][y-1]) or 0 in c[x][y]:
                return False
        elif kind==1:
            if inBoard(x,y-1) and 1 in c[x][y-1]:
                return False
        elif kind==2:
            if (inBoard(x+1,y) and 0 in c[x+1][y])or (inBoard(x+1,y-1) and 1 in c[x+1][y-1]):
                return False
    # 상
    elif dir==3:
        if kind==0:
            if (inBoard(x,y-1) and 1 in c[x][y-1]) or (inBoard(x,y-1) and 0 in c[x][y-1]):
                return False
        elif kind==1:
            if 0 in c[x][y]:
                return False
        elif kind==2:
            if 1 in c[x][y] or (inBoard(x,y+1) and 0 in c[x][y+1]):
                return False
    # 하
    else:
        if kind==0:
            if (inBoard(x,y-1) and 1 in c[x][y-1]) or (inBoard(x+1,y-1) and 0 in c[x+1][y-1]):
                return False
        elif kind==1:
            if inBoard(x+1,y) and 0 in c[x+1][y]:
                return False
        elif kind==2:
            if (inBoard(x+1,y+1) and 0 in c[x+1][y+1]) or 1 in c[x][y]:
                return False

    return True

def nearBlow(tmp,x,y,dir,kind,num):
    # 우
    if dir==1:
        if kind==0 and inBoard(x-1,y+1):
            tmp[x-1][y+1]=num
        if kind==1 and inBoard(x,y+1):
            tmp[x][y+1]=num
        if kind==2 and inBoard(x+1,y+1):
            tmp[x+1][y+1]=num
    # 좌
    elif dir==2:
        if kind==0 and inBoard(x-1,y-1):
            tmp[x-1][y-1]=num
        if kind==1 and inBoard(x,y-1):
            tmp[x][y-1]=num
        if kind==2 and inBoard(x+1,y-1):
            tmp[x+1][y-1]=num
    # 상
    elif dir==3:
        if kind==0 and inBoard(x-1,y-1):
            tmp[x-1][y-1]=num
        if kind==1 and inBoard(x-1,y):
            tmp[x-1][y]=num
        if kind==2 and inBoard(x-1,y+1):
            tmp[x-1][y+1]=num
    # 하
    else:
        if kind==0 and inBoard(x+1,y-1):
            tmp[x+1][y-1]=num
        if kind==1 and inBoard(x+1,y):
            tmp[x+1][y]=num
        if kind==2 and inBoard(x+1,y+1):
            tmp[x+1][y+1]=num
    return tmp

# 온풍기에서 바람이 한 번 나왔을 때, 온풍기의 바람이 나오는 방향에 있는 칸은 항상 온도가 5도 올라간다.
# 그 다음 이 바람은 계속 다른 칸으로 이동해 다른 칸의 온도를 위의 그림과 같이 상승시키게 된다.
# 어떤 칸 (x, y)에 온풍기 바람이 도착해 온도가 k (> 1)만큼 상승했다면, (x-1, y+1), (x, y+1), (x+1, y+1)의 온도도 k-1만큼 상승하게 된다.
# 이때 그 칸이 존재하지 않는다면, 바람은 이동하지 않는다.
# 온풍기에서 바람이 한 번 나왔을 때,어떤 칸에 같은 온풍기에서 나온 바람이 여러 번 도착한다고 해도 온도는 여러번 상승하지 않는다.
def blow(tmp,x,y,dir):

    if dir==1:
        x,y=x,y+1
    elif dir==2:
        x,y=x,y-1
    elif dir==3:
        x,y=x-1,y
    else:
        x,y=x+1,y

    tmp[x][y]=5

    for i in range(1,5):
        num=5-i
        size=2*i-1
        for j in range(size):
            if 1<=dir<=2:
                nx=x+j
                ny=y
            else:
                nx=x
                ny=y+j
            if not inBoard(nx,ny) or tmp[nx][ny]==0:continue
            for kind in range(3):
                if checkWall(nx,ny,dir,kind):
                    tmp=nearBlow(tmp,nx,ny,dir,kind,num)
        if dir==1:
            x-=1
            y+=1
        elif dir==2:
            x-=1
            y-=1
        elif dir==3:
            x-=1
            y-=1
        else:
            x+=1
            y-=1

    return tmp

def wind():
    global a

    for x,y,dir in heater:
        tmp=[[0]*m for _ in range(n)]
        tmp=blow(tmp,x,y,dir)
        for x in range(n):
            for y in range(m):
                a[x][y]+=tmp[x][y]

# 모든 인접한 칸에 대해서, 온도가 높은 칸에서 낮은 칸으로 ⌊(두 칸의 온도의 차이)/4⌋만큼 온도가 조절된다
# 온도가 높은 칸은 이 값만큼 온도가 감소하고, 낮은 칸은 온도가 상승한다.
# 인접한 두 칸 사이에 벽이 있는 경우에는 온도가 조절되지 않는다.
# 이 과정은 모든 칸에 대해서 동시에 발생한다.
def control():
    global a

    tmp=[[0]*m for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if a[x][y]==0:continue
            for k in range(4):
                if (k == 0 and 0 in c[x][y]) or (k == 1 and 1 in c[x][y]):continue
                nx,ny=x+dx[k],y+dy[k]
                if not inBoard(nx,ny):continue
                if (k==2 and 0 in c[nx][ny]) or (k==3 and 1 in c[nx][ny]):continue
                if a[nx][ny]<a[x][y]:
                    high=a[x][y]
                    low=a[nx][ny]
                    value=(high-low)//4
                    tmp[x][y] -= value
                    tmp[nx][ny]+=value

    for x in range(n):
        for y in range(m):
            a[x][y]+=tmp[x][y]

def decrease():
    global a

    for x in range(n-1):
        if a[x][0]>0:
            a[x][0]-=1
    for y in range(m-1):
        if a[n-1][y]>0:
            a[n-1][y]-=1
    for x in range(n-1,0,-1):
        if a[x][m-1]>0:
            a[x][m-1]-=1
    for y in range(m-1,0,-1):
        if a[0][y]>0:
            a[0][y]-=1

def check():

    for x,y in tg:
        if a[x][y]<K:
            return False
    return True

turn=0
while ans<=100:
    turn+=1
    # 1.바람 나옴
    wind()
    # 2.온도 조절
    control()
    # 3.온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
    decrease()
    # 4.초콜릿 섭취. 먹는 초콜릿의 개수가 100을 넘어가면 101을 출력
    ans+=1
    # 5.조사하는 모든 칸의 온도가 K 이상이 되었는지 검사.
    # 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작
    if check():
        break
print(ans)