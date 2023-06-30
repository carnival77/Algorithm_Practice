import sys
from itertools import product
from copy import deepcopy

input=sys.stdin.readline

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
ans=int(1e9)
cnt=0
cpos=[]
cno=[]

#  우,하,좌,상
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<m:
        return True
    return False

def check(a,pos,d):
    x,y=pos
    nx,ny=x+dx[d],y+dy[d]
    while inBoard(nx,ny):
        if a[nx][ny]==6:
            break
        elif a[nx][ny]==0:
            a[nx][ny]='#'
        x,y=nx,ny
        nx,ny=x+dx[d],y+dy[d]
    return a

# 맵의 각 cctv의 번호와 위치에서 주어진 방향대로 감시 영역 표시
def watch(a,d,pos,no):
    if no==1:
        a=check(a,pos,d)
    elif no==2:
        a=check(a,pos,d)
        a=check(a,pos,(d+2)%4)
    elif no==3:
        a = check(a, pos, d)
        a = check(a, pos, (d+1)%4)
    elif no==4:
        a = check(a, pos, d)
        a = check(a, pos, (d+1)%4)
        a = check(a, pos, (d + 2) % 4)
    return a

def process(a,prod):
    result=0
    # 각 감시 방향대로 cctv 방향 조정 후 사각지대 크기 측정
    for inx,d in enumerate(prod):
        a=watch(a,d,cpos[inx],cno[inx])
    for x in range(n):
        for y in range(m):
            if a[x][y]==0:
                result+=1
    return result

for x in range(n):
    for y in range(m):
        if a[x][y]=='#':
            continue
        if 1<=a[x][y]<=4:
            cno.append(a[x][y])
            cpos.append([x,y])
            cnt += 1
        elif a[x][y]==5:
            for d in range(4):
                a=check(a,[x,y],d)

# 모든 cctv의 감시 방향 조합의 경우의 수
for prod in product([0,1,2,3],repeat=cnt):
    # 이번 감시 방향 조합으로 사각지대 최소 크기 구하기
    res=process(deepcopy(a),prod)
    ans=min(ans,res)

print(ans)