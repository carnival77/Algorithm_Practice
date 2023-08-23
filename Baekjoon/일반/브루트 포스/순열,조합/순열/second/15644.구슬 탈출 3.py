import sys
from itertools import product
input=sys.stdin.readline

n,m=map(int,input().split())
# '.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다.
# 'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.
# 입력되는 모든 보드의 가장자리에는 모두 '#'이 있다.
# 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.
a=[list(input().strip()) for _ in range(n)]

#  우,하,좌,상
dx=[0,1,0,-1]
dy=[1,0,-1,0]
l=10

rx,ry=0,0 # 빨간 구슬 위치
bx,by=0,0 # 파란 구슬 위치

for i in range(n):
    for j in range(m):
        if a[i][j]=='R':
            rx,ry=i,j
        elif a[i][j]=='B':
            bx,by=i,j

def valid(arr):
    for i in range(9):
        if arr[i] == arr[i + 1]:
            return False
        if arr[i]%2 == arr[i+1]%2:
            return False
    return True

# 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.
def gen():

    res=[]
    arr=[0,1,2,3]
    for prod in product(arr,repeat=l):
        prod=list(prod)
        if valid(prod):
            res.append(prod)

    return res

cand=gen()

def change(d):
    if d==0: return 'R'
    elif d==1: return 'D'
    elif d==2: return 'L'
    else: return 'U'

def inBoard(nx,ny):
    if 0<nx<n-1 and 0<ny<m-1:
        return True
    return False

# 구슬 이동.
# 다른 구슬 때문에 더 이상 이동 못하는 경우는 이동 실패.
# 나머지 경우는 이동 성공
def move(d,a,x,y,self,other):

    moved=False # 이동 성공 여부
    inhole=False # 구멍 빠짐
    a[x][y]='.'

    while True:
        nx,ny=x+dx[d],y+dy[d]
        # 다음 칸이 범위 밖인 경우
        if not inBoard(nx,ny):
            moved=True
            break
        # 다음 칸이 벽인 경우
        if a[nx][ny]=='#':
            moved=True
            break
        # 다음 칸이 다른 구슬인 경우
        elif a[nx][ny]==other:
            # 그 다음 칸이
            nx1=nx+dx[d]
            ny1=ny+dy[d]
            # 벽인 경우
            if a[nx1][ny1]=='#':
                moved = True
                break
            # 벽이 아닌 경우
            else:
                break
        # 다음 칸이 구멍인 경우
        elif a[nx][ny]=='O':
            inhole=True
            moved=True
            break
        # 다음 칸이 빈 칸인 경우
        else:
            x,y=nx,ny # 이동

    # 구슬 위치 맵에 표시
    a[x][y]=self
    # 구멍에 빠졌을 경우 맵에서 구슬 삭제
    if inhole:
        a[x][y]='.'
        # x,y=0,0

    return [a,inhole,moved,x,y]

# 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.
# 각각의 동작에서 공은 동시에 움직인다.
# 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다.
# 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다.
# 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.
# 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다.
# 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.
# 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지, 또 어떻게 기울여야 하는지
def process(a,prod,rx,ry,bx,by):

    cnt=0
    route=[]
    success=False

    b=[row[:] for row in a]

    for d in prod:
        # 어떻게 기울여야 하는지 순서대로 출력한다.
        # 왼쪽으로 기울이기는 'L', 오른쪽으로 기울이기는 'R', 위로 기울이기는 'U', 아래로 기울이기는 'D'로 출력하며, 공백없이 한 줄에 모두 출력한다.
        # 가능한 방법이 여러 가지면, 아무거나 출력
        route.append(change(d))
        cnt+=1
        while True:
            b,inhole1,moved1,rx,ry=move(d,b,rx,ry,'R','B') # 빨간 구슬 이동
            b,inhole2,moved2,bx,by=move(d,b,bx,by,'B','R') # 파란 구슬 이동
            if moved1 and moved2:
                break
        if inhole2:
            break
        elif inhole1:
            success=True
            break

    if success:
        return [True,cnt,route]
    else:
        return [False,-1,[]]

result=[]
for prod in cand:
    ok,cnt,route=process(a,prod,rx,ry,bx,by)
    if ok:
        result.append([cnt,route])

if len(result)>0:
    result.sort()
    ans,ans2=result[0]
    print(ans)
    # print(''.join(ans2))
# 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력
else:
    print(-1)