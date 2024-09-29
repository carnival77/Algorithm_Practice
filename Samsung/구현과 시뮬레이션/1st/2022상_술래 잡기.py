import sys
input=sys.stdin.readline

n,m,h,turn=map(int,input().split())

board=[[0]*n for _ in range(n)]
rboard=[[[] for _ in range(n)] for _ in range(n)] # 도망자 보드
#    우,하,좌,상
dx1 = [0, 1, 0, -1]
dy1 = [1, 0, -1, 0]
#  하,우,상,좌
dx2=[1,0,-1,0]
dy2=[0,1,0,-1]

dx,dy=None,None

sx,sy,sd=(n-1)//2,(n-1)//2,0 # 술래 위치 및 주시 방향
ans=0

# 도망자 클래스
class Runaway:
    def __init__(self,no,way,dir,x,y):
        self.no=no # 번호
        self.way=way # 이동 방식. 1:좌우, 2:상하
        self.dir=dir # 주시 방향. 0,1,2,3=하,우,상,좌
        # 위치
        self.x=x
        self.y=y

rs=[] # 도망자 클래스 객체 배열
inx=1 # 술래 이동 인덱스

def inBoard(nx,ny):
    return 0<=nx<n and 0<=ny<n

# 술래 이동 경로 배열 얻기
# 이동 후의 위치가 만약 이동방향이 틀어지는 지점이라면, 방향을 바로 틀어줍니다
# 만약 이동을 통해 양끝에 해당하는 위치인 (1행, 1열) 혹은 정중앙에 도달하게 된다면 이 경우 역시 방향을 바로 틀어줘야 함에 유의
def getMoves(kind):
    global dx,dy # kind에 따라 전역변수 dx,dy 값 수정

    moves=[] # [x좌표,y좌표,주시 방향]

    # 안->밖
    if kind==1:
        #    우,하,좌,상
        dx,dy=dx1,dy1
        # 가운데 칸 저장
        x = (n - 1) // 2
        y = (n - 1) // 2
        # 주시 방향은 위측
        d=3
        moves.append([x,y,d])

        # 각 레이어는 3~n 범위의 홀수들만큼의 변의 길이를 가진다.
        for size in range(3, n + 1, 2):
            # 다음 레이어로 갈 때 위로 한 칸
            x += dx[3]
            y += dy[3]
            # 주시 방향은 우측
            d=0
            moves.append([x,y,d])
            # 이번 레이어를 우,하,좌,상 순서로 탐색
            for d in range(4):
                # (size-1)만큼 loop를 돌며,
                loop = size - 1
                # 오른쪽 방향으로는 (loop-1)만큼 loop를 돈다.
                if d == 0:
                    loop -= 1
                # 해당 loop 만큼 이동한다.
                for i in range(loop):
                    x += dx[d]
                    y += dy[d]
                    # 방향이 틀어지는 곳에서 저장할 주시 방향을 바꿔준다
                    if i==loop-1 and d!=3:
                        d=(d+1)%4
                    moves.append([x,y,d])

        # [0,0]의 방향은 아래로 저장
        moves[-1][2]=1

    # 밖->안
    elif kind==2:
        #  하,우,상,좌
        dx,dy=dx2,dy2

        visit=[[False]*n for _ in range(n)]
        x,y,d=0,0,0
        visit[x][y]=True
        moves.append([x,y,d])

        for _ in range(n**2-1):
            nx,ny=x+dx[d],y+dy[d]
            if inBoard(nx,ny) and not visit[nx][ny]:
                pass
            # 전진할 칸이 범위 밖이거나 이미 방문했다면, 방향 바꾸고 전진할 칸 바꾸고 이번 칸의 주시 방향도 바뀐 방향으로 바꾸기
            else:
                d=(d+1)%4
                nx,ny=x+dx[d],y+dy[d]
                moves[-1][2]=d
            visit[nx][ny]=True
            moves.append([nx,ny,d])
            x,y=nx,ny

        # 가운데 칸의 방향은 위로 저장
        moves[-1][2]=2

    return moves

# 도망자 이동.
# dx,dy는 하,우,상,좌인 dx2,dy2로 고정
def move():

    for r in rs:
        rx,ry=r.x,r.y
        # 도망자가 움직일 때 현재 술래와의 거리가 3 이하인 도망자만 움직입니다.
        # 도망자의 위치가 (x1, y1), 술래의 위치가 (x2, y2)라 했을 때 두 사람간의 거리는 |x1 - x2| + |y1 - y2|로 정의됩니다.
        if abs(rx-sx)+abs(ry-sy)<=3:
            d=r.dir
            x,y=rx,ry
            nx,ny=x+dx2[d],y+dy2[d]
            # 현재 바라보고 있는 방향으로 1칸 움직인다 했을 때 격자를 벗어나는 경우
            if not inBoard(nx,ny):
                # 먼저 방향을 반대로 틀어줍니다.
                d=(d+2)%4
                r.dir=d
                nx, ny = x + dx2[d], y + dy2[d]
            # 움직이려는 칸에 술래가 있지 않다면 해당 칸으로 이동
            if (nx,ny)!=(sx,sy):
                r.x,r.y=nx,ny
                rboard[x][y].remove(r)
                rboard[r.x][r.y].append(r)

# 잡힌 도망자 데이터 삭제
def removeRunaway(x,y):
    for r in rboard[x][y]:
        rs.remove(r)
    rboard[x][y].clear()

# 술래의 시야는 현재 바라보고 있는 방향을 기준으로 현재 칸을 포함하여 총 3칸
def catch(x,y,d,t):
    # 현재 kind에 맞는 dx,dy대로 감시
    global ans,dx,dy

    for i in range(3):
        nx,ny=x+dx[d]*i,y+dy[d]*i
        if not inBoard(nx,ny):continue
        # 나무가 있다면
        if board[nx][ny]==1:
            continue
        cnt=len(rboard[nx][ny])
        if cnt>0:
            ans+=cnt*t
            removeRunaway(nx,ny)

# 데이터 받기
for no in range(m):
    x,y,way=map(int,input().split())
    x-=1
    y-=1
    # 도망자의 종류는 좌우로만 움직이는 유형과 상하로만 움직이는 유형 이렇게 2가지가 있습니다.
    # 이때 좌우로 움직이는 사람은 항상 오른쪽을 보고 시작하며, 상하로 움직이는 사람은 항상 아래쪽을 보고 시작합니다.
    if way==1:
        dir=1
    else:
        dir=0
    r=Runaway(no,way,dir,x,y)
    rs.append(r)
    rboard[x][y].append(r)

for _ in range(h):
    x,y=map(int,input().split())
    board[x-1][y-1]=1

# 술래 이동 경로 구분. 1: 내부->외부, 2: 외부->내부
kind=1
# 술래 이동 경로 배열 얻기
moves=getMoves(kind)

for t in range(1,turn+1):
    # 도망자 이동
    move()

    # 술래 이동
    sx,sy,sd=moves[inx]

    # 도망자 잡고 점수 획득
    catch(sx,sy,sd,t)

    # 술래 전방 이동할 칸 없으면 반대로 이동 경로로 이동 시작
    if inx==n**2-1:
        inx=0
        if kind==1:
            kind=2
        elif kind==2:
            kind=1
        # 술래 이동 경로 배열 얻기
        moves = getMoves(kind)
    inx+=1

print(ans)