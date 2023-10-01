n,m,K=map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)] # 0이라면, 빈 칸. 1이상 9이하의 값을 갖는다면, 벽을 의미하며, 해당 값은 내구도
b=[[[] for _ in range(n)] for _ in range(n)] # 플레이어 및 출구 맵. [] : 빈 칸, [1~10] : 참가자 번호, [-1] : 출구
ans=0

# 움직일 수 있는 칸이 2개 이상이라면, 상하로 움직이는 것을 우선시합니다.
#  상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for no in range(1,m+1):
    x,y=map(int,input().split())
    x-=1
    y-=1
    b[x][y].append(no)

tx,ty=map(int,input().split()) # 출구 좌표
tx-=1
ty-=1
b[tx][ty].append(-1)

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

# 두 위치 (x1,y1), (x2,y2)의 최단거리는 ∣x1−x2∣+∣y1−y2∣로 정의됩니다.
# 모든 참가자는 동시에 움직입니다.
# 상하좌우로 움직일 수 있으며, 벽이 없는 곳으로 이동할 수 있습니다.
# 움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단 거리가 가까워야 합니다.
# 움직일 수 있는 칸이 2개 이상이라면, 상하로 움직이는 것을 우선시합니다.
# 참가가가 움직일 수 없는 상황이라면, 움직이지 않습니다.
# 한 칸에 2명 이상의 모험가가 있을 수 있습니다.
def move():
    global b,ans

    tmp=[[[] for _ in range(n)] for _ in range(n)] # 움직일 맵

    for x in range(n):
        for y in range(n):
            if len(b[x][y])>0 and b[x][y][0]!=-1:
                dist=abs(x-tx)+abs(y-ty)
                cand=[]
                ok = False
                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k]
                    if not inBoard(nx,ny) or a[nx][ny]>0:continue
                    ndist = abs(nx - tx) + abs(ny - ty)
                    cand.append([ndist,k,nx,ny])
                if len(cand)>0:
                    cand.sort()
                    for ndist,k,nx,ny in cand:
                        # 움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단 거리가 가까워야 합니다.
                        # 참가자가 움직일 수 없는 상황이라면, 움직이지 않습니다.
                        if ndist<dist:
                            ok=True
                            ans+=len(b[x][y])
                            # 참가자가 출구 칸에 도달하면, 즉시 탈출합니다.
                            # 한 칸에 2명 이상의 모험가가 있을 수 있습니다.
                            if (nx,ny)!=(tx,ty):
                                for no in b[x][y]:
                                    tmp[nx][ny].append(no)
                        if ok:
                            break
                if not ok:
                    for no in b[x][y]:
                        tmp[x][y].append(no)
    tmp[tx][ty].append(-1)
    b=tmp

def find(sx,sy,length):

    ok1,ok2=False,False
    for x in range(length):
        for y in range(length):
            if len(b[sx+x][sy+y])>0 and (sx+x,sy+y)!=(tx,ty):
                ok1=True
            if (sx+x,sy+y)==(tx,ty):
                ok2=True
    if ok1 and ok2:
        return True
    else:
        return False

# 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡습니다.
# 가장 작은 크기를 갖는 정사각형이 2개 이상이라면, 좌상단 r 좌표가 작은 것이 우선되고, 그래도 같으면 c 좌표가 작은 것이 우선됩니다.
def getSquareInfo():

    cand=[]

    for x in range(n):
        for y in range(n):
            MAX=min(n-x,n-y)
            for length in range(2,MAX+1):
                if not inBoard(x+(length-1),y+(length-1)):continue
                ok=find(x,y,length)
                if ok:
                    cand.append([length,x,y])
    cand.sort()
    length,sx,sy=cand[0]

    return [length,sx,sy]

def rotateClockwise(a):
    return list(map(list,zip(*a[::-1])))

def getSquare(length,sx,sy):

    square1=[[0]*length for _ in range(length)] # 벽 맵 정사각형
    square2 = [[[] for _ in range(length)] for _ in range(length)]
    for x in range(length):
        for y in range(length):
            square1[x][y]=a[sx+x][sy+y]
            square2[x][y]=b[sx+x][sy+y][:]

    return [square1,square2]

# 선택된 정사각형은 시계방향으로 90도 회전하며, 회전된 벽은 내구도가 1씩 깎입니다.
def rotate(square1,square2):
    global a,b,tx,ty

    square1=rotateClockwise(square1)
    square2=rotateClockwise(square2)

    for x in range(length):
        for y in range(length):
            a[sx + x][sy + y] = square1[x][y]
            b[sx + x][sy + y] = square2[x][y]
            if a[sx + x][sy + y]>0:
                a[sx + x][sy + y]-=1
            if len(b[sx+x][sy+y])>0 and b[sx+x][sy+y][0]==-1:
                tx,ty=sx+x,sy+y

def check():
    for x in range(n):
        for y in range(n):
            if len(b[x][y]) > 0 and b[x][y][0] != -1:
                return False
    return True

for turn in range(1,K+1):

    # 참가자 이동
    move()
    # 모든 참가자가 미로를 탈출
    if check():
        break
    # 미로 회전
    # 정사각형 시작점 및 길이 선정
    length,sx,sy=getSquareInfo()
    # 정사각형 선정
    s1,s2=getSquare(length,sx,sy)
    # 정사각형 회전
    rotate(s1,s2)

print(ans)
print(tx+1,ty+1)