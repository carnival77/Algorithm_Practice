import sys
input=sys.stdin.readline

class Horse:
    def __init__(self,no,x,y,d):
        self.no=no
        self.x=x
        self.y=y
        self.d=d

#  우,좌,상,하
dx=[0,0,-1,1]
dy=[1,-1,0,0]

n,k=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
b=[[[] for _ in range(n)] for _ in range(n)]
horses=[]
for i in range(1,k+1):
    x,y,d=map(int,input().split())
    x-=1
    y-=1
    d-=1
    horse=Horse(i,x,y,d)
    horses.append(horse)
    b[x][y].append(horse)

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def reverse_direction(d):
    if d==0: return 1
    elif d==1: return 0
    elif d==2: return 3
    else: return 2

def move():
    global horses,b

    for horse in horses:
        no,x,y,d=horse.no,horse.x,horse.y,horse.d
        # # 해당 말이 맨 아래에 있는 지
        # if b[x][y][0].no!=no:
        #     continue
        nx,ny=x+dx[d],y+dy[d]
        # 체스판 벗어나는 경우 or 파란색
        if not inBoard(nx,ny) or a[nx][ny]==2:
            # 방향 반대로
            d=reverse_direction(d)
            horse.d=d
            # 다음 칸
            nx,ny=x+dx[d],y+dy[d]
            # 체스판 벗어나는 경우 or 파란색
            if not inBoard(nx,ny) or a[nx][ny]==2:
                continue
        # 흰색 or 빨간색
        if 0<=a[nx][ny]<=1:
            # 이동할 말 그룹 선정
            pos=b[x][y].index(horse)
            hs=b[x][y][pos:]
            # 다음 칸으로 이동 후 이전 칸 비우기
            b[x][y]=b[x][y][:pos]
            # 이동할 모든 말 좌표 변경
            for h in hs:
                h.x,h.y=nx,ny
            # 빨간색
            if a[nx][ny]==1:
                hs.reverse()
            # 말 얹기
            for h in hs:
                b[nx][ny].append(h)
            # 말 개수 체크 : 4개 이상 쌓이는 순간 게임이 종료
            if len(b[nx][ny])>=4:
                print(time)
                sys.exit(0)
            # # 다음 칸으로 이동 후 이전 칸 비우기
            # b[x][y].clear()

# def check(time):
#     for i in range(n):
#         for j in range(n):
#             if len(b[i][j])>=4:
#                 print(time)
#                 sys.exit(0)

time=1
for _ in range(1,1001):
    #말 이동
    move()
    time+=1

print(-1)