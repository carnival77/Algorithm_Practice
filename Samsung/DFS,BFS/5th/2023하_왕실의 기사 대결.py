# 풀이 시간 : 약 2시간

from collections import deque

n,m,K=map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)] # 주어지는 맵
b=[[0]*n for _ in range(n)] # 기사 맵
init_hp=[None]+[0]*m
hp=[None]+[0]*m
pos=[None]*(m+1)
size=[None]*(m+1)

for no in range(1,m+1):
    x,y,h,w,k=map(int,input().split())
    x-=1
    y-=1
    pos[no]=[x,y]
    size[no]=[h,w]
    init_hp[no]=k
    hp[no]=k

    for i in range(x,x+h):
        for j in range(y,y+w):
            b[i][j]=no

#  상,우,하,좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def process(sno,dir):
    global pos,b,hp

    willMove=set() # 움직일 대상은 중복되지 않음
    tmp=[[0]*n for _ in range(n)]
    q=deque() # 이동 대상 큐
    q.append((sno,dir))

    # 이동 대상 선정
    while q:
        no,dir=q.popleft() # 이번 기사의
        willMove.add(no)
        sx,sy=pos[no]
        h,w=size[no]

        nx,ny=sx+dx[dir],sy+dy[dir] # 이동할 칸 기준으로
        # 기사의 영역이
        for x in range(nx,nx+h):
            for y in range(ny,ny+w):
                if not inBoard(x,y) or a[x][y]==2: # 격자 밖이거나 영역 내에 벽이 존재하면
                    return # 움직이지 않음
                else:
                    if b[x][y]>0 and b[x][y]!=no: # 또는 영역 내 본인이 아닌 다른 기사의 영역이 존재하면
                        q.append([b[x][y],dir]) # 다음 기사도 이동 대상 큐에 넣기

    # 실제로 이동 및 기사 영역 내 함정 존재하면 데미지 입기
    for move_no in willMove:
        sx,sy=pos[move_no]
        h,w=size[move_no]
        nx,ny=sx+dx[dir],sy+dy[dir]
        pos[move_no]=[nx,ny]
        for x in range(nx,nx+h):
            for y in range(ny,ny+w):
                if a[x][y]==1:
                    if hp[move_no]>0 and sno!=move_no:
                        hp[move_no]-=1

    # 기사들 중
    for no in range(1,m+1):
        x,y=pos[no]
        h,w=size[no]
        # 탈락한 기사는 제외하고
        if hp[no]<=0:continue
        # 움직일 맵에 움직일 대상의 영역 정보 넣기
        for i in range(x, x + h):
            for j in range(y, y + w):
                tmp[i][j] = no

    b=tmp

turn=0
for turn in range(1,K+1):

    no,dir=map(int,input().split())

    if hp[no]<=0:continue

    process(no,dir)

ans=0
for no in range(1,m+1):
    if hp[no]>0:
        ans+=init_hp[no]-hp[no]
print(ans)