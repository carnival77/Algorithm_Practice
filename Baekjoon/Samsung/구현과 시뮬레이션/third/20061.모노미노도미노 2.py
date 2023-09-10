import sys
input=sys.stdin.readline

N=int(input())
ans1=0 # 블록을 모두 놓았을 때 얻은 점수
ans2=0 # 파란색 보드와 초록색 보드에서 타일이 들어있는 칸의 개수

n=10
m=4
g=[[0]*m for _ in range(n)]
b=[[0]*n for _ in range(m)]
turn=0

def transpose(a):
    return list(map(list, zip(*a)))

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<m:
        return True
    return False

def check(a,x,y):
    # 가로
    if inBoard(x,y+1) and a[x][y]==a[x][y+1]:
        return 1
    # 가로 중복 탐색은 제외
    elif inBoard(x, y - 1) and a[x][y] == a[x][y - 1]:
        return -1
    # 세로
    elif inBoard(x-1,y) and a[x][y]==a[x-1][y]:
        return 2
    # 한 칸짜리 블록
    else:
        return 3

# 블록의 이동은 다른 블록을 만나거나 보드의 경계를 만나기 전까지 계속해서 이동한다.
def move(a):

    ok=True
    while ok:
        ok=False
        for i in range(n-2,-1,-1):
            # 좌측에서부터 탐색
            for j in range(m):
                # if a[i+1][j]==0 and a[i][j]!=0:
                if a[i+1][j]==0 and a[i][j]==turn:
                    # 어떤 블록인지 확인
                    kind=check(a,i,j)
                    if kind==-1:
                        continue
                    elif kind==1:
                        if a[i+1][j+1]==0:
                            a[i + 1][j], a[i][j] = a[i][j], a[i + 1][j]
                            a[i + 1][j + 1], a[i][j + 1] = a[i][j + 1], a[i + 1][j + 1]
                            ok=True
                    elif kind==2:
                        a[i + 1][j], a[i][j] = a[i][j], a[i + 1][j]
                        a[i - 1][j], a[i][j] = a[i][j], a[i - 1][j]
                        ok=True
                    else:
                        a[i + 1][j], a[i][j] = a[i][j], a[i + 1][j]
                        ok=True

    return a

def moveBoth():
    global g,b

    g=move(g)
    b=transpose(move(transpose(b)))

# 이 게임에서 사용하는 블록은 타일 하나 또는 두 개가 가로 또는 세로로 붙어있는 형태이다.
# 아래와 같이 세 종류가 있으며, 왼쪽부터 순서대로 크기가 1×1, 1×2, 2×1 이다.
# 블록을 놓을 위치를 빨간색 보드에서 선택하면,
# 그 위치부터 초록색 보드로 블록이 이동하고, 파란색 보드로 블록이 이동한다.
def setBlock(t,x,y):
    global g,b

    g[x][y]=turn
    b[x][y]=turn
    if t==2:
        g[x][y+1]=turn
        b[x][y+1]=turn
    elif t==3:
        g[x+1][y]=turn
        b[x+1][y]=turn

    moveBoth()

def check2(a):
    ans=[]

    for i in range(n - 1, 4, -1):
        ok = True
        for j in range(m):
            if a[i][j] == 0:
                ok = False
                break
        if ok:
            ans.append(i)
    if len(ans)>0:
        return ans
    return -1

# 이렇게 초록색 보드에서 어떤 행이 타일로 가득 차 있다면, 그 행의 타일은 모두 사라진다.
# 사라진 이후에는 초록색 보드에서 사라진 행의 위에 있는 블록이 사라진 행의 수만큼 아래로 이동한다.
# 파란색의 경우는 열이 타일로 가득 차 있으면, 그 열의 타일이 모두 사라지며,
# 사라진 이후에는 파란색 보드에서 사라진 열의 왼쪽에 있는 블록이 사라진 열의 수만큼 오른쪽으로 이동한다.
# 이렇게 한 행이나 열이 타일로 가득 차서 사라지면 1점을 획득한다.
# 점수는 사라진 행 또는 열의 수와 같다.
# 만약, 두 개의 행이 사라지면 2점을 획득하게 되고, 한 행과 한 열이 사라져도 2점을 획득하게 된다
def getPoint(a):
    global ans1

    res=check2(a)
    if res!=-1:
        for row in res:
            ans1+=1
            a[row] = [0] * 4
        down=res[0]
        cnt = len(res)
        for _ in range(cnt):
            for i in range(down, 4, -1):
                a[i-1],a[i]=a[i],a[i-1]

    return a

def getPointBoth():
    global g,b

    g=getPoint(g)
    b=transpose(getPoint(transpose(b)))

# 초록색 보드의 0, 1번 행과 파란색 보드의 0, 1번 열은 그림에는 연한색으로 표현되어 있는 특별한 칸이다.
# 초록색 보드의 0, 1번 행에 블록이 있으면, 블록이 있는 행의 수만큼 아래 행에 있는 타일이 사라지고,
# 초록색 보드의 모든 블록이 아래로 경계를 만나기 전까지 이동하고,
# 파란색 보드의 0, 1번 열에 블록이 있으면, 블록이 있는 열의 수만큼 오른쪽 열에 있는 타일이 사라지고,
# 파란색 보드의 모든 블록이 오른쪽으로 경계를 만나기 전까지 이동하게 된다.
def light(a):

    cnt=0
    for x in range(4,6):
        for y in range(m):
            if a[x][y]!=0:
                cnt+=1
                break
    if cnt>0:
        a[6:]=a[6-cnt:n-cnt]
        for k in range(cnt):
            a[5-k]=[0]*4

    return a

def lightBoth():
    global g,b

    g=light(g)
    b=transpose(light(transpose(b)))

def getCount(a):
    ans=0

    for x in range(n):
        for y in range(m):
            if a[x][y]!=0:
                ans+=1

    return ans

def getCountBoth():
    global ans2

    ans2+=getCount(g)
    ans2+=getCount(transpose(b))

for turn in range(1,N+1):
    t,x,y=map(int,input().split())
    # 블록 놓기
    setBlock(t,x,y)
    # 점수 획득
    getPointBoth()
    # 연한 영역 처리
    lightBoth()

getCountBoth()

print(ans1)
print(ans2)