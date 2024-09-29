import sys
from itertools import product
input=sys.stdin.readline

n=4
m,turn=map(int,input().split())
px,py=map(int,input().split())
px-=1
py-=1
t=0

#   상,좌,하,우
dx1=[-1,0,1,0]
dy1=[0,-1,0,1]

# 8가지 방향
dx2=[-1,-1,0,1,1,1,0,-1]
dy2=[0,-1,-1,-1,0,1,1,1]

a=[[[[0]*8 for j in range(n)] for i in range(n)] for _ in range(26)] # 몬스터 맵. t턴의 (x,y) 에 d 방향 몬스터 수
b=[[[] for _ in range(n)] for _ in range(n)] # 몬스터 시체 맵. 시체가 사라질 각각의 턴을 저장

for _ in range(m):
    x,y,d=map(int,input().split())
    x-=1
    y-=1
    d-=1
    a[0][x][y][d]+=1

# 몬스터는 현재의 위치에서 자신과 같은 방향을 가진 몬스터를 복제
def duplicate():
    global a

    for x in range(n):
        for y in range(n):
            for d in range(8):
                if a[t][x][y][d]==0:
                    continue
                a[t+1][x][y][d]+=a[t][x][y][d]

def canMove(nx,ny):
    if inBoard(nx,ny) and (nx,ny)!=(px,py) and len(b[nx][ny])==0:
        return True
    # 이때 움직이려는 칸에 몬스터 시체가 있거나, 팩맨이 있는 경우거나 격자를 벗어나는 방향일 경우
    return False

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

# 몬스터는 현재 자신이 가진 방향대로 한 칸 이동합니다.
# 이때 움직이려는 칸에 몬스터 시체가 있거나, 팩맨이 있는 경우거나 격자를 벗어나는 방향일 경우에는
# 반시계 방향으로 45도를 회전한 뒤 해당 방향으로 갈 수 있는지 판단합니다.
# 만약 갈 수 없다면, 가능할 때까지 반시계 방향으로 45도씩 회전하며 해당 방향으로 갈 수 있는지를 확인합니다.
# 만약 8 방향을 다 돌았는데도 불구하고, 모두 움직일 수 없었다면 해당 몬스터는 움직이지 않습니다.
def monsterMove():
    global a

    tmp=[[[0]*8 for j in range(n)] for i in range(n)]
    for x in range(n):
        for y in range(n):
            for d in range(8):
                if a[t][x][y][d]==0:continue
                # 몬스터는 현재 자신이 가진 방향대로 한 칸 이동합니다.
                nx,ny=x+dx2[d],y+dy2[d]
                nd=d
                ok=False # 이동할 수 있는지
                # 이때 움직이려는 칸에 몬스터 시체가 있거나, 팩맨이 있는 경우거나 격자를 벗어나는 방향일 경우에는
                # 반시계 방향으로 45도를 회전한 뒤 해당 방향으로 갈 수 있는지 판단합니다.
                # 만약 갈 수 없다면, 가능할 때까지 반시계 방향으로 45도씩 회전하며 해당 방향으로 갈 수 있는지를 확인합니다.
                if canMove(nx,ny):
                    ok=True
                else:
                    for _ in range(7):
                        nd = (nd + 1) % 8
                        nx, ny = x + dx2[nd], y + dy2[nd]
                        if canMove(nx,ny):
                            ok=True
                            break
                # 몬스터는 현재 자신이 가진 방향대로 한 칸 이동합니다.
                if ok:
                    tmp[nx][ny][nd]+=a[t][x][y][d]
                # 만약 8 방향을 다 돌았는데도 불구하고, 모두 움직일 수 없었다면 해당 몬스터는 움직이지 않습니다.
                else:
                    tmp[x][y][d]+=a[t][x][y][d]
    a[t]=tmp

def copyBoard(a):
    tmp=[[[[0]*8 for j in range(n)] for i in range(n)] for _ in range(26)]

    for x in range(n):
        for y in range(n):
            for d in range(8):
                if a[t][x][y][d]==0:continue
                tmp[t][x][y][d]=a[t][x][y][d]

    return tmp

# 팩맨의 이동은 총 3칸을 이동하게 되는데, 각 이동마다 상하좌우의 선택지를 가지게 됩니다.
# 총 4가지의 방향을 3칸 이동하기 때문에 총 64개의 이동 방법이 존재하는데,
# 이 중 몬스터를 가장 많이 먹을 수 있는 방향으로 움직이게 됩니다.
# 만약 가장 많이 먹을 수 있는 방향이 여러개라면 상-좌-하-우의 우선순위를 가지며
# 우선순위가 높은 순서대로 배열하면 "상상상 - 상상좌 - 상상하 - 상상우 - 상좌상 - 상좌좌 - 상좌하 - ..."과 같이 나타낼 수 있습니다.
# 이동하는 과정에 격자 바깥을 나가는 경우는 고려하지 않습니다.
# 이때 팩맨은 알은 먹지 않으며, 움직이기 전에 함께 있었던 몬스터도 먹지 않습니다.
# 즉, 이동하는 과정에 있는 몬스터만 먹습니다.
def pacmanMove():
    global px,py,b,a

    cand=[]
    # 팩맨의 이동은 총 3칸을 이동하게 되는데, 각 이동마다 상하좌우의 선택지를 가지게 됩니다.
    for prod in product([0,1,2,3],repeat=3):
        tmp = copyBoard(a)
        x, y = px, py
        cnt=0
        ok=True # 이번 이동조합이 격자 내에서 이루어지는지
        for dir in prod:
            nx,ny=x+dx1[dir],y+dy1[dir]
            # 이동하는 과정에 격자 바깥을 나가는 경우는 고려하지 않습니다.
            if not inBoard(nx,ny):
                ok=False
                break
            for d in range(8):
                if tmp[t][nx][ny][d]!=0:
                    cnt+=tmp[t][nx][ny][d]
                    tmp[t][nx][ny][d]=0
            x,y=nx,ny
        if ok:
            cand.append([cnt,prod])

    if len(cand)==0:
        return
    # 이 중 몬스터를 가장 많이 먹을 수 있는 방향으로 움직이게 됩니다.
    cand.sort(key=lambda x:(-x[0],x[1]))
    prod=cand[0][1]
    for dir in prod:
        nx,ny=px+dx1[dir],py+dy1[dir]
        for d in range(8):
            if a[t][nx][ny][d]!=0:
                a[t][nx][ny][d]=0
                # 시체가 사라질 턴 추가
                if t not in b[nx][ny]:
                    b[nx][ny].append(t)
        px,py=nx,ny

# 몬스터의 시체는 총 2턴동안만 유지됩니다.
# 즉, 시체가 생기고 나면 시체가 소멸되기 까지는 총 두 턴을 필요로 합니다.
def remove():
    global b

    for x in range(n):
        for y in range(n):
            if len(b[x][y])==0:continue
            if t-2 in b[x][y]:
                b[x][y].remove(t-2)

def add():
    global a

    for x in range(n):
        for y in range(n):
            for d in range(8):
                if a[t][x][y][d]==0:continue
                a[t+1][x][y][d]+=a[t][x][y][d]

for t in range(turn):
    # 몬스터 복제 시도
    duplicate()
    # 몬스터 이동
    monsterMove()
    # 팩맨 이동
    pacmanMove()
    # 몬스터 시체 소멸
    remove()
    # 이번 턴 생존 몬스터 다음 턴에도 추가
    add()

ans=0
for x in range(n):
    for y in range(n):
        for d in range(8):
            if a[turn][x][y][d]==0:continue
            ans+=a[turn][x][y][d]

print(ans)