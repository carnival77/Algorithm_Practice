import sys
from collections import deque
input=sys.stdin.readline

n,m,K=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] # 보드 맵
b=[[0]*n for _ in range(n)] # 기사맵
init_hp=[None] # 초기 기사 HP
hp=[None] # 기사 HP
pos=[None] # 기사 위치
info=[None] # 기사 정보
g=[] # 기사 번호 리스트

#  상,우,하,좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

# 기사 정보 토대로 기사 맵에 각 영역 표시
def adjustGmap(r,c,h,w,no,b):

    for i in range(h):
        for j in range(w):
            b[r+i][c+j]=no

    return b

for no in range(1,m+1):
    r,c,h,w,k=map(int,input().split())
    r-=1
    c-=1
    b=adjustGmap(r,c,h,w,no,b)
    pos.append([r,c])
    info.append([h,w])
    init_hp.append(k)
    hp.append(k)
    g.append(no)

# 해당 기사 영역 내 각 위치에서 d 방향에 인접한 기사 또는 벽을 탐색한다.
# 벽을 발견 시, 이동 불가이므로 이동 후보 리스트는 빈 배열이 되도록 None을 반환한다.
# 기사를 발견 시, 인접 기사 리스트에 넣는다.
def bfs(sx, sy, num, d):

    near=[] # 인접 기사 리스트
    q = deque()
    q.append((sx, sy))
    visit = [[False] * n for _ in range(n)]
    visit[sx][sy] = True

    # 시작점에서 이동할 방향의 칸에 기사가 있을 경우 인접 기사 리스트에 넣는다.
    nx1,ny1=sx+dx[d],sy+dy[d]
    if inBoard(nx1,ny1) and b[nx1][ny1]>0 and b[nx1][ny1]!=num:
        near.append(b[nx1][ny1])

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            # 해당 기사 영역 내 각 위치에서 d 방향에 인접한 기사 또는 벽을 탐색한다.
            if inBoard(nx, ny) and not visit[nx][ny] and b[nx][ny] == num:
                nx1,ny1=nx+dx[d],ny+dy[d]
                if not inBoard(nx1,ny1):continue
                # 벽을 발견 시, 이동 불가이므로 이동 후보 리스트는 빈 배열이 되도록 None을 반환한다.
                if a[nx1][ny1]==2:
                    return None
                # # 기사를 발견 시, 인접 기사 리스트에 넣는다.
                if b[nx1][ny1]>0 and b[nx1][ny1]!=num:
                    near.append(b[nx1][ny1])
                q.append((nx,ny))
                visit[nx][ny]=True

    return near

def canMove(gnum,d):

    x,y=pos[gnum]
    h,w=info[gnum]
    nx,ny=x+dx[d],y+dy[d]

    for i in range(h):
        for j in range(w):
            if not inBoard(nx+i,ny+j) or a[nx+i][ny+j]==2:
                return False
    return True

# 왕에게 명령을 받은 기사는 상하좌우 중 하나로 한 칸 이동할 수 있습니다.
# 이때 만약 이동하려는 위치에 다른 기사가 있다면 그 기사도 함께 연쇄적으로 한 칸 밀려나게 됩니다.
# 그 옆에 또 기사가 있다면 연쇄적으로 한 칸씩 밀리게 됩니다.
# 하지만 만약 기사가 이동하려는 방향의 끝에 벽이 있다면 모든 기사는 이동할 수 없게 됩니다.
def check(num,d):
    global cand

    # 기사 맵에서 기사의 영역 내의 각 위치를 탐색하여 이동할 방향의 인접한 기사의 번호를 얻는다.
    # 이를 명령을 받은 첫 번째 기사부터 시작하여 인접 기사들까지 반복하여 이동 후보 기사 리스트를 만든다.
    # 만약 이 과정에서 이동할 방향에 벽이 발견되면 이동 후보 기사 리스트는 빈 배열로 반환하여 모든 기사가 이동하지 않게 한다.
    sx, sy = pos[num]
    q=deque()
    q.append([sx,sy,num])
    while q:
        x,y,num=q.popleft()
        near=bfs(x,y,num,d)
        # 벽이 발견되면 빈 배열 반환
        if near is None:
            cand=[]
            break
        # 그렇지 않을 경우 인접 기사들을 차례로 큐에 넣어 bfs 탐색할 수 있도록 함
        else:
            for gnum in near:
                cand.append(gnum)
                nx,ny=pos[gnum]
                q.append(([nx,ny,gnum]))
    # 이동 후보 기사 리스트 내 이동할 기사의 영역이 격자 안이며 이동 가능한지 확인
    # 만약 이동 불가할 경우, 모든 기사는 이동 불가
    for gnum in cand:
        if not canMove(gnum, d):
            cand = []
            return

# 명령을 받은 기사가 다른 기사를 밀치게 되면, 밀려난 기사들은 피해를 입게 됩니다.
# 이때 각 기사들은 해당 기사가 이동한 곳에서 w×h 직사각형 내에 놓여 있는 함정의 수만큼만 피해를 입게 됩니다.
# 각 기사마다 피해를 받은 만큼 체력이 깎이게 되며,
# 기사들은 모두 밀린 이후에 대미지를 입게 됩니다.
# 밀렸더라도 밀쳐진 위치에 함정이 전혀 없다면 그 기사는 피해를 전혀 입지 않게 됨에 유의합니다.
def damage(x,y,gnum,h,w):
    global hp

    for i in range(h):
        for j in range(w):
            if a[x+i][y+j]==1:
                if hp[gnum]>0:
                    hp[gnum]-=1

def move(num,d):
    global pos,b

    # 이동 후보 기사인 것은 이동 및 새로운 영역 그리기,
    # 아닌 것은 기존 영역 그대로 유지
    tmp = [[0] * n for _ in range(n)] # 이동 예상 기사 맵
    for gnum in g:
        if hp[gnum]==0:continue # 죽은 기사 제외
        x, y = pos[gnum]
        h, w = info[gnum]
        if gnum not in cand: # 이동 후보 기사 아니면 기존 영역 그대로 유지
            tmp=adjustGmap(x,y, h, w,gnum,tmp)
            continue
        # 이동 후보 기사인 것은 이동 및 새로운 영역 그리기
        nx,ny=x+dx[d],y+dy[d]
        pos[gnum]=[nx,ny]
        tmp=adjustGmap(nx,ny, h, w,gnum,tmp)
        # 단, 명령을 받은 기사는 피해를 입지 않으며,
        if num==gnum:continue
        # 대결 데미지
        damage(nx,ny,gnum,h,w)
    # 이동 결과 기사 맵에 반영
    b=tmp

#  현재 체력 이상의 대미지를 받을 경우 기사는 체스판에서 사라지게 됩니다.
def update():
    global pos,b,info

    for i in range(1,m+1):
        if hp[i]==0:
            if pos[i]==None:continue
            x,y=pos[i]
            h,w=info[i]
            b=adjustGmap(x,y,h,w,0,b)
            pos[i]=None
            info[i]=None

for round in range(1,K+1):
    num,d=map(int,input().split())
    # 기사 생존 여부 체크
    # 또, 체스판에서 사라진 기사에게 명령을 내리면 아무런 반응이 없게 됩니다.
    if hp[num]==0:
        continue
    cand = [num]  # 이번 라운드 이동 후보 기사 리스트
    # 이동 후보 기사 체크
    check(num,d)
    if len(cand)==0:continue # 이동할 기사 없으면 스킵
    # 기사 이동
    move(num,d)
    # 기사 생존 여부 업데이트
    update()

ans=0
for i in range(1,m+1):
    if hp[i]!=0:
        ans+=(init_hp[i]-hp[i])
print(ans)