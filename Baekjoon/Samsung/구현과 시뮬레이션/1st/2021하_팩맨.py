import sys
from itertools import product
import heapq
input=sys.stdin.readline

n=4
z,turn=map(int,input().split())

dboard=[[[] for _ in range(n)] for _ in range(n)] # 몬스터 시체 보드. 시체가 사라질 각각의 턴을 배열에 담는다.
mboard=[[[[0]*8 for _ in range(n)] for _ in range(n)] for _ in range(26)] # 몬스터 보드. t턴에 (x,y) 위치에서 방향 d를 가진 몬스터 수
md=[[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]] # 몬스터 방향
# 팩맨 방향
#  상,좌,하,우
dx=[-1,0,1,0]
dy=[0,-1,0,1]

r,c=map(int,input().split())
# 팩맨 위치
px,py=r-1,c-1

for _ in range(z):
    x,y,d=map(int,input().split())
    x,y,d=x-1,y-1,d-1
    mboard[0][x][y][d]+=1

def copyBoard(a,t):
    b=[[[[0]*8 for _ in range(n)] for _ in range(n)] for _ in range(25)]
    for x in range(n):
        for y in range(n):
            for d in range(8):
                if a[t][x][y][d]!=0:
                    b[t][x][y][d]=a[t][x][y][d]
    return b

# 몬스터는 현재의 위치에서 자신과 같은 방향을 가진 몬스터를 복제
def duplicateMonster(t):
    global mboard

    for x in range(n):
        for y in range(n):
            for d in range(8):
                if mboard[t][x][y][d]==0:
                    continue
                mboard[t + 1][x][y][d] = mboard[t][x][y][d]

# 격자를 벗어나는 방향일 경우
def inBoard(nx,ny):
    return 0<=nx<n and 0<=ny<n

# 이때 움직이려는 칸에 몬스터 시체가 있거나, 팩맨이 있는 경우거나 격자를 벗어나는 방향일 경우
def canMove(nx,ny):
    if not inBoard(nx,ny) or len(dboard[nx][ny])>0 or (nx,ny)==(px,py):
        return False
    return True

# 몬스터는 현재 자신이 가진 방향대로 한 칸 이동합니다.
# 이때 움직이려는 칸에 몬스터 시체가 있거나, 팩맨이 있는 경우거나 격자를 벗어나는 방향일 경우에는
# 반시계 방향으로 45도를 회전한 뒤 해당 방향으로 갈 수 있는지 판단합니다.
# 만약 갈 수 없다면, 가능할 때까지 반시계 방향으로 45도씩 회전하며 해당 방향으로 갈 수 있는지를 확인합니다.
# 만약 8 방향을 다 돌았는데도 불구하고, 모두 움직일 수 없었다면 해당 몬스터는 움직이지 않습니다.
def moveMonster(t):
    global mboard

    temp = [[[0] * 8 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            for d in range(8):
                if mboard[t][x][y][d]==0:
                    continue
                # 몬스터는 현재 자신이 가진 방향대로 한 칸 이동합니다.
                ok=False # 이동할 수 있는지
                nd=d
                nx,ny=x+md[nd][0],y+md[nd][1]
                # 이때 움직이려는 칸에 몬스터 시체가 있거나, 팩맨이 있는 경우거나 격자를 벗어나는 방향일 경우에는
                # 반시계 방향으로 45도를 회전한 뒤 해당 방향으로 갈 수 있는지 판단합니다.
                # 만약 갈 수 없다면, 가능할 때까지 반시계 방향으로 45도씩 회전하며 해당 방향으로 갈 수 있는지를 확인합니다.
                if not canMove(nx,ny):
                    for _ in range(7):
                        nd=(nd+1)%8
                        nx,ny=x+md[nd][0],y+md[nd][1]
                        if canMove(nx,ny):
                            ok=True
                            break
                else:
                    ok=True
                # 몬스터는 현재 자신이 가진 방향대로 한 칸 이동합니다.
                if ok:
                    temp[nx][ny][nd]+=mboard[t][x][y][d]
                # 만약 8 방향을 다 돌았는데도 불구하고, 모두 움직일 수 없었다면 해당 몬스터는 움직이지 않습니다.
                else:
                    temp[x][y][d]+=mboard[t][x][y][d]
    mboard[t]=temp

# 팩맨의 이동은 총 3칸을 이동하게 되는데, 각 이동마다 상하좌우의 선택지를 가지게 됩니다.
# 총 4가지의 방향을 3칸 이동하기 때문에 총 64개의 이동 방법이 존재하는데,
# 이 중 몬스터를 가장 많이 먹을 수 있는 방향으로 움직이게 됩니다.
# 만약 가장 많이 먹을 수 있는 방향이 여러개라면 상-좌-하-우의 우선순위를 가지며
# 우선순위가 높은 순서대로 배열하면 "상상상 - 상상좌 - 상상하 - 상상우 - 상좌상 - 상좌좌 - 상좌하 - ..."과 같이 나타낼 수 있습니다.
# 이동하는 과정에 격자 바깥을 나가는 경우는 고려하지 않습니다.
# 이때 팩맨은 알은 먹지 않으며, 움직이기 전에 함께 있었던 몬스터도 먹지 않습니다.
# 즉, 이동하는 과정에 있는 몬스터만 먹습니다.
def movePacman(px,py,t):
    global mboard,dboard

    cand=[]
    max_cnt=0
    # 팩맨의 이동은 총 3칸을 이동하게 되는데, 각 이동마다 상하좌우의 선택지를 가지게 됩니다.
    for prod in product([0,1,2,3],repeat=3):
        temp = copyBoard(mboard,t)
        ok = True # 이번 이동조합이 격자 내에서 이루어지는지
        x,y=px,py
        cnt=0
        prod=list(prod)
        for dir in prod:
            nx,ny=x+dx[dir],y+dy[dir]
            # 이동하는 과정에 격자 바깥을 나가는 경우는 고려하지 않습니다.
            if not inBoard(nx,ny):
                ok=False
                break
            for d in range(8):
                if temp[t][nx][ny][d]==0:
                    continue
                cnt+=temp[t][nx][ny][d]
                temp[t][nx][ny][d]=0
            x,y=nx,ny
        # 이번 이동조합이 격자 내에서 이루어지지 않으면 다음 이동조합으로
        if not ok:
            continue
        # 이 중 몬스터를 가장 많이 먹을 수 있는 방향으로 움직이게 됩니다.
        if cnt>=max_cnt:
            max_cnt=cnt
            cand.append([-cnt,prod])
    heapq.heapify(cand)
    moves=heapq.heappop(cand)[1] # 이동조합
    for pd in moves:
        nx,ny=px+dx[pd],py+dy[pd]
        for d in range(8):
            if mboard[t][nx][ny][d]==0:
                continue
            # 즉, 이동하는 과정에 있는 몬스터만 먹습니다.
            mboard[t][nx][ny][d]=0
            # 시체가 사라질 턴 추가
            if t not in dboard[nx][ny]:
                dboard[nx][ny].append(t)
        px,py=nx,ny
    return [px,py]

# 몬스터의 시체는 총 2턴동안만 유지됩니다.
# 즉, 시체가 생기고 나면 시체가 소멸되기 까지는 총 두 턴을 필요로 합니다.
def removeDead(t):
    global dboard

    for x in range(n):
        for y in range(n):
            if t-2 in dboard[x][y]:
                dboard[x][y].remove(t-2)

def addMonster(t):
    global mboard

    for x in range(n):
        for y in range(n):
            for d in range(8):
                if mboard[t][x][y][d]==0:
                    continue
                mboard[t+1][x][y][d]+=mboard[t][x][y][d]

# t는 0부터 시작. 턴은 (1<=turn<=25)이므로, 매 턴의 한 턴 전에 프로세스들이 진행된 후 매 턴의 초기 상태에 해당 턴의 몬스터가 표시됨.
for t in range(turn):
    # 1. 몬스터 복제 - 다음 턴에 적용
    duplicateMonster(t)
    # 2. 몬스터 이동
    moveMonster(t)
    # 3. 팩맨 이동
    px,py=movePacman(px,py,t)
    # 4. 몬스터 시체 소멸
    removeDead(t)
    # 이번 턴에 남은 몬스터 다음 턴으로 이동
    addMonster(t)

# t개의 턴이 지난 이후 격자에 살아남은 몬스터는 총 몇 마리인지 출력
ans=0
for x in range(n):
    for y in range(n):
        for d in range(8):
            if mboard[turn][x][y][d]==0:
                continue
            ans+=mboard[turn][x][y][d]

print(ans)