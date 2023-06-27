import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]

c1=[[False] * n for _ in range(n)]
c1[n-1][0]=c1[n-1][1]=c1[n-2][0]=c1[n-2][1]=True
ans=0

dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def move(d,s):
    global c1

    tmp=[[False] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if c1[x][y]:
                nx=(x+dx[d]*s)%n
                ny=(y+dy[d]*s)%n
                tmp[nx][ny]=True

    c1=tmp

def plus():
    global p

    for x in range(n):
        for y in range(n):
            if c1[x][y]:
                a[x][y]+=1
                p[x][y]=True

def copy():
    global a

    b=[row[:] for row in a]
    for x in range(n):
        for y in range(n):
            if p[x][y]:
                cnt=0
                for k in range(1,8,2):
                    nx,ny=x+dx[k],y+dy[k]
                    if inBoard(nx,ny) and a[nx][ny]>0:
                        cnt+=1
                b[x][y]+=cnt
    a=b

def create():
    global c1

    for x in range(n):
        for y in range(n):
            if not c1[x][y] and a[x][y]>=2:
                c2[x][y]=True
                a[x][y]-=2

    c1=[row[:] for row in c2]

for _ in range(m):
    d,s=map(int,input().split())
    d-=1

    p=[[False] * n for _ in range(n)]
    c2=[[False] * n for _ in range(n)]

    # 1. 구름 이동
    move(d,s)

    # 2. 물 증가
    plus()

    # 4. 물 복사 버그
    copy()

    # 5. 구름 생성
    create()

for x in range(n):
    for y in range(n):
        ans+=a[x][y]
print(ans)