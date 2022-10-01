# # (k,k) ~ (k,n-1-(k+1))
# # (k,n-1-k) ~ (n-1-(k+1),n-1-k)
# # (n-1-k,n-1-k) ~ (n-1-k,k+1)
# # (n-1-k,k) ~ (k+1,k)
#
# import math
#
# n=int(input())
# a=[list(map(int,input().split())) for _ in range(n)]
# ans=0
# # 시계방향
# #  상,우,하,좌
# dx=[-1,0,1,0]
# dy=[0,1,0,-1]
#
# def get_rotate_path(n):
#     reversed_path=[]
#     for k in range(n//2+1):
#         for i in range(k,n-1-k):
#             reversed_path.append((k,i))
#         for i in range(k,n-1-k):
#             reversed_path.append((i,n-1-k))
#         for i in range(n-1-k,k,-1):
#             reversed_path.append((n-1-k,i))
#         for i in range(n-1-k,k,-1):
#             reversed_path.append((i,k))
#     reversed_path.append((n//2,n//2))
#     return list(reversed(reversed_path))
#
# def rotate(path,i,n):
#     nx,ny=path[i]
#     if 0<=nx<n and 0<=ny<n:
#         return True
#     else:
#         return False
#
# def sand(x,y,num):
#     global a,ans
#     if 0<=x<n and 0<=y<n:
#         a[x][y]+=num
#     else:
#         ans+=num
#     return num
#
# def spread(k,x,y):
#     global a
#     Y=a[x][y]
#     alpha=Y
#     # 앞, 오른쪽 10%
#     # alpha-=sand(x+dx[k]+dy[k],y+dy[k]+dx[k],math.trunc(Y*0.1))
#     alpha-=sand(x+dx[k]+dy[k],y+dy[k]+dx[k],Y*10//100)
#     # 앞, 왼쪽 10%
#     # alpha-=sand(x + dx[k] - dy[k], y + dy[k] + dx[k], math.trunc(Y * 0.1))
#     alpha-=sand(x + dx[k] - dy[k], y + dy[k] + dx[k], Y*10//100)
#     # 두 칸 앞 5%
#     # alpha-=sand(x+2*dx[k],y+2*dy[k],math.trunc(Y*0.05))
#     alpha-=sand(x+2*dx[k],y+2*dy[k],Y*5//100)
#     # 오른쪽 7%
#     # alpha-=sand(x+dy[k],y+dx[k],math.trunc(Y*0.07))
#     alpha-=sand(x+dy[k],y+dx[k],Y*7//100)
#     # 왼쪽 7%
#     # alpha-=sand(x-dy[k],y+dx[k],math.trunc(Y*0.07))
#     alpha-=sand(x-dy[k],y+dx[k],Y*7//100)
#     # 뒤, 오른쪽 1%
#     # alpha-=sand(x-dx[k]+dy[k],y-dy[k]+dx[k],math.trunc(Y*0.01))
#     alpha-=sand(x-dx[k]+dy[k],y-dy[k]+dx[k],Y*1//100)
#     # 뒤, 왼쪽 1%
#     # alpha-=sand(x-dx[k]-dy[k],y-dy[k]+dx[k],math.trunc(Y*0.01))
#     alpha-=sand(x-dx[k]-dy[k],y-dy[k]+dx[k],Y*1//100)
#     # 두 칸 오른쪽 2%
#     # alpha-=sand(x+2*dy[k],y+2*dx[k],math.trunc(Y*0.02))
#     alpha-=sand(x+2*dy[k],y+2*dx[k],Y*2//100)
#     # 두 칸 왼쪽 2%
#     # alpha-=sand(x-2*dy[k],y+2*dx[k],math.trunc(Y*0.02))
#     alpha-=sand(x-2*dy[k],y+2*dx[k],Y*2//100)
#     # 알파. 한 칸 앞
#     sand(x + dx[k], y + dy[k], alpha)
#     a[x][y]=0
#
# def process(now,next):
#     x,y=now
#     nx,ny=next
#     # 방향 찾기
#     dx=nx-x
#     dy=ny-y
#     # 상
#     if (dx,dy)==(-1,0):
#         spread(0,nx,ny)
#     # 우
#     elif (dx,dy)==(0,1):
#         spread(1,nx,ny)
#     # 하
#     elif (dx,dy)==(1,0):
#         spread(2,nx,ny)
#     # 좌
#     elif (dx,dy)==(0,-1):
#         spread(3,nx,ny)
#
# path=get_rotate_path(n)
# sx=sy=n//2
# i=0
# MAX=n*n-2
# while True:
#     if i<=MAX and rotate(path,i+1,n):
#         process(path[i],path[i+1])
#         print(path[i],path[i+1])
#         i+=1
#     else:
#         break
# print(ans)


# 회전 : 가운데 칸부터 시작해서, 계속해서 방향을 90도 반시계 방향 회전하며 이동하다가, 회전해서 이동할 칸이 이미 처리한 칸이면 회전하지 않는 방식으로 탐색
# 모래 : 모래의 이동과 비율은 기준이 되는 방향을 하나 미리 구하고(좌) 그 기준을 계속해서 90도 반시계 방향 회전 시키면 4가지 방향(상,하,좌,우)에 대한 이동과 기준 구할 수 있다.
# 방향 : 방향 (dx,dy) -> (-dy,dx)로 바꾸면 90도 반시계 방향 회전

# 바람에 의해 모래가 옮겨지는 지점 및 비율
class Wind:
    def __init__(self,dx,dy,ratio):
        self.dx=dx
        self.dy=dy
        self.ratio=ratio

# 반시계방향
#  좌,하,우,상
dx=[0,1,0,-1]
dy=[-1,0,1,0]
spread=[]

# 반시계 방향으로 바람 경로 회전
def rotate(points):
    res=[]
    for p in points:
        nx=-p.dy
        ny=p.dx
        res.append(Wind(nx,ny,p.ratio))
    return res

# 상하좌우 방향별 모래 흩뿌리는 지점 리스트 저장
def make_spread():
    # 좌 방향
    points=[]
    points.append(Wind(1,-1,10))
    points.append(Wind(-1,-1,10))
    points.append(Wind(-1,0,7))
    points.append(Wind(1,0,7))
    points.append(Wind(-1,1,1))
    points.append(Wind(1,1,1))
    points.append(Wind(0,-2,5))
    points.append(Wind(-2,0,2))
    points.append(Wind(2,0,2))
    spread.append(points)
    # 하, 우, 상 방향
    for _ in range(3):
        points=rotate(points)
        spread.append(points)

# 격자 내부/외부 선별하여 내부이면 모래양 +, 외부이면 ans +
def inout(x,y,cur):
    global a,n
    if 0<=x<n and 0<=y<n:
        a[x][y]+=cur
        return 0
    else:
        return cur

make_spread()
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
visit=[[False]*n for _ in range(n)] # 해당 칸이 처리되었는지 나타냄
order=[[0] * n for _ in range(n)] # 디버깅용
ans=0
x,y=n//2,n//2
visit[x][y]=True
cnt=2 # 디버깅용
order[x][y]=1
k=0 # 방향

while True:
    # 다음 이동할 칸 선별/방문
    nx,ny=x+dx[k],y+dy[k]
    order[nx][ny]=cnt
    cnt+=1
    visit[nx][ny]=True
    # (x,y) -> (nx,ny)
    sand=a[nx][ny]
    used=0
    a[nx][ny]=0
    # 칸 이동
    x,y=nx,ny

    # 해당 방향으로 모래 흩뿌리기
    for p in spread[k]:
        nx,ny=x+p.dx,y+p.dy
        cur=sand*p.ratio//100
        used+=cur
        ans+=inout(nx,ny,cur)
    sand-=used
    nx,ny=x+dx[k],y+dy[k]
    ans+=inout(nx,ny,sand)

    # (0,0) 칸이면 중지
    if (x,y)==(0,0):
        break

    # 다음 탐색할 방향 설정
    nk=(k+1)%4
    nx,ny=x+dx[nk],y+dy[nk]
    if not visit[nx][ny]:
        k=nk

print(ans)