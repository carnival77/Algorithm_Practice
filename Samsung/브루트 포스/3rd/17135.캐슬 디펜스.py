import sys
from itertools import combinations
from collections import deque

input=sys.stdin.readline

n,m,d=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]+[[0]*m]
ans=0

arr=[i for i in range(m)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def check(a):
    for x in range(n):
        for y in range(m):
            if a[x][y]==1:
                return True
    return False

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<m:
        return True
    return False

def bfs(a,sx,sy):

    cand=[]

    q=deque()
    q.append((sx,sy))
    visit=[[False]*m for _ in range(n)]+[[False]*m]
    visit[sx][sy]=True

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            dist=abs(sx-nx)+abs(sy-ny)
            if inBoard(nx,ny) and not visit[nx][ny] and dist<=d:
                q.append((nx,ny))
                visit[nx][ny]=True
                if a[nx][ny]==1:
                    cand.append([dist,[ny,nx]])

    return cand

def attack(a):

    for x in comb:
        a[n][x]=2

    cnt=0
    b=[row[:] for row in a]

    for x in comb:
        cand=bfs(a,n,x)
        if len(cand)==0: continue
        cand.sort()
        ty,tx=cand[0][1]
        if b[tx][ty]==1:
            b[tx][ty]=0
            cnt+=1

    return [b,cnt]

def move(a):

    for i in range(n-1,0,-1):
        a[i]=a[i-1][:]
        a[i-1]=[0]*m

    return a

for comb in combinations(arr,3):
    res=0
    b=[row[:] for row in a]
    while check(b):
        # 공격
        b,cnt=attack(b)
        res+=cnt
        # 이동
        b=move(b)
    ans=max(ans,res)

print(ans)