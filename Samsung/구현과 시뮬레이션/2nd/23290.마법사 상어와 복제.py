import sys
from itertools import product
input=sys.stdin.readline

n=4
m,s=map(int,input().split())

#  상,좌,하,우 - 상어 이동방향
dx1=[-1,0,1,0]
dy1=[0,-1,0,1]

# 8가지 방향 - 물고기 이동방향
dx2=[0,-1,-1,-1,0,1,1,1]
dy2=[-1,-1,0,1,1,1,0,-1]

a=[[[] for _ in range(n)] for _ in range(n)] # 물고기 맵. 물고기별 방향 저장
c=[[0]*n for _ in range(n)] # 물고기 냄새 맵. 0: 냄새 X, 자연수 : 해당 자연수의 턴에 생긴 냄새
for _ in range(m):
    x,y,d=map(int,input().split())
    x-=1
    y-=1
    d-=1
    a[x][y].append(d)
sx,sy=map(int,input().split())
sx-=1
sy-=1
arr=[0,1,2,3]
ans=0

# 상어가 모든 물고기에게 복제 마법을 시전
def cast():
    global b

    b=[row[:] for row in a]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

# 모든 물고기가 한 칸 이동한다.
# 상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다.
# 각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
# 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다
def fishMove():
    global a

    dx,dy=dx2,dy2

    t=[[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if len(a[x][y])==0: continue
            for d in a[x][y]:
                ok=False
                for i in range(8):
                    nx,ny=x+dx[d],y+dy[d]
                    if not inBoard(nx,ny) or (nx,ny)==(sx,sy) or c[nx][ny]>0:
                        d=(d-1)%8
                    else:
                        ok=True
                        break
                if ok:
                    t[nx][ny].append(d)
                else:
                    t[x][y].append(d)
    a=t

# 상어가 연속해서 3칸 이동한다.
# 상어는 현재 칸에서 상하좌우로 인접한 칸으로 이동할 수 있다.
# 연속해서 이동하는 칸 중에 격자의 범위를 벗어나는 칸이 있으면, 그 방법은 불가능한 이동 방법이다.
# 연속해서 이동하는 중에 상어가 물고기가 있는 같은 칸으로 이동하게 된다면,
# 그 칸에 있는 모든 물고기는 격자에서 제외되며, 제외되는 모든 물고기는 물고기 냄새를 남긴다.
# 가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며, 그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용
def sharkMove(turn):
    global sx,sy,a,c

    dx,dy=dx1,dy1
    cand=[]

    for prod in product(arr,repeat=3):
        t=[row[:] for row in a]
        prod=list(prod)
        ok=True
        cnt=0
        x,y=sx,sy
        for d in prod:
            nx,ny=x+dx[d],y+dy[d]
            if not inBoard(nx,ny):
                ok=False
                break
            else:
                cnt+=len(t[nx][ny])
                t[nx][ny]=[]
            x,y=nx,ny
        if ok:
            cand.append([cnt,prod])

    cand.sort(key=lambda x:(-x[0],x[1]))
    move=cand[0][-1]
    for d in move:
        nx,ny=sx+dx[d],sy+dy[d]
        if len(a[nx][ny])>0:
            a[nx][ny].clear()
            c[nx][ny]=turn
        sx,sy=nx,ny

def remove(turn):
    global c

    for x in range(n):
        for y in range(n):
            if c[x][y]==turn-2:
                c[x][y]=0

def complete():
    global a,b

    for x in range(n):
        for y in range(n):
            if len(b[x][y])>0:
                for d in b[x][y]:
                    a[x][y].append(d)

for turn in range(1,s+1):
    b=[[[] for _ in range(n)] for _ in range(n)] # 복제 마법 시전 후 복제될 물고기 임시 저장
    # 복제 마법 시전
    cast()
    # 물고기 이동
    fishMove()
    # 상어 이동
    sharkMove(turn)
    # 물고기 냄새 제거
    remove(turn)
    # 복제 마법 완료
    complete()

for x in range(n):
    for y in range(n):
        ans+=len(a[x][y])
print(ans)