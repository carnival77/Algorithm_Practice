# 풀이 시간 : 약 3시간 30분
from collections import deque

n,K,m,c,d=map(int,input().split())

rx,ry=map(int,input().split())
rx-=1
ry-=1

pos=[None]*(m+1)
panic=[None]+[0]*m
point=[None]+[0]*m
tmp=[]

a=[[0]*n for _ in range(n)] # 산타 맵
for _ in range(m):
    no,x,y=map(int,input().split())
    x-=1
    y-=1
    a[x][y]=no
    pos[no]=[x,y]

#  상,우,하,좌 포함 8방향
dx=[-1,0,1,0,-1,1,-1,1]
dy=[0,1,0,-1,-1,1,1,-1]

def getDistance(x,y,nx,ny):
    return (x-nx)**2 + (y-ny)**2

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def interaction(sx,sy,xdir,ydir):
    global tmp,pos

    q=deque()
    q.append((sx,sy)) # 이번 산타 넣기

    while q:
        x,y=q.popleft() # 이번 산타가
        no=a[x][y]
        nx,ny=x+xdir,y+ydir # 다음 방향으로 움직일 때
        if inBoard(nx,ny): # 격자 내이면
            tmp[nx][ny]=no # 움직일 맵에 저장
            if a[nx][ny]>0: # 다른 산타가 존재하면
                q.append((nx,ny)) # 큐에 삽입
        else: # 격자 밖이면 탈락
            pos[no]=None

def crash(sx,sy,xdir,ydir,kind):
    global a,pos,panic,tmp,point

    no=a[sx][sy]
    a[sx][sy]=0
    tmp=[[0]*n for _ in range(n)] # 산타가 움직일 칸 저장
    ok=False

    if kind==1:
        z=c
    else:
        z=d

    point[no]+=z
    panic[no]=turn+1
    nx,ny=sx+xdir*z,sy+ydir*z
    if not inBoard(nx,ny): # 움직일 칸이 격자 밖이면 탈락
        pos[no]=None
    else:
        ok=True # 움직일 칸에 저장된 내용 맵에 반영 필요
        tmp[nx][ny]=no
        if a[nx][ny]>0: # 움직일 칸에 다른 산타가 있으면 방향 그대로 갖고 상호작용
            interaction(nx,ny,xdir,ydir)

    if ok:
        for x in range(n):
            for y in range(n):
                if tmp[x][y]>0:
                    a[x][y]=tmp[x][y]
                    no=tmp[x][y]
                    pos[no]=[x,y]

def move1():
    global rx,ry

    # 산타 선택
    cand=[]
    for no in range(1,m+1):
        if pos[no] is None:continue
        x,y=pos[no]
        dist=getDistance(x,y,rx,ry) # 모든 산타들이 위치한 칸에서 현재의 루돌프가 위치한 칸에서 가장 거리가 가까운 칸 구하기
        cand.append([dist,x,y])

    cand.sort(key=lambda x:(x[0],-x[1],-x[2]))
    tx,ty=cand[0][-2],cand[0][-1]

    # 이동할 칸 선택
    cand=[]
    for k in range(8):
        xdir=dx[k]
        ydir=dy[k]
        nx,ny=rx+xdir,ry+ydir
        dist=getDistance(nx,ny,tx,ty) # 이동하고 난 다음 칸에서 대상 산타가 있는 칸까지의 거리가 가까우면 후보에 넣기
        cand.append([dist,[nx,ny],[xdir,ydir]])

    cand.sort()
    nx,ny=cand[0][-2]
    xdir,ydir=cand[0][-1]

    # 이동할 칸에 산타 있으면 충돌
    if a[nx][ny]>0:
        crash(nx,ny,xdir,ydir,1)
    # 루돌프는 그 칸으로 이동
    rx,ry=nx,ny

def check():

    for e in pos:
        if e is not None:
            return True
    return False

def move2():
    global pos,a

    # 산타는 번호순으로 움직인다
    for no in range(1,m+1):
        if panic[no]>=turn or pos[no] is None:continue
        x,y=pos[no]
        minDist=getDistance(x,y,rx,ry)
        cand=[]
        for k in range(4):
            xdir=dx[k]
            ydir=dy[k]
            nx,ny=x+xdir,y+ydir
            if not inBoard(nx,ny) or a[nx][ny]>0:continue # 격자 밖이거나 다른 산타가 존재하는 경우는 제외
            dist=getDistance(nx,ny,rx,ry)
            if minDist>dist: # 현재 있는 칸에서 루돌프가 있는 칸까지의 거리보다 이동할 다음 칸에서 루돌프가 있는 칸까지의 거리가 가까우면(거리 값이 작으면)
                cand.append([dist,k,[nx,ny],[xdir,ydir]])

        if len(cand)>0:
            cand.sort()
            nx,ny=cand[0][-2]
            xdir,ydir=cand[0][-1]
            a[x][y]=0
            a[nx][ny]=no
            pos[no]=[nx,ny]

            # 움직일 칸에 루돌프 존재하면, 반대 방향 좌표와 함께 다음 칸으로 이동
            if (nx,ny)==(rx,ry):
                crash(nx,ny,-xdir,-ydir,2)

def getPoint():
    global point

    for no in range(1,m+1):
        if pos[no] is not None:
            point[no]+=1

turn=0
for turn in range(1,K+1):
    # 루돌프 이동
    move1()
    # 산타 존재 여부
    if not check():
        break
    # 산타 이동
    move2()
    # 산타 존재 여부
    if not check():
        break
    # 생존 산타 점수 1 획득
    getPoint()

print(*point[1:])