import sys
input=sys.stdin.readline

n,m,K=map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)] # 벽 보드
b=[[[] for _ in range(n)] for _ in range(n)] # 참가자 보드. 참가자의 no가 담김

for no in range(m):
    px,py=map(int,input().split())
    px-=1
    py-=1
    b[px][py].append(no)

ex,ey=map(int,input().split()) # 출구
ex-=1
ey-=1
a[ex][ey]=-1 # 벽 보드에 출구 표시
cnt=0 # 참가자 이동거리 합

#  상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def move():
    global cnt,b

    npos=[None]*m # 참가자 이동예정 위치
    # 격자 내 참가자 존재 위치 찾고
    for x in range(n):
        for y in range(n):
            if len(b[x][y])==0: continue # 참가자 없으면 스킵
            dist=abs(ex-x)+abs(ey-y) # 현재 칸 ~ 출구까지 최단거리
            for no in b[x][y]: # 현재 칸에 있는 각 참가자별
                cand=[] # 움직일 칸 후보
                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k] # 상,하,좌,우 순 탐색 (상하 우선)
                    if not inBoard(nx,ny) or a[nx][ny]>0:continue  # 벽이거나 격자 밖이면 이동 불가
                    ndist=abs(ex-nx)+abs(ey-ny)
                    if dist>ndist:
                        cand.append([nx,ny])
                if len(cand)==0:
                    npos[no]=[x,y] # 움직일 수 있는 칸 없으면 이동 X
                else:
                    nx,ny=cand[0]
                    cnt+=1 # 이동 거리 증가
                    npos[no]=[nx,ny] # 해당 참가자의 이동예정 위치 추가

    tmp=[[[] for _ in range(n)] for _ in range(n)] # 이동예정 보드
    for no in range(m):
        if npos[no]==None: continue # 참가자가 존재하지 않으면 스킵
        nx,ny=npos[no]
        if (nx,ny)==(ex,ey):continue # 출구면 탈출. 이동예정 보드에 넣지 않음
        tmp[nx][ny].append(no)
    b=tmp # 모든 참가자 동시 이동

def check():
    for x in range(n):
        for y in range(n):
            if len(b[x][y])>0:
                return False
    return True

def find():

    cand=[] # 정사각형 후보
    # (0,0)부터 차례로 탐색
    for x in range(n-1):
        for y in range(n-1):
            for l in range(2,n): # 한 변의 길이는 2~n-1
                if not inBoard(x + l-1, y + l-1): continue  # 격자 밖 탐색이면 스킵
                ok1=False # 출구 존재
                ok2=False # 참가자 존재
                # (x,y) 위치에서 한 변의 길이가 l인 정사각형 공간 탐색
                for i in range(l):
                    for j in range(l):
                        nx,ny=x+i,y+j
                        if (nx,ny)==(ex,ey): # 출구 존재 여부
                            ok1=True
                        if len(b[nx][ny])>0: # 참가자 존재 여부
                            ok2=True
                if ok1 and ok2: # 둘 다 존재하면
                    cand.append([l,x,y]) # 정사각형 후보 추가
    cand.sort() # 크기가 가장 작으며, 좌상단 x 오름차순, y 오름차순
    return cand[0]

def getSquare(kind,a,length,sx,sy):
    if kind==1:
        tmp=[[0]*length for _ in range(length)]
    else:
        tmp=[[[] for _ in range(length)] for _ in range(length)]

    for i in range(length):
        for j in range(length):
            tmp[i][j]=a[sx+i][sy+j]

    return tmp

def rotateClockwise(a):
    return list(map(list,zip(*a[::-1])))

def decrease(a,length):

    for x in range(length):
        for y in range(length):
            if a[x][y]>0:
                a[x][y]-=1

    return a

def adjustSquare(a,tmp,length,sx,sy):
    for i in range(length):
        for j in range(length):
            a[sx+i][sy+j]=tmp[i][j]
    return a

def updateExit():
    global ex,ey

    for x in range(n):
        for y in range(n):
            if a[x][y]==-1:
                ex,ey=x,y

def rotate():
    global a,b

    length,sx,sy=find() # 한 명 이상의 참가자와 출구 포함한 정사각형의 정보(한 변 길이, 죄상단 위치) 얻기
    asquare=getSquare(1,a,length,sx,sy) # 벽 보드 정사각형 얻기
    bsquare=getSquare(2,b,length,sx,sy) # 참가자 보드 정사각형 얻기
    rotated_asquare=rotateClockwise(asquare) # 시계방향 90도 회전
    rotated_bsquare=rotateClockwise(bsquare)
    rotated_asquare=decrease(rotated_asquare,length) # 벽보드 정사각형 내구도 -1
    a=adjustSquare(a,rotated_asquare,length,sx,sy) # 정사각형 원래 보드에 적용
    b=adjustSquare(b,rotated_bsquare,length,sx,sy)
    updateExit() # 출입구 위치 업데이트

for round in range(1,K+1):
    # 참가지 이동
    move()
    # 참가자 체크 - 참가자가 하나도 없을 경우 중단
    if check():
        break
    # 미로 회전
    rotate()

print(cnt)
print(ex+1,ey+1)