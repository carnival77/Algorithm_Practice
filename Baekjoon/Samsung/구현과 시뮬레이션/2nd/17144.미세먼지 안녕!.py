import sys

input=sys.stdin.readline

n,m,t=map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)]
ans=0
s1,s2=0,0

#  우,상,좌,하
dx=[0,-1,0,1]
dy=[1,0,-1,0]

for x in range(n):
    for y in range(m):
        if a[x][y]==-1:
            if s1==0:
                s1=x
            else:
                s2=x

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<m:
        return True
    return False

# 미세먼지 확산
def diffuse():
    global a

    b=[row[:] for row in a]

    for x in range(n):
        for y in range(m):
            if a[x][y]<5:
                continue
            cnt=0
            for k in range(4):
                nx,ny=x+dx[k],y+dy[k]
                if not inBoard(nx,ny) or (nx,ny)==(s1,0) or (nx,ny)==(s2,0):
                    continue
                cnt+=1
                b[nx][ny]+=a[x][y]//5
            b[x][y]-=a[x][y]//5*cnt
    a=b

def clean(sx,sy,k):
    global a

    d=0
    x,y=sx+dx[d],sy+dy[d]
    pre=a[x][y]
    a[x][y]=0
    while True:
        nx,ny=x+dx[d],y+dy[d]
        if (nx,ny)==(sx,sy):
            break
        if not inBoard(nx,ny):
            d=(d+k)%4
            nx,ny=x+dx[d],y+dy[d]
        now=a[nx][ny]
        a[nx][ny]=pre
        pre=now
        x,y=nx,ny

for _ in range(t):
    # 미세먼지 확산
    diffuse()

    # 공기청정기 작동
    clean(s1,0,1)
    clean(s2,0,-1)

for x in range(n):
    for y in range(m):
        if a[x][y]==-1:
            continue
        ans+=a[x][y]

print(ans)